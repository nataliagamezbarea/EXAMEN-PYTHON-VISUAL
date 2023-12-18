import tkinter as tk
from PIL import Image, ImageTk

def ver_imagen(canvas, iniX, iniY, imagen):
    canvas.create_image(iniX, iniY, anchor=tk.CENTER, image=imagen)

def mostrar_mensaje(mensaje, mensaje_label):
    mensaje_label.config(text=mensaje)

def elige_imagen(root, canvas, display_width, display_height, nombre1, nombre2, img_corazon, img_roto, img_amistad, img_interrogante, mensaje_label):
    iniX = display_width / 2
    iniY = display_height / 2

    # Borrar la imagen actual en el lienzo, si existe alguna
    canvas.delete("all")

    if nombre1 == "Maria" and nombre2 == "Pedro":
        ver_imagen(canvas, iniX, iniY, img_corazon)
        mostrar_mensaje("¡Hay amor!", mensaje_label)
    elif nombre1 == "Maria" and nombre2 == "Juan":
        ver_imagen(canvas, iniX, iniY, img_roto)
        mostrar_mensaje("No hay amor.", mensaje_label)
    elif nombre1 == "Maria" and nombre2 == "Fernando":
        ver_imagen(canvas, iniX, iniY, img_amistad)
        mostrar_mensaje("¡Hay una bonita amistad!", mensaje_label)
    else:
        ver_imagen(canvas, iniX, iniY, img_interrogante)
        mostrar_mensaje("Porfavor inserte nombres válidos.", mensaje_label)

def main():
    root = tk.Tk()
    root.title('Juego del Amor')

    display_width = 600
    display_height = 400

    canvas = tk.Canvas(root, width=display_width, height=display_height)
    canvas.pack()

    img_corazon = ImageTk.PhotoImage(Image.open('img/corazon.png'))
    img_roto = ImageTk.PhotoImage(Image.open('img/roto.jpg'))
    img_amistad = ImageTk.PhotoImage(Image.open('img/amistad.png'))
    img_interrogante = ImageTk.PhotoImage(Image.open('img/interrogante.png'))

    nombre1_label = tk.Label(root, text="Primer nombre:")
    nombre1_label.pack()
    nombre1_entry = tk.Entry(root)
    nombre1_entry.pack()

    nombre2_label = tk.Label(root, text="Segundo nombre:")
    nombre2_label.pack()
    nombre2_entry = tk.Entry(root)
    nombre2_entry.pack()

    mensaje_label = tk.Label(root, text="")  # Etiqueta para mostrar el mensaje
    mensaje_label.pack()

    def obtener_nombres():
        nombre1 = nombre1_entry.get()
        nombre2 = nombre2_entry.get()
        elige_imagen(root, canvas, display_width, display_height, nombre1, nombre2, img_corazon, img_roto, img_amistad, img_interrogante, mensaje_label)

    boton = tk.Button(root, text="Mostrar imagen", command=obtener_nombres)
    boton.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
