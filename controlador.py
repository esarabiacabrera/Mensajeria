import sqlite3
from sqlite3 import Error

def validarUsuario(usuario):
 db=sqlite3.connect('Mensajeria.db')
 db.row_factory=sqlite3.Row
 cursor=db.cursor()
 resultado = cursor.execute('SELECT * FROM usuarios WHERE correo = ? and estado=?', (usuario,1)).fetchone()
 return resultado

def listaUsuario(usuario):
 db=sqlite3.connect('Mensajeria.db')
 db.row_factory=sqlite3.Row
 cursor=db.cursor()
 cursor.execute("SELECT * FROM usuarios WHERE correo <> ? ",[usuario])
 resultado = cursor.fetchall()
 return resultado

def guardarUsuario(usuario, correo, password,codigoActivacion):
 db=sqlite3.connect('Mensajeria.db')
 db.row_factory=sqlite3.Row
 cursor=db.cursor()
 cursor.execute('INSERT INTO usuarios (nombreUsuario,correo,contrasena,estado,codigoActivacion) VALUES (?,?,?,?,?)', (usuario,correo,password,0,codigoActivacion))
 db.commit()
 return "1"

def activarUsuario(codigo):
  db=sqlite3.connect('Mensajeria.db')
  db.row_factory=sqlite3.Row
  cursor=db.cursor()
  cursor.execute('UPDATE  usuarios SET estado=? WHERE codigoActivacion=?', (1,codigo))
  db.commit()
  resultado = cursor.execute('SELECT * FROM usuarios WHERE codigoActivacion = ? and estado=?', (codigo,1)).fetchone()
  return resultado
