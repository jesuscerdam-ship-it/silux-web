from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/descargar/<tipo>")
def descargar(tipo):

    archivos = {
        "portable": "Silux.zip",
        "instalador": "SILUX_4.0_Setup.exe"
    }

    if tipo not in archivos:
        abort(404)

    archivo = archivos[tipo]

    ruta = os.path.join(
        DOWNLOADS_DIR,
        archivo
    )

    if not os.path.isfile(ruta):
        abort(404)

    return send_from_directory(
        DOWNLOADS_DIR,
        archivo,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
