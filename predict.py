#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input

class dogcat:
    def __init__(self,filename):
        self.filename =filename


    def predictiondogcat(self):
        # load model
        imagename = self.filename
        model = load_model('model.h5')
        img = image.load_img(imagename, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        img_data = preprocess_input(x)
        classes = model.predict(img_data)
        New_pred = np.argmax(classes, axis=1)
        if New_pred==[1]:
            prediction= "Normal"
            #return [{ "image" : prediction}]
            return ['Negative! You are all FINE. Still, take care and have a healthy life.']
        else:
          prediction= "Corona"
          #return [{ "image" : prediction}]
          return ['!!!COVID POSITIVE!!! Hope for a speedy recovery Dear, Take Care.']


