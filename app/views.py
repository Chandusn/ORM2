from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def Insert_Topic(request):
    tn=input('enter Topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic_name is inserted')

def Insert_webpage(request):
    tn=input('enter Topic name: ')
    n=input('enter name: ')
    u=input('enter URL: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('Webpage data in inserted')

def Insert_accessrecord(request):
    tn=input('enter Topic name: ')
    n=input('enter name: ')
    u=input('enter URL: ')
    a=input('enter author name: ')
    d=input('enter date: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    AR=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    AR.save()
    return HttpResponse('AccessRecords are inserted')
