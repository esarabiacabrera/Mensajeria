import email
import os
from flask import Flask, render_template, flash, redirect, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import controlador
from datetime import datetime
import envioEmail

app = Flask(__name__)




app.secret_key = os.urandom(24)


@app.route("/")
def inicio():
  return render_template('login.html')


@app.route("/principal",methods=["GET", "POST"])
def validarUsuario():
  if request.method == "POST":
    correo=request.form['usuario']
    password=request.form['contrasenia']
    #hashClave = generate_password_hash(password)

    respuesta=controlador.validarUsuario(correo)

    if respuesta!= None:
      claveHash = respuesta[3]
      usuario_bd=respuesta[1]
      if(check_password_hash(claveHash, password)):
        session['usuario']=correo #creación de la variable de sesion
        flash("Usuario Logueado, "+usuario_bd)
        listaUsua=controlador.listaUsuario(correo)
        return render_template('principal.html',listaUsua=listaUsua)
      else:
          flash("Credenciales incorrectas")
          return redirect('/credencialesIncorrectas/')
    else:
          flash("Credenciales incorrectas")
          return redirect('/credencialesIncorrectas/')

@app.route("/credencialesIncorrectas/")
def credencialesIncorrectas():
    return render_template('error.html')

@app.route("/registrarUsuario")
def registrarUsuario():
       return render_template('crearCuenta.html')

@app.route("/guardarUsuario",methods=["GET", "POST"])
def guardarUsuario():
  if request.method == "POST":
    usuario=request.form['usuario']
    email=request.form['email']
    password=request.form['contrasenia']
    hashClave = generate_password_hash(password)

    codigo=datetime.now()
    codigo2=str(codigo)
    codigo2=codigo2.replace('-','')
    codigo2=codigo2.replace(' ','')
    codigo2=codigo2.replace(':','')
    codigo2=codigo2.replace('.','')
    print(codigo2)
    
    mensaje='Sr '+ usuario +', usuario su código de activación es: \n\n'+codigo2+'\n\nPor favor copie y pegue el codigo de activación para que su cuenta sea activada'
    envioEmail.enviar(email,mensaje)
    respuesta=controlador.guardarUsuario(usuario, email, hashClave,codigo2) 
    flash("El usuario se ha registrado, pendiente de activación. Por favor revise su correo, se le envio el código de activación")
    return redirect('/activarUsuario')

@app.route("/activarUsuario")
def activarUsuario():
 return render_template('activar.html')

@app.route("/activarCuenta",methods=["GET", "POST"])
def activarCuenta():
  if request.method == "POST":
    codigo=request.form['codigo']
    respuesta=controlador.activarUsuario(codigo)
    if respuesta == None:  
     flash("El codigo de activación no es correcto")
    else:
     flash("Usuario activado exitosamente")   
  return redirect('/activarUsuario')



   
      
