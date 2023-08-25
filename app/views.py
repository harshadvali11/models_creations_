from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topics(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpages.html',d)


def display_access(request):
    QSAO=AccessRecord.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_access.html',d)


def insert_topic(request):
    topic_name=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
    TO.save()
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)



def insert_webpage(request):
    tn=input('enter topic_name')
    na=input('enter name')
    ur=input('enter url')

    TO=Topic.objects.get(topic_name=tn)

    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    WO.save()

    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpages.html',d)
































