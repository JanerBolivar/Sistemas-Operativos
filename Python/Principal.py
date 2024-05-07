import cv2
import torch
import numpy as np
import requests
import json

# Modificar el comportamiento predeterminado de pathlib
import pathlib
pathlib.PosixPath = pathlib.WindowsPath

# Cargar el modelo YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:Ejemplo/best.pt')


def actualizar_estado(json_file, nuevo_estado):
    # Abrir el archivo JSON y cargar los datos
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Actualizar el estado en los datos
    data['status'] = nuevo_estado

    # Escribir los datos actualizados de nuevo al archivo JSON
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=2)

# Ruta del archivo JSON
ruta_json = r"C:/Ejemplo/data/tourist-sites.json"



# Función para obtener la imagen del ESP32 cámara
def get_frame(url):
    response = requests.get(url)
    img_array = np.array(bytearray(response.content), dtype=np.uint8)
    frame = cv2.imdecode(img_array, -1)
    return frame

# URL de la cámara IP del ESP32
camera_ip = '192.168.4.1'
capture_url = f'http://{camera_ip}/capture'

while True:
    frame = get_frame(capture_url)

    # Detectar objetos en el frame utilizando YOLOv5
    if frame is not None:
        detect = model(frame)

        # Filtrar detecciones con más del 50% de confianza
        detections = detect.pred[0]
        confident_detections = detections[detections[:, 4] > 0.5]

        # Mostrar los datos de detección en la consola
        if len(confident_detections) > 0:
            print("Objeto detectado con más del 50% de confianza:")
            highest_confidence_detection = confident_detections[np.argmax(confident_detections[:, 4])]
            id_clase = int(highest_confidence_detection[5])
            print(f" - Clase: {highest_confidence_detection[5]}, Confianza: {highest_confidence_detection[4]}")
            print(f"    Id Clase: {id_clase}")
            actualizar_estado(ruta_json, id_clase)

        # Mostrar el resultado de la detección en una ventana
        cv2.imshow('Detector de Celulares', np.squeeze(detect.render()))

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
