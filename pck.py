from flask import Flask, render_template, redirect, url_for, request
from urlextract import URLExtract
from googleapiclient.discovery import build

#----------------------|  ASSIGNMENT  |--------------------------------
extractor = URLExtract()
my_api_key = "AIzaSyCaugQenN9PpH5I6agQTcFlkf8hbyAEOKw"
my_cse_id = "000757437883487112859:wtcjp5mwqmu"

app = Flask(__name__, template_folder = './')


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


#---------------------------------------------------------------------

@app.route('/', methods=['GET','POST'])
def homepage():

    '''result = google_search(txt, my_api_key, my_cse_id, num=2)
    gen = list(result)

    a = []
    for url in extractor.gen_urls(str(gen[0])):
        a.append(url)

    i = 1
    for all in a:
        if a[2] == all:
            i=i+1   
#------------------------------------------------------
    print(i)	#frequency
#------------------------------------------------------

    for d in extractor.gen_urls(str(gen[0])):
#------------------------------------------------------
        print(d)	#probables
#------------------------------------------------------

    try:
#------------------------------------------------------
        print(a[2])	#link
#------------------------------------------------------
    except:
#------------------------------------------------------
        print('match not found')	#exception 
#------------------------------------------------------ 
'''

    
    return render_template('index.html')

    
if __name__ == '__main__':
    app.run()
