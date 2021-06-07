from flask import Flask, request
import os
import json
import pymongo

app = Flask(__name__)

@app.route("/")
def main():
    return "<form action=\"\" method=\"get\"><p>Nombre: <input type=\"text\" name=\"nombre\" size=\"40\"></p><p>Año de nacimiento: <input type=\"number\" name=\"nacido\" min=\"1900\"></p><p>Sexo:<input type=\"radio\" name=\"hm\" value=\"h\"> Hombre<input type=\"radio\" name=\"hm\" value=\"m\"> Mujer</p><p><input type=\"submit\" value=\"Enviar\"><input type=\"reset\" value=\"Borrar\"></p></form>"