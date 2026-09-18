from flask import Flask, request, render_template_string, send_file
from PIL import Image, ImageDraw, ImageFont
import io
import base64

app = Flask(__name__)


HTML = """
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Generador DEMO</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            padding: 30px;
            background: #f2f2f2;
            font-family: Arial, sans-serif;
        }

        .contenedor {
            max-width: 1100px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 15px;
        }

        h1 {
            text-align: center;
            margin-bottom: 30px;
        }

        .contenido {
            display: flex;
            gap: 40px;
            align-items: flex-start;
        }

        .formulario {
            width: 40%;
        }

        .vista {
            width: 60%;
            text-align: center;
        }

        label {
            display: block;
            margin-top: 15px;
            margin-bottom: 7px;
            font-weight: bold;
        }

        input {
            width: 100%;
            padding: 13px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 8px;
        }

        button {
            width: 100%;
            padding: 14px;
            margin-top: 25px;
            border: none;
            border-radius: 8px;
            background: #333;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background: #555;
        }

        .imagen {
            max-width: 100%;
            max-height: 650px;
            border: 1px solid #ddd;
            border-radius: 8px;
        }

        .descargar {
            display: inline-block;
            margin-top: 20px;
            padding: 14px 30px;
            background: #333;
            color: white;
            text-decoration: none;
            border-radius: 8px;
        }

        @media (max-width: 800px) {

            .contenido {
                flex-direction: column;
            }

            .formulario,
            .vista {
                width: 100%;
            }

        }
    </style>

</head>

<body>

<div class="contenedor">

    <h1>Generador de imagen DEMO</h1>

    <div class="contenido">

        <div class="formulario">

            <form method="POST">

                <label>Nombre</label>

                <input
                    type="text"
                    name="nombre"
                    placeholder="Escribe el nombre"
                    required
                >

                <label>Monto</label>

                <input
                    type="text"
                    name="monto"
                    placeholder="100.00"
                    required
                >

                <button type="submit">
                    Generar imagen
                </button>

            </form>

        </div>


        <div class="vista">

            <h2>Vista previa</h2>

            {% if imagen %}

                <img
                    class="imagen"
                    src="data:image/png;base64,{{ imagen }}"
                >

                <br>

                <a
                    class="descargar"
                    href="/descargar?imagen={{ imagen }}"
                >
                    Descargar imagen
                </a>

            {% else %}

                <p>
                    Introduce el nombre y monto para generar
                    la imagen.
                </p>

            {% endif %}

        </div>

    </div>

</div>

</body>
</html>
"""


def crear_imagen(nombre, monto):

    # Imagen original
    img = Image.open("imagen.jpg").convert("RGB")

    draw = ImageDraw.Draw(img)

    # Coordenadas originales
    x, y = 200, 300
    width, height = 400, 260

    mover_x = -120
    mover_y = 350

    x1 = x + mover_x
    y1 = y + mover_y
    x2 = x + width + mover_x
    y2 = y + height + mover_y

    # Rectángulo
    draw.rectangle(
        [x1, y1, x2, y2],
        fill="white"
    )

    color = (59, 52, 86)

    # Fuente monto
    font_monto = ImageFont.truetype(
        "asimovwid.otf",
        150
    )

    # Monto
    draw.text(
        (200, 640),
        monto,
        fill=color,
        font=font_monto
    )

    # Fuente nombre
    font_nombre = ImageFont.truetype(
        "asimovwid.otf",
        50
    )

    # Nombre
    draw.text(
        (95, 840),
        nombre,
        fill=color,
        font=font_nombre
    )

    # S/
    font_s = ImageFont.truetype(
        "asimovwid.otf",
        90
    )

    draw.text(
        (95, 650),
        "S/",
        fill=color,
        font=font_s
    )


    # Convertir imagen a memoria
    memoria = io.BytesIO()

    img.save(
        memoria,
        format="PNG"
    )

    memoria.seek(0)

    return base64.b64encode(
        memoria.getvalue()
    ).decode("utf-8")


@app.route("/", methods=["GET", "POST"])
def inicio():

    imagen = None

    if request.method == "POST":

        nombre = request.form.get("nombre", "")
        monto = request.form.get("monto", "")

        imagen = crear_imagen(
            nombre,
            monto
        )

    return render_template_string(
        HTML,
        imagen=imagen
    )


@app.route("/descargar")
def descargar():

    datos = request.args.get("imagen")

    if not datos:
        return "No hay imagen"

    imagen = base64.b64decode(datos)

    archivo = io.BytesIO(imagen)

    archivo.seek(0)

    return send_file(
        archivo,
        mimetype="image/png",
        as_attachment=True,
        download_name="imagen_demo.png"
    )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
