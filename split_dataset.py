import os
import shutil
import random

def split_dataset(input_folder_images, input_folder_labels, output_folder1_images, output_folder2_images, output_folder3_images, 
                  output_folder1_labels, output_folder2_labels, output_folder3_labels, split_ratio_train=0.7, split_ratio_val=0.15):
    # Obtener la lista de archivos en la carpeta de entrada de imágenes
    image_files = os.listdir(input_folder_images)
    # Mezclar los archivos aleatoriamente
    random.shuffle(image_files)

    # Calcular los índices de división
    split_index_train = int(len(image_files) * split_ratio_train)
    split_index_val = split_index_train + int(len(image_files) * split_ratio_val)

    # Dividir los archivos en tres listas
    train_image_files = image_files[:split_index_train]
    val_image_files = image_files[split_index_train:split_index_val]
    test_image_files = image_files[split_index_val:]

    # Crear las carpetas de salida para las imágenes si no existen
    os.makedirs(output_folder1_images, exist_ok=True)
    os.makedirs(output_folder2_images, exist_ok=True)
    os.makedirs(output_folder3_images, exist_ok=True)

    # Copiar los archivos de entrenamiento de imágenes a la primera carpeta
    for image_file in train_image_files:
        shutil.copy(os.path.join(input_folder_images, image_file), os.path.join(output_folder1_images, image_file))

    # Copiar los archivos de validación de imágenes a la segunda carpeta
    for image_file in val_image_files:
        shutil.copy(os.path.join(input_folder_images, image_file), os.path.join(output_folder2_images, image_file))

    # Copiar los archivos de prueba de imágenes a la tercera carpeta
    for image_file in test_image_files:
        shutil.copy(os.path.join(input_folder_images, image_file), os.path.join(output_folder3_images, image_file))

    # Obtener la lista de archivos en la carpeta de entrada de etiquetas
    label_file = os.listdir(input_folder_labels)

    # Crear las carpetas de salida para las etiquetas si no existen
    os.makedirs(output_folder1_labels, exist_ok=True)
    os.makedirs(output_folder2_labels, exist_ok=True)
    os.makedirs(output_folder3_labels, exist_ok=True)

    # Copiar las etiquetas correspondientes a los archivos de entrenamiento
    for image_file in train_image_files:
        label_file = os.path.splitext(image_file)[0] + ".txt"  # Se asume que los nombres de archivos coinciden
        shutil.copy(os.path.join(input_folder_labels, label_file), os.path.join(output_folder1_labels, label_file))

    # Copiar las etiquetas correspondientes a los archivos de validación
    for image_file in val_image_files:
        label_file = os.path.splitext(image_file)[0] + ".txt"  # Se asume que los nombres de archivos coinciden
        shutil.copy(os.path.join(input_folder_labels, label_file), os.path.join(output_folder2_labels, label_file))

    # Copiar las etiquetas correspondientes a los archivos de prueba
    for image_file in test_image_files:
        label_file = os.path.splitext(image_file)[0] + ".txt"  # Se asume que los nombres de archivos coinciden
        shutil.copy(os.path.join(input_folder_labels, label_file), os.path.join(output_folder3_labels, label_file))

if __name__ == "__main__":
    input_folder_images = ""
    input_folder_labels = ""
    
    output_folder1_images = ""
    output_folder2_images = ""
    output_folder3_images = ""
    
    output_folder1_labels = ""
    output_folder2_labels = ""
    output_folder3_labels = ""

    split_dataset(input_folder_images, input_folder_labels, output_folder1_images, output_folder2_images, output_folder3_images,
                  output_folder1_labels, output_folder2_labels, output_folder3_labels)

