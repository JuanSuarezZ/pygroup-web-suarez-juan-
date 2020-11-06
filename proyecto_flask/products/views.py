from app import app


@app.route('/mirutaa')
def index():
    return "hola pygroup"


@app.route('/ruta2')
def index():
    return "hola pygroup"


@app.route('/ruta1')
def index():
    return "hola pygroup"

"""Se utiliza para renderizar plantillas, es decir despues de una peticion se puede lanzar una pagina o alguna plantilla rapidamente,
 creeria que puede servir para cuando no existe una pagina, entonces se crearia una plantilla explicando que dicha pagina no existe,
 mas alla de solo mostrar un error. para ultilizar render_template() se debe importar de la siguiente manera 
 
from flask import render_template.    un ejemplo de su uso seria
Aqui -> Definemos el route
@app.route("/")
Aqui -> Un segundo route con el nombre del parametro
@app.route('/<nombre>')
def render(nombre=None): # Inicializamos "nombre"
Aqui -> Retornamos la plantilla "index.html" y Le pasamo el parametro a el método render_template
 return render_template("index.html", nombre=nombre)
 """