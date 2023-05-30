from flask import Flask, render_template # Flask es la clase, render template para trabajar con los archivos html,css,js

app = Flask(__name__) # name hace referencia al archivo donde estamos

@app.route("/") # estas son rutas
def Saludo():
    return render_template('index.html', titulo='Practica') #variable con str y en html la invocamos con {{}}

@app.route("/index")
def presentacion():
    dic = {
        "titulo":"Practicas Flask",
        "encabezado":"Bienvenid@ a mi pagina",
        "parrafo":"Este parrafo es de prueba"
    }
    return render_template('index.html', dic=dic ) #en html se los pasa con parametro {{dic.titulo}}, {{dic.encabezado}}, {{dic.parrafo}}

@app.route("/contacto")
def contacto():
    dic = {
        "titulo":"Contacto",
        "encabezado":"Bienvenid@ a Contacto",
        "parrafo":"Este parrafo es de prueba en contactos"
    }
    return render_template('contacto.html', dic=dic)

@app.route("/base")
def base():
    dic = {
        "titulo":"Base",
        "encabezado":"Bienvenid@ a Base",
        "parrafo":"Este parrafo es de prueba en base"
    }
    return render_template('base.html', dic=dic)

@app.route("/saludo/<int:valor1>/<int:valor2>")
def saludo(valor1,valor2):
    return f"La suma es: {valor1 + valor2}"


@app.route("/lenguajes")
def lenguajes():
    dic = {
        "titulo":"Lenguajes",
        "encabezado":"Bienvenid@ a Lenguajes",
        "parrafo":"Este parrafo es de prueba en Lenguajes",
        "condicion":True,
        "lenguajes":["JS","HTML","CSS","C#","PHP"],
        
    }
  
    return render_template('lenguajes.html', dic=dic)

app.run('localhost', port=3000, debug=True) #corremos nuestro server, con debug True recarga aut el server
