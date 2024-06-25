import torch
import numpy as np
from PIL import Image
import cv2
from ultralytics import YOLO
from supervision import BoxAnnotator
from supervision.detection.core import Detections

class ObjectDetection:
    def __init__(self, capture_index):
        self.capture_index = capture_index
        self.model = self.load_model()
        self.CLASS_NAMES_DICT = self.model.model.names
        self.box_annotator = BoxAnnotator(thickness=3, text_thickness=3, text_scale=1.5)

    def load_model(self):
        model = YOLO('C:/Users/arand/OneDrive/Desktop/TFG/runs/detect/train6/weights/best.pt')
        model.fuse()
        return model

    def predict(self, frame):
        results = self.model(frame)
        return results

    def plot_bboxes(self, results, frame, confidence_threshold=0.75):
        detections = Detections(
            xyxy=results[0].boxes.xyxy.cpu().numpy(),
            confidence=results[0].boxes.conf.cpu().numpy(),
            class_id=results[0].boxes.cls.cpu().numpy().astype(int),
        )

        high_conf_detections_indices = detections.confidence > confidence_threshold
        detections = Detections(
            xyxy=detections.xyxy[high_conf_detections_indices],
            confidence=detections.confidence[high_conf_detections_indices],
            class_id=detections.class_id[high_conf_detections_indices],
        )

        self.labels = [f"{self.CLASS_NAMES_DICT[class_id]} {confidence:0.2f}"
                       for confidence, class_id in zip(detections.confidence, detections.class_id)]

        frame = self.box_annotator.annotate(scene=frame, detections=detections, labels=self.labels)
        return frame

    def __call__(self):
        cap = cv2.VideoCapture(self.capture_index)
        assert cap.isOpened()
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 576)

        while True:
            ret, frame = cap.read()
            assert ret

            results = self.predict(frame)
            frame = self.plot_bboxes(results, frame, confidence_threshold=0.60)

            #im=Image.fromarray(frame)
            #im.show()
            cv2.imshow('YOLOv8 Detection', frame)

            key = cv2.waitKey(5) & 0xFF

            # Si se ha presionado una tecla, rompe el bucle
            if key != 255:
                break

        cap.release()
        cv2.destroyAllWindows()


import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk, ExifTags
from ultralytics import YOLO
import cv2
import numpy as np

dic = {0: "Liquidambar. Liquidambar styraciflua",
       1: "Castaño de indias. Aesculus hippocastanum",
       2: "Cinamomo. Melia azedarach",
       3: "Falsa acacia. Robinia pseudoacacia",
       4: "Ciruelo rojo. Prunus cerasifera",
       5: "Aligustre del Japón. Ligustrum japonicum",
       6: "Arce real. Acer platanoides",
       7: "Olivo. Olea europaea",
       8: "Olmo de Siberia. Ulmus pumila"
       }

ventana = tk.Tk()
ventana.geometry("920x800")  # Tamaño de la ventana
ventana.title('Comprobador')
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(ventana, text='Seleccione una foto de su dispositivo', width=30, font=my_font1)
l1.grid(row=1, column=1)


def correct_image_orientation(image):
    # Función para corregir la orientación de la imagen
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = image._getexif()
        if exif is not None:
            if exif[orientation] == 3:
                image = image.rotate(180, expand=True)
            elif exif[orientation] == 6:
                image = image.rotate(270, expand=True)
            elif exif[orientation] == 8:
                image = image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        pass
    return image


def upload_file():
    global img
    f_types = [('Archivos jpg', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    img = correct_image_orientation(img)  # Corregir la orientación de la imagen
    img.thumbnail((375, 500))
    img = ImageTk.PhotoImage(img)
    b2 = tk.Button(ventana, image=img, command=lambda: predict(filename))
    b2.grid(row=3, column=1)


def predict(path):
    global imgn
    model= YOLO('C:/Users/arand/OneDrive/Desktop/TFG/runs/detect/train6/weights/best.pt')
    #model = YOLO('./runs/detect/train6/weights/best.pt')
    img = cv2.imread(path)
    results = model.predict(img, stream=True, save=False, imgsz=320, conf=0.6)
    for r in results:
        im_array = r.plot()  # Plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im = im.resize((375, 500))
        # im = correct_image_orientation(im)
    imgn = ImageTk.PhotoImage(im)
    b3 = tk.Label(ventana, image=imgn)  # Mostrar la imagen en una etiqueta en lugar de un botón
    b3.image = imgn  # Asegurar que la imagen no se elimine
    b3.grid(row=3, column=2)

    l = []
    for i in range(len(r.boxes.data)):
        l = l + [int(r.boxes.data[i - 1][5])]
    d = dict(zip(l, map(lambda x: l.count(x), l)))
    # print(d)
    tipos = list(d.keys())
    cant = list(d.values())
    for j in range(len(list(d.values()))):
        print(f" Hay {cant[j - 1]} hojas del tipo{tipos[j - 1]}. Hoja de {dic[tipos[j - 1]]}")
        my_font2 = ('times', 12, 'bold')
        li = tk.Label(ventana, text=f" Hay {cant[j - 1]} hojas del tipo{tipos[j - 1]}. Hoja de {dic[tipos[j - 1]]}",
                      font=my_font2)
        li.grid(row=4 + j, column=1)


b1 = tk.Button(ventana, text='Subir foto', width=20, command=upload_file)
b1.grid(row=2, column=1)
b8 = tk.Button(ventana, text='Prediccion en tiempo real con camara', width=60, command=ObjectDetection(capture_index=0))
b8.grid(row=2, column=2)

ventana.mainloop()  # Mantener la ventana abierta