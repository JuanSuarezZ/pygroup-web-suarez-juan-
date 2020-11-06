from flask import Flask
from flask import render_template

app = Flask(__name__)


#from app.products import views
#from app.products.views import products


@app.route('/mirutaa/<name>')
def hindex(name=None):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run(debug = True)