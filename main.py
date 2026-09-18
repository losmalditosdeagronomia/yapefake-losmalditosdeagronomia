from PIL import Image, ImageDraw, ImageFont

# Cargar imagen original
img = Image.open(r"yape.jpg")

draw = ImageDraw.Draw(img)

# Coordenadas base
x, y = 200, 300  # esquina superior izquierda
width, height = 400, 260

# Ajustes de posición
mover_x = -120 # valores positivos mueven a la derecha
mover_y = 350   # valores positivos mueven hacia abajo

# Coordenadas ajustadas
x1 = x + mover_x
y1 = y + mover_y
x2 = x + width + mover_x
y2 = y + height + mover_y

# Dibujar un rectángulo blanco
draw.rectangle([x1, y1, x2, y2], fill="white")









# Cargar la fuente y establecer el tamaño
font = ImageFont.truetype("asimovwid.otf", 150)


texto = "100.0"
posicion = (200, 640)  

color = (59,52,86,255)  # Negro
draw.text(posicion, texto, fill=color, font=font)


texto = "Cristina V. Carbajal A."
posicion = (95, 840)  
color = (59,52,86,255)  
font = ImageFont.truetype("asimovwid.otf", 50)



draw.text(posicion, texto, fill=color, font=font)



# Cargar la fuente y establecer el tamaño
font = ImageFont.truetype("asimovwid.otf", 90)


texto = "S/"
posicion = (95, 650)  

color = (59,52,86,255)  # Negro
draw.text(posicion, texto, fill=color, font=font)

# Mostrar o guardar la imagen
img.show()
img.save("yape-dayana.png")
# img.save("imagen_editada.jpg")
