from flask import Flask, render_template, redirect, url_for
from urlextract import URLExtract

extractor = URLExtract()

app = Flask(__name__, template_folder = './')
@app.route('/', methods=['GET','POST'])
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
