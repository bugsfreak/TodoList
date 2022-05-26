#importar Flask
from flask import Flask, render_template,request,redirect,url_for
import pandas as pd
from sqlalchemy import table
#inicializar variable
app = Flask(__name__, template_folder='paginas')
#define la ruta

listaTareas = []
listaResponsables = []
listaPrioridad = []
listaTareasCompletas = []

#Define la ruta para index que se encuentra en HTML
@app.route('/')
def principal():
    
    return render_template('principal.html', listaTareas = listaTareasCompletas)

    

#Define la ruta para contacto que también se encuentra en HTML
@app.route('/enviar', methods=['GET','POST'])
def enviar():
    if(request.method == "POST"):
        tareas = request.form['tarea']
        listaTareas.append(tareas)
        responsables = request.form['responsable']
        listaResponsables.append(responsables)
        prioridades = request.form['prioridad']
        listaPrioridad.append(prioridades)
        listaTareasCompletas.append({'tarea': tareas, 'responsable': responsables, 'prioridad': prioridades })
        return redirect(url_for('principal'))

@app.route('/borrar', methods=["GET","POST"])
def borrar():
    if(request.method == "POST"):
        listaTareas.clear()
        listaResponsables.clear()
        listaPrioridad.clear()
        listaTareasCompletas.clear()
        return redirect(url_for('principal'))


def success(name):
    return 'Welcome %s ' % name

    
@app.route("/tabla", methods=["GET", "POST"])
def show_tables():
    info = list(zip(listaTareas,listaResponsables,listaPrioridad))
    data = pd.DataFrame(info)

    return data.to_html(header="true", table_id="tabla")


#Main, desde el que se ejecuta la aplicación

if __name__ == '__main__':
    app.run(debug=True)