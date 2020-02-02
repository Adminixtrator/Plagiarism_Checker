import os
from flask import Flask, render_template, redirect, url_for, request
from urlextract import URLExtract
from googleapiclient.discovery import build

#----------------------|  ASSIGNMENT  |--------------------------------
extractor = URLExtract()
my_api_key = "AIzaSyCaugQenN9PpH5I6agQTcFlkf8hbyAEOKw"
my_cse_id = "000757437883487112859:wtcjp5mwqmu"

app = Flask(__name__, template_folder = './')

#---------------------------------------------------------------------

# allow specific files
ALLOWED_FILES = set(['pdf', 'docx', 'odt', 'txt'])

def allowed_files(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_FILES

#--------------------------------------------------------------------------

# allow specific images
ALLOWED_IMAGES = set(['png', 'jpg', 'jpeg'])

def allowed_images(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGES

#--------------------|  HANDLERS  |------------------------------------

def google_search(search_term, api_key, cse_id, **kwargs):
    try:
          service = build("customsearch", "v1", developerKey=api_key)
          res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
          return res['items']
    except KeyError:
        return ['No match', 'No match', 'No match']

#---------------------------------------------------------------------
#txt = input('Please enter or paste text below:\n')	#file
#---------------------------------------------------------------------
# Function to open txt
def open_txt(filename,content):
     a = open(filename,'r');c = a.read();a.close();content = c

#---------------------------------------------------------------------

# Handler for file upload -----------------------------
@app.route('/', methods=['GET','POST'])
def homepage():
    
    if request.method == 'POST':
        # check if file is present
        if 'myfile' not in request.files:
            return render_template('index.html', filename='Click to select file')
        # Store the file in the input
        myfile = request.files['myfile']
        # check if a file is selected
        if myfile.filename == '':
            return render_template('index.html', filename='No file selected')

        if myfile and allowed_files(myfile.filename):
            txt = ''
            open_txt(str(myfile),txt)
            # Handler for google search
            result = google_search(txt, my_api_key, my_cse_id, num=2)
            gen = list(result)
            # Getting things ready
            a = []
            for url in extractor.gen_urls(str(gen[0])):
                a.append(url)

            i = 1
            for all in a:
                if a[2] == all:
                    i=i+1   
            print(i)	#------------------------------------------------frequency
            for d in extractor.gen_urls(str(gen[0])):
                print(d)	#---------------------------------------------probables
            try:
                print(a[2])	#link
            except:
                print('match not found')	#exception 

    return render_template('index.html')


# Handler for text input -------------------------------------
@app.route('/txt', methods=['GET','POST'])
def texthandle():
    # check if text is available
    if request.method == 'POST':
        if 'text' not in request.files:    
            return render_template('index.html', text='It works..', homepage=homepage)
        else:
            text = request.files['text']
    return render_template('index.html')

    
if __name__ == '__main__':
    app.run()
