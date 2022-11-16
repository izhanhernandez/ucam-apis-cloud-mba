#!/usr/bin/env python

# ================================================================================================================================================ #
# SYSTEM CONFIGURATION
# ================================================================================================================================================ #

# -*- coding: utf-8 -*-

# ================================================================================================================================================ #
# IMPORTS
# ================================================================================================================================================ #

import os
import flask
import platform
import ServicioCalculadora as calculadora

# ================================================================================================================================================ #
# CONSTANTS
# ================================================================================================================================================ #

# Local filesystem
opSys = "mac" if "mac" in platform.platform().lower() else "linux"
if "windows" in platform.platform().lower(): opSys = "windows"
pathSep = "\\" if opSys == "windows" else "/"
currentFolder = os.path.dirname(os.path.abspath(__file__)) + pathSep

# ================================================================================================================================================ #
# MAIN FUNCTION
# ================================================================================================================================================ #

# Flask App Runner
def runCalculadoraApp():
    app.run(host = "0.0.0.0", port = 5000)

# ================================================================================================================================================ #
# FLASK ENDPOINTS
# ================================================================================================================================================ #

# Define the Flask app
app = flask.Flask("calculadora")

# Welcome page 
@app.route("/")
def welcome():
    return flask.Response(open(f"{currentFolder}ApiHtmlCalculadora.html").read(), status = 200, mimetype = "text/html")
    
# Execute an addition 
@app.route("/suma")
def suma():
    try:
        # Read the params
        passedArguments = dict(flask.request.args)
        # Execute the operation
        result = calculadora.servicioCalculadora("suma", passedArguments['variable1'], passedArguments['variable2'])
        # Return the data
        return flask.Response(str(result), status = 200, mimetype = "text/plain")
    except: return flask.Response("error", status = 400, mimetype = "text/plain")
    
# Execute an substract 
@app.route("/resta")
def resta():
    try:
        # Read the params
        passedArguments = dict(flask.request.args)
        # Execute the operation
        result = calculadora.servicioCalculadora("resta", passedArguments['variable1'], passedArguments['variable2'])
        # Return the data
        return flask.Response(str(result), status = 200, mimetype = "text/plain")
    except: return flask.Response("error", status = 400, mimetype = "text/plain")
    
# Execute a multiplication
@app.route("/multiplicacion")
def multiplicacion():
    try:
        # Read the params
        passedArguments = dict(flask.request.args)
        # Execute the operation
        result = calculadora.servicioCalculadora("multiplicacion", passedArguments['variable1'], passedArguments['variable2'])
        # Return the data
        return flask.Response(str(result), status = 200, mimetype = "text/plain")
    except: return flask.Response("error", status = 400, mimetype = "text/plain")

if __name__ == '__main__':
    runCalculadoraApp()

# ================================================================================================================================================ #
# END OF FILE
# ================================================================================================================================================ #