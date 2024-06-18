# Reciclaje Inteligente con YOLO

Este proyecto implementa un sistema de reciclaje inteligente utilizando la biblioteca YOLO para la detección de objetos. El sistema identifica y clasifica diferentes tipos de materiales reciclables en tiempo real utilizando una cámara web.

## Descripción del Proyecto

La aplicación utiliza el modelo YOLO para detectar y clasificar cinco tipos de materiales reciclables:
- Metal
- Vidrio
- Plástico
- Cartón
- Material Médico

## Tecnologías Utilizadas

- **Lenguaje de Programación:** Python
- **Modelo de Detección de Objetos:** [YOLO](https://github.com/ultralytics/yolov5)
- **Interfaz Gráfica:** Tkinter
- **Procesamiento de Imágenes:** OpenCV, Pillow
- **Manipulación de Arreglos:** NumPy

## Requisitos

- Python 3.x
- Bibliotecas necesarias:
  - `tkinter`
  - `Pillow`
  - `imutils`
  - `cv2` (OpenCV)
  - `numpy`
  - `ultralytics`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/kwok1216/reciclaje-inteligente.git
   cd reciclaje-inteligente

    Crea un entorno virtual e instala las dependencias:

    bash

    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    pip install -r requirements.txt

Uso

    Asegúrate de tener los archivos de imágenes necesarios en el directorio setUp:
        Canva.png
        metal.png, vidrio.png, plastico.png, carton.png, medical.png
        metaltxt.png, vidriotxt.png, plasticotxt.png, cartontxt.png, medicaltxt.png

    Coloca el modelo YOLO entrenado (best.pt) en el directorio Modelos.

    Ejecuta la aplicación:

    bash

    python main.py

Estructura del Código
main.py

    clean_labels(): Limpia las etiquetas de las imágenes en la GUI.
    update_images(detection_img, classification_img): Actualiza las etiquetas de imágenes con las imágenes proporcionadas.
    perform_scanning(): Maneja el escaneo de video y la detección de objetos.
    setup_main_window(): Configura la ventana principal de la aplicación e inicializa el modelo y la captura de video.

Estructura de Directorios

css

reciclaje-inteligente/
│
├── Modelos/
│   └── best.pt
│
├── setUp/
│   ├── Canva.png
│   ├── metal.png
│   ├── vidrio.png
│   ├── plastico.png
│   ├── carton.png
│   ├── medical.png
│   ├── metaltxt.png
│   ├── vidriotxt.png
│   ├── plasticotxt.png
│   ├── cartontxt.png
│   └── medicaltxt.png
│
├── main.py
└── requirements.txt

Contribuciones

Las contribuciones son bienvenidas. Para mayores detalles, por favor abre un issue o realiza un pull request en el repositorio.
Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.
