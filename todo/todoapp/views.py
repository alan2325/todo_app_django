from django.shortcuts import render,redirect

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

def edit(req,std):
    std1={}
    pos=0
    for i in l:
        if i['ID']==std:
            std1=i
            pos=l.index(i)
    if req.method=="POST":
        name=req.POST['name']
        age=req.POST['age']
        mark=req.POST['mark']
        l[pos]={'nm':name , 'ag':age , 'mrk':mark}
        return redirect(view)
    else:   
         return render(req,'edit.html',{'data':std1})     

def delete(req,ID):
    for i in l:
        if i['ID']==ID:
            l.remove(i)
            return redirect(view)
    return render