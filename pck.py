from flask import Flask, render_template, redirect, url_for, requests
from urlextract import URLExtract

extractor = URLExtractor

app = Flask(__name__, template_folder = './')
@app.route('/', methods=['GET','POST'])
def homepage():
    return render_template('index.html')
