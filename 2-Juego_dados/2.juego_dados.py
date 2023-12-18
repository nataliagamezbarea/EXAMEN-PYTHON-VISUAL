import tkinter as tk
from PIL import Image, ImageTk
import random

def mostrar_dado(root, canvas, img_dados, mensaje_label, movements_left=10):
    canvas.delete("all")
    num = random.randint(1, 6)
    imagen_dado = img_dados[num - 1]
    canvas.create_image(200, 200, anchor=tk.CENTER, image=imagen_dado)
    mensaje_label.config(text=f"El dado muestra el número {num}")

    movements_left -= 1
    if movements_left > 0:
        root.after(100, mostrar_dado, root, canvas, img_dados, mensaje_label, movements_left)

def main():
    root = tk.Tk()
    root.title('Animación de Dado')

    display_width = 400
    display_height = 400

    canvas = tk.Canvas(root, width=display_width, height=display_height)
    canvas.pack()

    img1 = ImageTk.PhotoImage(Image.open('img/dado1.png'))
    img2 = ImageTk.PhotoImage(Image.open('img/dado2.png'))
    img3 = ImageTk.PhotoImage(Image.open('img/dado3.png'))
    img4 = ImageTk.PhotoImage(Image.open('img/dado4.png'))
    img5 = ImageTk.PhotoImage(Image.open('img/dado5.png'))
    img6 = ImageTk.PhotoImage(Image.open('img/dado6.png'))

    img_dados = [img1, img2, img3, img4, img5, img6]

    mensaje_label = tk.Label(root, text="")
    mensaje_label.pack()

    boton_dado = tk.Button(root, text="Lanzar Dado", command=lambda: mostrar_dado(root, canvas, img_dados, mensaje_label))
    boton_dado.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
