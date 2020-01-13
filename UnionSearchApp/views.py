from django.shortcuts import render,HttpResponse
from UnionSearchApp import models

# Create your views here.
def index(request):
    return render(request,'index.html')

def video(request,*args,**kwargs):
    # print(kwargs)
    condition={}
    for k,v in kwargs.items():
        tmp=int(v)
        kwargs[k]=tmp
        if tmp:
            condition[k]=tmp
            # print(tmp,condition)


    video=models.Video.objects.filter(**condition)
    # print(video)
    direaction=models.Direaction.objects.all()
    classfication=models.Classfication.objects.all()
    level=models.Level.objects.all()
    context={'video':video,
             'classfication':classfication,
             'level':level,
             'direaction':direaction,
             'kwargs':kwargs}

    return render(request, 'video.html', context)
