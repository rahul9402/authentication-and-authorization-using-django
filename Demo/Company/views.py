from django.shortcuts import render,HttpResponse,redirect
from .models import register
# Create your views here.

def registerpage(request):
    if request.method == 'POST': #access
        getname = request.POST.get("name")
        getaddress = request.POST.get("address")
        getusername = request.POST.get("username")
        getpassword = request.POST.get("password")
        users = register()
        users.Name = getname
        users.Address = getaddress
        users.Username = getusername
        users.Password = getpassword
        users.save()

    return render(request,'registerpage.html')

def userlogin(request):
    if request.method == 'POST':
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        try:
            register.objects.get(Username = getusername , Password = getpassword)
            return HttpResponse('Welcome User')
        except:
            return HttpResponse('Invalid User')

    return render(request,'userlogin.html')

def adminlogin(request):
    if request.method == 'POST':
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        if getusername == 'admin' and getpassword == 'admin':
            return redirect('/adminhome')
        else:
            return HttpResponse('Invalid')
    return render(request,'adminlogin.html')

def adminhome(request):
    return render(request,'adminhome.html')

def pending(request):
    details = register.objects.filter(Status = False)
    return render(request,'pendinglist.html',{'value':details})


def approve(request,id):
    data = register.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/pending')

def approved(request):
    details = register.objects.filter(Status = True)
    return render(request,'approvedlist.html',{'value':details})



