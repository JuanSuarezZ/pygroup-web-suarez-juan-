from flask import Flask
from proyecto_flask.products.views import ruta





app = Flask(__name__)
app.register_blueprint(ruta)


if __name__ == "__main__":
    app.run(debug = True)