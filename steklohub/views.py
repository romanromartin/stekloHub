from django.shortcuts import render
from .models import Peregorodki, Kozirki, Nerjograda, Stekloograda, Interer
import os



def index(request):
    loop = loop_list[0]
    per = Peregorodki.objects.all()
    koz = Kozirki.objects.all()
    ner = Nerjograda.objects.all()
    stek = Stekloograda.objects.all()
    inter = Interer.objects.all()
    if request.method == 'POST':
        if request.POST.get("1"):
            loop = loop_list[0]
        elif request.POST.get("2"):
            loop = loop_list[1]
        elif request.POST.get("3"):
            loop = loop_list[2]
        elif request.POST.get("4"):
            loop = loop_list[3]
    print(loop)





    return render(request, 'index.html',
                  context={'per': per, 'koz': koz, 'ner': ner, 'stek': stek, 'inter': inter})



def managment(request):
    if request.method == 'POST':
        if request.POST.get("peregor"):
            Peregorodki.objects.all().delete()
            for file in os.listdir('static/media/peregorodki'):
                port = Peregorodki(picture='static/media/peregorodki/'+file)
                port.save()
        elif request.POST.get("kozirki"):
            Kozirki.objects.all().delete()
            for file in os.listdir('static/media/kozirki'):
                port = Kozirki(picture='static/media/kozirki/'+file)
                port.save()
        elif request.POST.get("Nerjograda"):
            Nerjograda.objects.all().delete()
            for file in os.listdir('static/media/nerjograda'):
                port = Nerjograda(picture='static/media/nerjograda/'+file)
                port.save()
        elif request.POST.get("Stekloograda"):
            Stekloograda.objects.all().delete()
            for file in os.listdir('static/media/stekloograda'):
                port = Stekloograda(picture='static/media/stekloograda/'+file)
                port.save()
        elif request.POST.get("interer"):
            Interer.objects.all().delete()
            for file in os.listdir('static/media/interer'):
                port = Interer(picture='static/media/interer/'+file)
                port.save()

    return render(request, 'managment.html')



loop_list =[[1, ], [2,], [3,], [4,]   ]