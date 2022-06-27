import json
import time
#from selenium import webdriver
from flask import Flask, jsonify, redirect, render_template, request
# from sebin.Tensorflow.api import playlist
# from sebin.Tensorflow.emotions import mood
import subprocess    #method1
                    #using subprocess module to run commands to system
                    #ALternative to os.system(), 
                    #subprocess is high level shit, so handle with care

from test import the_useless_fn #method2 importing the function and 
                                #calling it form inside this fi

#from sebin.Tensorflow.api import mood
# try:
#     from emotions import mood
# except:
#     from sebin.Tensorflow.emotions import mood                              

# driver = webdriver.Chrome()
# driver.get('http://youtube.com')


app = Flask(__name__)

@app.route('/')
def index():
  with open('MyRecords.json', 'r+') as f:
    data = json.load(f)
    data['mood'] = '' # <--- add id value.
    data['play'] = ''
    f.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data, f, indent=4)
    f.truncate() 
  return render_template('index.html')    #make sure the index file is inside templates folder in same directory

@app.route('/my-link/')
def my_link():
#   print ('I got clicked!')
# add your own shits
  # render_template('dummy.html')  #dont remove this, I've tried .... lol :)
  # subprocess.Popen(['python', r'sebin\Tensorflow\emotions.py'])  #method 1
  subprocess.Popen(['python', r'sebin\Tensorflow\api.py'])
  # the_useless_fn() ## method 2, be wary of params, if any
  
  return render_template('page2.html')  #dont remove this, I've tried .... lol :)


@app.route("/api/geo_code")

  
def geo_code():
  
  with open('MyRecords.json', 'r+') as f:
    data = json.load(f)
  md={
    'mood' : data['mood'],
    'play' : data['play']
  }
  
  return jsonify(md)
  #return render_template('page2.html')

# time.sleep(20)
# driver.refresh()



if __name__ == '__main__':
  app.run()
