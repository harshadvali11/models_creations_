from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
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
    QSWO=Webpage.objects.filter(Q(topic_name='Cricket') & Q(url__endswith='in'))

    QSWO=Webpage.objects.all()
    QSWO=Webpage.objects.filter(Q(name__contains='r') & Q(url__endswith='com'))

    QSWO=Webpage.objects.filter(Q(topic_name='Cricket') | Q(name__contains='r'))














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






def update_webpage(request):
    
    #Webpage.objects.filter(topic_name='Foot Ball').update(name='Ronaldo')
    #Webpage.objects.filter(name='virat').update(url='https://kohli.com')
    #Webpage.objects.filter(name='Python').update(url='https://kohli.com')
    #Webpage.objects.filter(name='virat').update(topic_name='Chess')
    #Webpage.objects.filter(name='virat').update(topic_name='Boxing')
    
    #Webpage.objects.update_or_create(topic_name='Foot Ball',defaults={'name':'NeyMar'})
    #Webpage.objects.update_or_create(topic_name='Volley Ball',defaults={'name':'NeyMar'})
    
    #RO=Topic.objects.get(topic_name='Rugby')
    #Webpage.objects.update_or_create(name='dileep',defaults={'topic_name':RO})
    
    #Webpage.objects.update_or_create(name='Hardhik',defaults={'url':'https://Hardhik.com'})
    CTO=Topic.objects.get(topic_name='Cricket')
    Webpage.objects.update_or_create(name='Hardhik',defaults={'topic_name':CTO,'url':'https://Hardhik.com'})
    
    QSWO=Webpage.objects.all()

    d={'QSWO':QSWO}

    return render(request,'display_webpages.html',d)





























