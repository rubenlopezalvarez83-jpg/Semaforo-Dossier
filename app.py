from flask import Flask, render_template, request, session, redirect               #IMPORTAMOS FLASK
from preguntas import PREGUNTAS, PUNTUACION_MAXIMA, UMBRAL_VERDE, UMBRAL_AMARILLO  #IMPORTAMOS LAS PREGUNTAS Y LAS PUNTUACIONES CON LAS QUE TRABAJAMOS

# CREAMOS LA APLICACIÓN Y LE DIREMOS EN QUÉ CARPETA ESTAMOS TRABAJANDO 

app = Flask(__name__)
app.secret_key = "semaforo_dossier_2026" #CONTRASEÑA QUE VAMOS A PONER DE FORMA INTERNA

#************************************************************

@app.route("/") #ESTA FUNCIÓN LE DICE A FLASK QUE CUANDO EL CIUDADANO ENTRE EN LA DIRECCIÓN PRINCIPAL DE LA APP SE EJECUTE LA FUNCIÓN INICIO
def inicio():
    return render_template("inicio.html") #BUSCA EN LA CARPETA TEMPLATES EL ARCHIVO HTML INICIO Y LO PONDRÁ EN EL NAVEGADOR

#********************************************************************************************************************

@app.route("/iniciar")                               # al pulsar el botón iniciar cuestionario, en navegador irá a la dirección iniciar y flask ejecutará la función
def iniciar():                                       # definimos la función iniciar
    session["puntuacion"] = 0                        # session será una memoria temporal de la app, creamos una puntuación para cada sesión y lo iniciamos a cero
    session["pregunta_actual"] = 1                   # creamos una variable para saber en qué pregunta estamos y la iniciamos en la primera pregunta
    session["senales"] = []                          # aquí guardamos las respuestas de sí o no estoy seguro
    return render_template("cuestionario.html",      # devolvemos la página del cuestionario y mandamos los datos
                           pregunta=PREGUNTAS[0],    # la pregunta 0 es la primera porque las listas en python empiezan en cero
                           total=len(PREGUNTAS))     # número total de preguntas (recorrido de las preguntas)

#**********************************************************************************************************
# PARTE CENTRAL DEL ALGORITMO - VAMOS A PROCESAR LAS RESPUESTAS DADAS POR EL USUARIO

@app.route("/responder", methods=["POST"])                    # POST es un método privado que es más seguro para enviar datos, o sea las respuestas
def responder():                                              # función responder - definimos
    respuesta = request.form["respuesta"]                           # Flask abrirá el sobre de POST y extraerá la respuesta según lo pulsado por el ciudadano
    numero = session["pregunta_actual"]                             # indicamos el número de la pregunta en el que vamos
    pregunta = PREGUNTAS[numero - 1]                                # recorremos las preguntas

    # Sumamos los puntos según la respuesta dada
    if respuesta == "si":
        session["puntuacion"] += pregunta["valor_si"]
        session["senales"].append(pregunta["texto"])
    elif respuesta == "nose":
        session["puntuacion"] += pregunta["valor_nose"]
        session["senales"].append(pregunta["texto"])

    # Avanzamos a la siguiente pregunta
    session["pregunta_actual"] += 1

    # ¿Quedan más preguntas?    ----- Si quedan seguimos con la siguiente, si no quedan devuelve el resultado al fondo con redirect
    if session["pregunta_actual"] <= len(PREGUNTAS):
        siguiente = PREGUNTAS[session["pregunta_actual"] - 1]
        return render_template("cuestionario.html",
                               pregunta=siguiente,
                               total=len(PREGUNTAS))
    else:
        return redirect("/resultado")
    
# ************************************************************************************************************
# ahora SE CREA LA FUNCIÓN QUE VA A DEVOLVER EL RESULTADO DEL ALGORITMO 

@app.route("/resultado")
def resultado():
    puntuacion = session["puntuacion"]                                      # Aquí se recupera la puntuación final acumulada en el cuestionario
    senales = session["senales"]                                            # Recupera la lista de señales con las que advertiremos al usuario

    # Calcula el nivel de riesgo según la puntuación y le da el consejo que se ha decidido según dicha puntuación
    if puntuacion < UMBRAL_VERDE:
        nivel = "verde"
        titulo = "Riesgo bajo"
        mensaje = "No se han detectado señales claras de fraude. \
Aun así, mantenga la precaución y verifique siempre \
por canales oficiales."
    elif puntuacion < UMBRAL_AMARILLO:
        nivel = "amarillo"
        titulo = "Riesgo medio"
        mensaje = "Se han detectado algunas señales de alerta. \
Le recomendamos que no actúe precipitadamente y consulte \
con su entidad bancaria por el número oficial."
    else:
        nivel = "rojo"
        titulo = "Riesgo alto"
        mensaje = "Se han detectado señales claras de posible fraude. \
No realice ninguna transferencia ni facilite datos. \
Cuelgue y contacte con su banco por el número oficial."

    return render_template("resultado.html",                                # AQUÍ EN LA PÁGINA DE RESULTADO, SE MANDARÁ CINCO DATOS QUE USARÁ EN HTML
                           puntuacion=puntuacion,
                           nivel=nivel,
                           titulo=titulo,
                           mensaje=mensaje,
                           senales=senales)

# SE ARRANCA LA APLICACIÓN ------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)       # debug=True muestra dónde está el fallo en el navegador si se comete un error en el código