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
ruta_json = r"D:Ejemplo/tourist-sites.json"


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
        id_clase = detectar_qr(frame)
        if id_clase is not None:
            actualizar_estado(ruta_json, id_clase)

    # Mostrar el resultado de la detección en una ventana
    cv2.imshow('Detector de Celulares', frame)

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()