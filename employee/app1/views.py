from django.shortcuts import render
from .models import Employee

# Create your views here.

def home(request):
    k = Employee.objects.all()
    return render(request, 'home.html', {'employee':k})


def add(request):
    if (request.method == "POST"):
        i=request.POST['i']
        n=request.POST['n']
        a=request.POST['a']
        ad=request.POST['ad']
        e=request.POST['e']
        im=request.FILES['im']

        m =Employee.objects.create(empid=i,ename=n, age=a,address=ad,email=e,image=im)
        m.save()
        return home(request)
    return render(request,'add.html')
def viewdetail(request,i):
    k=Employee.objects.get(id=i)
    return render(request, 'detail.html', {'employee':k})

def edit(request,i):
    k =Employee.objects.get(id=i)
    if (request.method == "POST"):
        k.empid= request.POST['i']
        k.ename= request.POST['n']
        k.age= request.POST['a']
        k.address= request.POST['ad']
        k.email=request.POST['e']
        if request.FILES.get('im')==None:
            k.save()
        else:
            k.image = request.FILES['im']
        k.save()
        return home(request)

    return render(request, 'edit.html', {'employee':k})

def delete(request,i):
    k =Employee.objects.get(id=i)
    k.delete()
    return home(request)