from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')

def view(req):
    # if req.method=='POST':
    #     name=req.POST['name']
    #     age=req.POST['age']
    #     mark=req.POST['mark']
    #     l.append({'nm':name,'ag':age,'mrk':mark})
    #     return render(req,'view.html', {'data':l})
    # else:
    #     return render(req,'view.html',{'data':l})
    return render(req,'view.html',{'data':l})
l=[]
def add(req):
    if req.method=='POST':
        ID=req.POST['ID']
        name=req.POST['name']
        age=req.POST['age']
        mark=req.POST['mark']
        l.append({'ID':ID ,'nm':name,'ag':age,'mrk':mark})
        print(l)
        return render(req,'add.html')
    
    else:
        return render(req,'add.html')

