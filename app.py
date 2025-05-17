from flask import Flask
from data.data_productos import productos, categorias

app = Flask(__name__)

@app.route("/")
def home():
    nombre = "Julio Nicolás Martínez"
    descripcion = "Soy estudiante de informática, apasionado por el desarrollo web y las nuevas tecnologías."
    return f"Hola, soy {nombre}. {descripcion}"

@app.route("/productos")
def listar_productos():
    resultado = ""
    for producto in productos:
        resultado += f"ID: {producto['id']} - Descripción: {producto['descripcion']} - Categoría ID: {producto['categoria_id']}<br>"
    return resultado

@app.route("/categorias")
def listar_categorias():
    resultado = ""
    for categoria in categorias:
        resultado += f"ID: {categoria['id']} - Descripción: {categoria['descripcion']}<br>"
    return resultado

if __name__ == "__main__":
    app.run(debug=True)
