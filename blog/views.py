from sys import flags
from django.db.models.base import Model
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import path
from datetime import datetime

from tensorflow.python.eager.context import context
from blog.models import Contacts
from django.contrib import messages
import numpy as np 
from  tensorflow.keras.models import load_model 
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 
import pandas as pd 
scaler = MinMaxScaler()
modeldata = pd.read_csv('my-application\static\cancer_classification.csv')
X = modeldata.drop('benign_0__mal_1',axis=1)
scaler.fit(X)
  
def index(request):
    if (request.method == 'POST'):
        meanradius =  request.POST.get(' meanradius')
        meantexture =  request.POST.get('meantexture')
        meanperimeter =  request.POST.get('meanperimeter')
        meanarea =  request.POST.get('meanarea ')
        meansmoothness =  request.POST.get('meansmoothness')
        meancompactness =  request.POST.get('meancompactness')
        meanconcavity =  request.POST.get('meanconcavity')
        meanconcavepoints =  request.POST.get('meanconcavepoints')
        meansymmetry =  request.POST.get('meansymmetry')
        meanfractaldimension=  request.POST.get('meanfractaldimension')
        radiuserror = request.POST.get('radiuserror ')
        textureerror=  request.POST.get('textureerror')
        perimetererror =  request.POST.get('perimetererror')
        areaerror =  request.POST.get('areaerror')
        smoothnesserror = request.POST.get('smoothnesserror ')
        compactnesserror  =request.POST.get('compactnesserror')
        concavityerror = request.POST.get('concavityerror ')
        concavepointserror = request.POST.get('concavepointserror')
        symmetryerror =  request.POST.get('symmetryerror')
        fractaldimensionerror =  request.POST.get('fractaldimensionerror')
        worstradius =  request.POST.get('worstradius')
        worsttexture =  request.POST.get('worsttexture')
        worstperimeter =  request.POST.get('worstperimeter')
        worstarea =  request.POST.get('worstarea')
        worstsmoothness =  request.POST.get('worstsmoothness')
        worstcompactness =  request.POST.get('worstcompactness')
        worstconcavity =  request.POST.get('worstconcavity ')
        worstconcavepoints =  request.POST.get('worstconcavepoints')
        worstsymmetry =  request.POST.get('worstsymmetry')
        worstfractaldimension =  request.POST.get('worstfractaldimension')
        
        data= np.array([meanradius, meantexture, meanperimeter, meanarea,
        meansmoothness, meancompactness, meanconcavity,
        meanconcavepoints, meansymmetry, meanfractaldimension,
        radiuserror, textureerror, perimetererror, areaerror,
        smoothnesserror, compactnesserror, concavityerror,
        concavepointserror, symmetryerror, fractaldimensionerror,
        worstradius, worsttexture, worstperimeter, worstarea,
        worstsmoothness, worstcompactness, worstconcavity,
        worstconcavepoints, worstsymmetry, worstfractaldimension])
        
        data = np.ndarray(shape=(1,30),dtype=float)
        
        scaler.transform(data)
        
        model = load_model('my-application\static\breastcancerprediction.h5')
        
        if model.predict_classes(data) == 1:
            cancerval = 'malignant '
        else :
            cancerval = 'benign'
            
        context ={
            'test' : cancerval,
        }
        return render(request,'prediction.html',context)
        
        
    return render(request,'index.html')
                
def Contact(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        email=request.POST.get('email')
        subject = request.POST.get('desc')
        contacts = Contacts(Name=name,Email=email,Des=subject,Date = datetime.today())
        print(request.POST.items())
        contacts.save()
        messages.success(request,"Your message was sent ")
        
    return render(request,'contact.html')
def mainpage(request):
    return render(request,'mainpage.html')

# Create your views here.




