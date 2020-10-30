from flask import Flask
app = Flask(__name__)


#from app.products import views
#from app.products.views import products



@app.route('/mirutaa')
def index():
    return "hola pygroup"



if __name__ == "__main__":
    app.run(debug = True)