from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# Cargar imagen original
img = Image.open("yape.jpg")
draw = ImageDraw.Draw(img)

# -----------------------------------
# COORDENADAS BASE
# -----------------------------------
x, y = 200, 300
width, height = 400, 260

mover_x = -120
mover_y = 350

x1 = x + mover_x
y1 = y + mover_y
x2 = x + width + mover_x
y2 = y + height + mover_y

# Rectángulo blanco
draw.rectangle([x1, y1, x2, y2], fill="white")


# -----------------------------------
# MONTO
# -----------------------------------
font = ImageFont.truetype("asimovwid.otf", 150)

texto = "100.0"
posicion = (200, 640)
color = (59, 52, 86)

draw.text(posicion, texto, fill=color, font=font)


# -----------------------------------
# NOMBRE
# -----------------------------------
texto = "Cristina V. Carbajal A."
posicion = (95, 840)

font = ImageFont.truetype("asimovwid.otf", 50)

draw.text(posicion, texto, fill=color, font=font)


# -----------------------------------
# S/
# -----------------------------------
font = ImageFont.truetype("asimovwid.otf", 90)

texto = "S/"
posicion = (95, 650)

draw.text(posicion, texto, fill=color, font=font)


# -----------------------------------
# FECHA Y HORA ACTUALES
# -----------------------------------

ahora = datetime.now()

# Ejemplo:
# 18 sept. 2026
# 10:45 a. m.

fecha = ahora.strftime("%d %b. %Y")

hora = ahora.strftime("%I:%M %p")

# Convertir AM/PM a formato usado visualmente
hora = hora.replace("AM", "a. m.").replace("PM", "p. m.")

texto_fecha_hora = f"{fecha} | {hora}"

font_fecha = ImageFont.truetype("asimovwid.otf", 32)

# Coordenada de ejemplo para una MAQUETA
posicion_fecha = (150, 900)

draw.text(
    posicion_fecha,
    texto_fecha_hora,
    fill=(90, 86, 105),
    font=font_fecha
)


# -----------------------------------
# MARCA DE MAQUETA
# -----------------------------------

font_demo = ImageFont.truetype("asimovwid.otf", 28)

draw.text(
    (130, 760),
    "DEMO - EJEMPLO",
    fill=(180, 0, 0),
    font=font_demo
)


# -----------------------------------
# GUARDAR
# -----------------------------------

img.show()
img.save("yape_demo.png")