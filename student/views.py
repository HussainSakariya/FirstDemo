from django.shortcuts import render
from .models import student 
from .forms import student_form

# Create your views here.
def index(request):
    context={}
    context['obj']=student.objects.all()
    return render(request,"index.html",context)

def second(request):
    if request.method=="POST":
        no=request.POST['no']
        name=request.POST['name']
        age=request.POST['age']

        if student.objects.filter(no=no).exists():
            return render(request,"index.html",{'name':"ERROR"})
        else:    
            obj1=student(no=no,name=name,age=age)
            obj1.save()

        return render(request,"second.html")
    else:
        return render(request,"second.html")

def dynamic_form(request):
    if request.method=="POST":
        frm=student_form(request.POST)
        if frm.is_valid():
            frm.save()
            return render(request,'second.html')
    else:
        frm=student_form()
        return render(request,'dynamic_form.html',{"frm":frm})