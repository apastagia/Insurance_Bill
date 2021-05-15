from flask import Flask, config, request, url_for, redirect, render_template, jsonify
from pycaret.regression import *
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

model = load_model('deployment.pkl')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=config.DEBUG_MODE)