import cv2
import numpy as np
import requests
import json


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
ruta_json = r"C:Ejemplo/tourist-sites.json"


# Función para detectar y decodificar el QR en el frame
def detectar_qr(frame):
    # Inicializar el detector QR de OpenCV
    detector = cv2.QRCodeDetector()
    # Detectar y decodificar el QR en el frame
    valor, puntos, _ = detector.detectAndDecode(frame)
    # Si se detecta un QR, imprimir su valor
    if valor:
        print("Valor del QR:", valor)
        return valor



camera_ip = '192.168.128.2'
camera_port = 8080

video_url = f'http://{camera_ip}:{camera_port}/video'

cap = cv2.VideoCapture(video_url)

while True:
    ret, frame = cap.read()

    # Detectar objetos en el frame utilizando YOLOv5
    if frame is not None:
        id_clase = detectar_qr(frame)
        if id_clase is not None:
            actualizar_estado(ruta_json, id_clase)

    # Mostrar el resultado de la detección en una ventana
    cv2.imshow('Detector de Celulares', frame)

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()