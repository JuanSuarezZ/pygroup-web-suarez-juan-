from app import app


@app.route('/mirutaa')
def index():
    return "hola pygroup"