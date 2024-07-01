RECONOCIMIENTO DE HOJAS EN TIEMPO REAL.

Este repositorio contiene los recursos necesarios para utilizar un modelo de reconocimiento de hojas en tiempo real, capaz de detectar e identificar 30 especies diferentes de árboles a partir de fotos de sus hojas.

----------Contenido del Repositorio----------------


0.  Para probar una versión básica del demostrador sin necesidad de utilizar un entorno de desarrollo, puedes acceder al archivo 'demostrador_basico', que da acceso a un archivo de Google Colab en el que está cargado el modelo y se puede poner a prueba. Nota: para poner a prueba el modelo puedes utilizar por ejemplo alguna de las imágenes de los archivos 'images1' o 'images2'

1.  Imágenes de la Base de Datos:
'images' contienen todas las imágenes utilizadas para entrenar y validar el modelo. Estas imágenes representan las diferentes especies de árboles y sus hojas.

2.  Etiquetado de Imágenes:
El archivo 'labels' proporciona el etiquetado de todas las imágenes en el formato YOLOv8. Estos datos son fundamentales para el entrenamiento y la evaluación del modelo.

3.  Código de Implementación:
El archivo 'demostrador' contiene un código que permite a los usuarios utilizar el modelo para reconocimiento en tiempo real. Este script facilita la interacción con el modelo entrenado para identificar especies de árboles a partir de imágenes de hojas.

4.  Configuración para Entrenamiento:
En el archivo 'configuración' se encuentra la configuración necesaria para aquellos interesados en entrenar el modelo desde cero o realizar ajustes en el mismo. En ese archivo en la primera línea se debe copiar en "path:", la ruta a la carpeta del dataset. Para entrenar un modelo desde cero, habrá que ejecutar el archivo 'train_detection' asegurándose de colocar la ruta al archivo 'configuracion' correctamente.

Importante: La carpeta que utiliza el archivo 'configuracion' para cargar el dataset debe tener la siguiente estructura. Debe incluir dos carpetas llamadas "images" y "labels". En cada una de estas dos carpetas debe haber tres carpetas, llamadas "test", "train" y "val". En las carpetas "test", "train" y "val" de la carpeta "images" irán las imágenes destinadas al test, entrenamiento y validacción respectivamente. En las carpetas "test", "train" y "val" de la carpeta "labels" irán las etiquetas pertenecientes a las imágenes que se han colocado en estas tres carpetas anteriormente. Para facilitar este reparto en carpetas y la división del dataset en entrenamiento, test y validación, se puede utilizar el código 'split_dataset', que permite seleccionar los porcentajes que se van a emplear en entrenamiento, test y validación y reparte las imágenes y sus etiquetas de manera adecuada.

5.  Demostrador:
Para poner a prueba el modelo de reconociemiento de hojas se ha subido el archivo 'best.pt' que contiene la arquitectura, los pesos y los sesgos de la red entrenada. En el archivo 'demostrador' se ecnuentra el código que permite poner a prueba el modelo con una interfaz sencilla para el usuario. 

IMPORTANTE! Asegúrate de colocar adecuadamente la ruta al archivo "best.pt" en el código de 'demostrador'.
En caso de haber entrenado desde cero tu propio modelo, al terminar el entrenamiento se habrán guardado los pesos "best.pt" del modelo en una carpeta de tu dispositivo. Este archivo "best.pt" es el que deberás utilizar en el demostrador 'demostrador' para poner a prueba tu modelo.


----------------Contacto---------------------

Para cualquier pregunta, sugerencia o problema relacionado con el uso de este repositorio, por favor contacta con [mig.algaba@gmail.com].

¡Esperamos que este modelo sea útil!
