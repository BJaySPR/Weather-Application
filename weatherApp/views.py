from django.shortcuts import render
import requests
import json
from django.contrib import messages
# Create your views here.
# apikey = bf22686cf11682e29d657b984d138978
def index(request):    
    if request.method=="POST":
        city = request.POST['city']
    else:
        city='kathmandu'

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf22686cf11682e29d657b984d138978'
    PARAMS = {'units':'metric'}
    try:
        data =requests.get(url,PARAMS).json()
        tem = data["main"]["temp"]   #temperature in celsius
        humidity = data['main']['humidity']
        wind = data['wind']['speed']  
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        return render(request, 'index.html',{'temp':tem,'city':city,'humidity':humidity,'wind':wind,'description':description,'icon':icon})

    except:
        messages.error(request,"City not found")        
    return render(request, 'index.html',{'temp':25,'city':'kathmandu'})

   

