from flask import Flask, render_template
import subprocess    #method1
                    #using subprocess module to run commands to system
                    #ALternative to os.system(), 
                    #subprocess is high level shit, so handle with care

from test import the_useless_fn #method2 importing the function and 
                                #calling it form inside this file

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')    #make sure the index file is inside templates folder in same directory

@app.route('/my-link/')
def my_link():
#   print ('I got clicked!')
# add your own shits
  subprocess.Popen(['python', r'C:\Users\tonyk\Desktop\MoodProII\sebin\Tensorflow\emotions.py'])  #method 1

  # the_useless_fn() ## method 2, be wary of params, if any

  return 'Camera is starting...'  #dont remove this, I've tried .... lol :)

if __name__ == '__main__':
  app.run()