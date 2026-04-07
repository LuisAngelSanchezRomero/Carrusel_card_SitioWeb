from flask import Flask, render_template
import os
from datetime import datetime

#inicializar la aplicacion en flask
app = Flask(__name__)

#rutas
@app.route("/")
def index():
    imagenes = [
        "static/image/Captura de pantalla 2025-02-18 232647.png",
        "static/image/Captura de pantalla 2025-02-18 233038.png",
        "static/image/Captura de pantalla 2025-02-18 234504.png",
        "static/image/Captura de pantalla 2025-02-18 234910.png",
        "static/image/Captura de pantalla 2025-02-18 235218.png",
        "static/image/Captura de pantalla 2025-02-18 235742.png",
    ]
    return render_template("index.html", imagenes=imagenes, year=datetime.now().year)

#ejecutar mi servidor
if __name__ == '__main__':
    app.run(debug=True)