from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length

def display_topics(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSWO=Webpage.objects.all()

    QSWO=Webpage.objects.filter(pk=3)
    QSWO=Webpage.objects.filter(topic_name='Cricket')
    QSWO=Webpage.objects.exclude(topic_name='Cricket')
    
    QSWO=Webpage.objects.all()[2:5:1]
    
    QSWO=Webpage.objects.all()[5:6:]
    
    QSWO=Webpage.objects.all().order_by('name')
    QSWO=Webpage.objects.filter(topic_name='Cricket').order_by('name')
    QSWO=Webpage.objects.all().order_by('-name')
    QSWO=Webpage.objects.all().order_by(Length('name'))

    QSWO=Webpage.objects.all().order_by(Length('name').desc())
    QSWO=Webpage.objects.filter(name__startswith='v')

    QSWO=Webpage.objects.all()
    QSWO=Webpage.objects.filter(url__endswith='in')
    QSWO=Webpage.objects.filter(url__contains='R')
    QSWO=Webpage.objects.exclude(url__contains='R')
















    d={'QSWO':QSWO}
    return render(request,'display_webpages.html',d)


def display_access(request):
    QSAO=AccessRecord.objects.all()
    QSAO=AccessRecord.objects.filter(date='2022-10-10')
    QSAO=AccessRecord.objects.filter(date__gte='2022-10-10')
    QSAO=AccessRecord.objects.filter(date__lte='2022-10-10')
    QSAO=AccessRecord.objects.filter(date__year='1999')
    QSAO=AccessRecord.objects.filter(date__month='7')
    QSAO=AccessRecord.objects.filter(date__day='10')
    QSAO=AccessRecord.objects.filter(author__in=('di','VK'))
    QSAO=AccessRecord.objects.filter(author__regex='^V\w+')
    QSAO=AccessRecord.objects.filter(date__year__lt='1999')
    
    
    
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
































