# Importación de bibliotecas
from tkinter import *
from PIL import Image, ImageTk
import imutils
import cv2
import numpy as np
from ultralytics import YOLO
import math

# Funciones auxiliares
def clean_labels():
    """Limpia las etiquetas de las imágenes en la GUI."""
    lbl_img.config(image='')
    lbl_img_text.config(image='')

def update_images(detection_img, classification_img):
    """Actualiza las etiquetas de imágenes con las imágenes proporcionadas."""
    # Convertir y mostrar la imagen de detección
    detection_img = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(np.array(detection_img, dtype="uint8"), cv2.COLOR_RGB2BGR)))
    lbl_img.configure(image=detection_img)
    lbl_img.image = detection_img

    # Convertir y mostrar la imagen de clasificación
    classification_img = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(np.array(classification_img, dtype="uint8"), cv2.COLOR_BGR2RGB)))
    lbl_img_text.configure(image=classification_img)
    lbl_img_text.image = classification_img

def perform_scanning():
    """Maneja el escaneo de video y la detección de objetos."""
    if cap is not None:
        ret, frame = cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = model(frame_rgb, stream=True, verbose=False)
            detect = False

            for res in results:
                for box in res.boxes:
                    detect = True
                    x1, y1, x2, y2 = [int(coord) for coord in box.xyxy[0]]
                    cls = int(box.cls[0])
                    conf = math.ceil(box.conf[0] * 100)

                    # Dibujar la caja delimitadora y el texto
                    color = color_map.get(cls, (0, 255, 0))
                    cv2.rectangle(frame_rgb, (x1, y1), (x2, y2), color, 2)
                    text = f'{cls_names[cls]} {conf}%'
                    text_size, baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[:2]
                    cv2.rectangle(frame_rgb, (x1, y1 - text_size[1] - baseline), (x1 + text_size[0], y1 + baseline), (0, 0, 0), cv2.FILLED)
                    cv2.putText(frame_rgb, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

                    # Actualizar las imágenes de clasificación
                    update_images(img_map[cls], imgtxt_map[cls])

            if not detect:
                clean_labels()

            frame_resized = imutils.resize(frame_rgb, width=640)
            frame_display = ImageTk.PhotoImage(image=Image.fromarray(frame_resized))
            lbl_video.configure(image=frame_display)
            lbl_video.image = frame_display

        lbl_video.after(10, perform_scanning)

def setup_main_window():
    """Configura la ventana principal de la aplicación e inicializa el modelo y la captura de video."""
    global cap, lbl_video, model, cls_names, img_map, imgtxt_map, lbl_img, lbl_img_text, color_map

    root = Tk()
    root.title("Reciclaje Inteligente")
    root.geometry("1280x720")

    # Fondo de la interfaz
    bg_image = PhotoImage(file="setUp/Canva.png")
    Label(root, image=bg_image).place(x=0, y=0, relwidth=1, relheight=1)

    # Cargar el modelo YOLO
    model = YOLO('Modelos/best.pt')

    # Definir las clases y asignar imágenes
    cls_names = ['Metal', 'Glass', 'Plastic', 'Carton', 'Medical']
    img_map = {0: cv2.imread("setUp/metal.png"), 1: cv2.imread("setUp/vidrio.png"), 2: cv2.imread("setUp/plastico.png"), 3: cv2.imread("setUp/carton.png"), 4: cv2.imread("setUp/medical.png")}
    imgtxt_map = {0: cv2.imread("setUp/metaltxt.png"), 1: cv2.imread("setUp/vidriotxt.png"), 2: cv2.imread("setUp/plasticotxt.png"), 3: cv2.imread("setUp/cartontxt.png"), 4: cv2.imread("setUp/medicaltxt.png")}
    color_map = {0: (255, 255, 0), 1: (255, 255, 255), 2: (0, 0, 255), 3: (150, 150, 150), 4: (255, 0, 0)}

    # Configurar etiquetas de video y detección
    lbl_video = Label(root)
    lbl_video.place(x=320, y=180)
    lbl_img = Label(root)
    lbl_img.place(x=75, y=260)
    lbl_img_text = Label(root)
    lbl_img_text.place(x=995, y=310)

    # Iniciar la captura de video
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    perform_scanning()
    root.mainloop()

if __name__ == "__main__":
    setup_main_window()

