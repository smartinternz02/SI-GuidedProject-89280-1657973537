from __future__ import division, print_function

import os
import numpy as np

import cv2
from keras.models import load_model
from keras import utils

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)


print('Model loaded. Check http://127.0.0.1:5000/home')

def model_predict(img_path):
        model=load_model('Food.h5')
        img = utils.load_img(img_path, target_size=(64 ,64))
        x = utils.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        preds=np.argmax(model.predict(x), axis=1)
        if(preds==0):
            a="https://www.thespruceeats.com/thmb/QUyxKfZoo6rHgczWZieyQBAKviw=/1333x1000/smart/filters:no_upscale()/how-to-make-french-fries-995932_final-6a36c7cf85604fa9b15fc868a7bcc6c8.png";
    
        elif(preds==1):
            a="https://files.liveworksheets.com/def_files/2020/10/3/1003050249676828/1003050249676828001.jpg";
        else:
            a="https://i.pinimg.com/736x/8d/ce/56/8dce569d41b2d6dfb88c48dd698c195e.jpg";
        return a
            
   
        

@app.route('/home', methods=['GET'])
def index():
    # Main page
    return render_template('home.html')
@app.route('/prediction', methods=['GET'])
def index2():
    # Main page
    return render_template('launch.html')
@app.route('/predict', methods=['GET', 'POST'])
def upload():
    print("hi")
    if request.method == 'POST':
        f = request.files['fileq']
       

      
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        result=model_predict(file_path)
    
    return render_template('launchr.html',user_image=result)
    return None


if __name__ == '__main__':
    app.run(debug=True)
    