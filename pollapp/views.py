from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

arr=['Java','Python','Cplusplus','C','DotNet','Javascript','PHP','Swift'
    'SQL','Ruby','Delphi','Objective-C','Go','Assemblylanguage','VisualBasic','D','R','Perl','MATLAB']
globalcnt=dict()

# Create your views here.
def index(request):
    mydict={
        "arr":arr
    }
    return render(request,'index.html',context=mydict)

def getquery(request):
    q=request.GET['languages']
    if q in globalcnt:
        globalcnt[q]=globalcnt[q]+1
    else:
        globalcnt[q]=1
    mydict={
        "arr":arr,
        "globalcnt":globalcnt
    }
    return render(request,'index.html',context=mydict)
