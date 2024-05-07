# Sistemas Operativos
Explora este repositorio para descubrir cómo aprovechar una ESP-CAM como cámara IP para realizar reconocimiento de objetos mediante visión computacional. Encuentra guías detalladas, ejemplos de código y recursos útiles para implementar esta emocionante tecnología en tus proyectos.



## Codificación para ESP32 Cámara

Para codificar el ESP32, sigue estos pasos:

1. Abre el proyecto en el Arduino IDE.
2. Modifica las credenciales de red en el archivo `CameraWebServer_AP.h` según tus preferencias, ingresando tu SSID y contraseña.

   ![image](https://github.com/JanerBolivar/Sistemas-Operativos/assets/101657362/a1cd3108-f3d2-4d97-a129-d89a7f754f28)

4. Guarda los cambios.

Luego, en la sección de herramientas del Arduino IDE, selecciona lo siguiente:

- **Placa:** ESP32S3 Dev Module

  ![image](https://github.com/JanerBolivar/Sistemas-Operativos/assets/101657362/ca909b82-32a2-466c-852a-415ce0778533)

  
- **Puerto:** El puerto al que está conectado tu ESP32

  ![image](https://github.com/JanerBolivar/Sistemas-Operativos/assets/101657362/471c96f0-8d63-44ad-bdf3-26c5e7f7a995)




Presiona el botón de subir código en el Arduino IDE. Cuando aparezca el mensaje "Subiendo (Upload)", presiona el botón BOOT en tu ESP32 y mantenlo presionado hasta que se complete la carga del código.

¡Listo! Tu ESP32 está ahora codificado y listo para funcionar como cámara.



## Ejecución del Script de Python

Para ejecutar el script de Python, sigue estos pasos:

1. Ejecuta todos los comandos que se muestran en el archivo `Librerias.txt`.

Además, asegúrate de realizar las siguientes modificaciones:

- Actualiza la ruta donde se encuentra ubicado el modelo previamente entrenado (`best.pt`).

  ![image](https://github.com/JanerBolivar/Sistemas-Operativos/assets/101657362/db39141a-21cb-4aa6-9fcb-84cba7938426)

  
- Modifica la ruta donde se encuentra el archivo JSON que contiene la información sobre los diferentes monumentos.

  ![image](https://github.com/JanerBolivar/Sistemas-Operativos/assets/101657362/44a9762c-9e9c-4c1a-a3ba-4bb0059a7616)


¡Listo! Ahora el script de Python está configurado y listo para ser ejecutado.

**Recuerda que el ordenador donde se ejecute el script de Python debe estar conectado a la misma red que el ESP32.**

