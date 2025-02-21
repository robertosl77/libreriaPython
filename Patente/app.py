from flask import Flask, request, render_template
from buscador import Buscador

class app:
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            patente = request.form['patente'].upper()
            
            if Buscador.validar_patente(patente):
                id = Buscador.calcular(patente)
                patente_generada = Buscador.id_a_patente(id)
                mensaje=__name__
                return render_template('index.html', patente=patente, id=id, patente_generada=patente_generada, mensaje=mensaje)
            else:
                return render_template('index.html', error="Patente inválida. Debe tener el formato 'ABC123'.")
        return render_template('index.html')

    if __name__ == '__main__':
        app.run(debug=True)