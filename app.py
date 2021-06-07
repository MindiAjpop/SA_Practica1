from flask import Flask, request
import os
import json
import pymongo

app = Flask(__name__)

@app.route("/")
def main():
    return ""
