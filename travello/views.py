from django.shortcuts import render
from .models import Destination


def index(request):
    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.price= 800
    dest1.img = 'destination_1.jpg'
    dest1.offers= False
    dest2 = Destination()
    dest2.name = "Kochi"
    dest2.price= 100
    dest2.offers=True
    dest2.img = 'destination_2.jpg'
    dest3 = Destination()
    dest3.name = "Qln"
    dest3.price=  750
    dest3.offers=False
    dest3.img = 'destination_3.jpg'
    dests=[dest1 , dest2 , dest3]
    return render(request , 'index.htm',{'dests' :dests })


