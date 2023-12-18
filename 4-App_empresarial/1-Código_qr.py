import qrcode
from flask import Flask, send_file, render_template
from io import BytesIO

app = Flask(__name__)

# Función para generar un código QR que redirija a una URL
def generate_qr_with_url(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Ruta para generar y mostrar el código QR que redirige a una URL
@app.route('/')
def generate_qr():
    url = 'nataliagamezbarea.github.io/EXAMEN-PYTHON-VISUAL/4-App_empresarial/2-Correo_electronico.html'
    qr_img = generate_qr_with_url(url)
    img_io = BytesIO()
    qr_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

# Ruta para servir la página index.html
if __name__ == '__main__':
    app.run(debug=True)  # Asegúrate de incluir la ejecución de la aplicación Flask
