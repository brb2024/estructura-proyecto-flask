from flask import Flask, render_template


# Crear app
app = Flask(__name__)

# Ruta principal
@app.route("/")
def index():
    return render_template("index.html")

# Ejecutar al ejecutar main.py
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080, debug = True)