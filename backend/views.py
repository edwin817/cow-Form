from django.shortcuts import render,redirect
from django.http import HttpResponse
from backend.models import fadb,apdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.
def intropage(request):
    return render(request,"intro.html")

def addpage(request):
    return  render(request,"addcategory.html")

def saveadd(request):
    if request.method=="POST":
        na=request.POST.get('name')
        desc=request.POST.get('description')
        img=request.FILES['image']
        obj=fadb(name=na,description=desc,image=img)
        obj.save()
        messages.success(request, "Congratulations..! your Category added successfull..!")
        return redirect(addpage)

def display(request):
    data= fadb.objects.all()
    return render(request, "displaycategory.html", {"data": data})


def editcategory(request,dataid):
    data= fadb.objects.get(id=dataid)
    print(data)
    return render(request,"Editcategory.html",{"data":data})

def updatecategory(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        desc = request.POST.get('description')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=fadb.objects.get(id=dataid).image
        fadb.objects.filter(id=dataid).update(name=na,description=desc)
        return redirect(display)

def deletecategory(request,dataid):
    data=fadb.objects.filter(id=dataid)
    data.delete()
    return redirect(display)

def addproduct(request):
    data= fadb.objects.all()
    return render(request,"add product.html",{"data":data})

def saveproduct(request):
    if request.method=="POST":
        na=request.POST.get('name')
        ca = request.POST.get('category')
        pr=request.POST.get('price')
        qnty=request.POST.get('qunty')
        desc=request.POST.get('description')
        img=request.FILES['image']
        obj = apdb(Name=na, Category=ca, Price=pr, Qnty=qnty, Description=desc, Image=img)
        obj.save()
        messages.success(request, "Congratulations..! Your Product added Successfully..!")
        return redirect(addproduct)

def displayproduct(request):
    data = apdb.objects.all()
    return render(request,"display product.html",{"data":data})

def editproduct(request,dataid):
    data=apdb.objects.get(id=dataid)
    print(data)
    return render(request,"Editproduct.html",{"data":data})

def updateproduct(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        ca = request.POST.get('category')
        pr = request.POST.get('price')
        qnty = request.POST.get('quantity')
        desc = request.POST.get('description')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=apdb.objects.get(id=dataid).Image
        apdb.objects.filter(id=dataid).update(Name=na,Category=ca,Price=pr,Qnty=qnty,Image=file,Description=desc)
        return redirect(displayproduct)

def deleteproduct(request,dataid):
    data=apdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)


def loginpage(request):
    return render(request,"Login.html")

def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r

                return redirect(intropage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)


def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)

def cart2pg(request):
    cart = cartdb.objects.all()
    return render(request,"cdel.html",{"cart":cart})














