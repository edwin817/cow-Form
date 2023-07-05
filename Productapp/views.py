from django.shortcuts import render,redirect
from django.http import HttpResponse
from backend.models import fadb,apdb
from Productapp.models import userdb
from Productapp.models import cartdb,userdb,paymentdetaildb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.db.models import Sum

# Create your views here.
def homepage(request):
    data = fadb.objects.all()
    return render(request,"home.html",{'data':data})

def aboutpage(request):
    data = fadb.objects.all()
    return render(request,"about.html",{'data':data})

def servicepage(request):
    data = fadb.objects.all()
    return render(request,"services.html",{'data':data})

def productpage(request,iteamcatg):
    data = fadb.objects.all()
    products = apdb.objects.filter(Category=iteamcatg)
    return render(request,"product.html",{"products":products,"data":data})

def singleproductpg(request,dataid):
    data = fadb.objects.all()
    product = apdb.objects.get(id=dataid)
    return render(request,"singleproduct.html",{"product":product,'data':data})

def cartpg(request):
    # data = fadb.objects.all()
    cart = cartdb.objects.all()
    cart_empty = cartdb.objects.all()
    grand_total=cart.aggregate(Sum("totalprice"))["totalprice__sum"]
    return render(request,"cart.html",{'cart':cart,"grand_total":grand_total,"cart_empty":cart_empty})

def savecart(request):
    if request.method=="POST":
        pn=request.POST.get('productname')
        pq=request.POST.get('productqut')
        un=request.POST.get('user')
        pid = request.POST.get('productid')
        data= apdb.objects.get(id=pid)
        img=data.Image
        tp=request.POST.get('totalprice')
        pp=request.POST.get('productprice')
        obj=cartdb(productname=pn,productqut=pq,totalprice=tp,user=un,productprice=pp,image=img)
        obj.save()
        return redirect(cartpg)

def Deletecart(request,dataid):
    data=cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cartpg)

def checkoutpg(request):
    cart = cartdb.objects.all()
    data = fadb.objects.all()
    grand_total = cart.aggregate(Sum("totalprice"))["totalprice__sum"]
    return render(request,"checkout.html",{'cart':cart,"grand_total":grand_total,'data':data})

def savecheckout(request):
    if request.method=="POST":
        fn =request.POST.get('fullname')
        em = request.POST.get('emaill')
        pn = request.POST.get('phonenumber')
        cty =request.POST.get('city')
        ste =request.POST.get('state')
        pE = request.POST.get('productname')
        pp = request.POST.get('productprice')
        pt = request.POST.get('total')
        obj=paymentdetaildb(fullname=fn,emaill=em,phonenumber=pn,city=cty,state=ste,productname=pE,productprice=pp,total=pt)
        obj.save()
        return redirect(homepage)


def userloginpg(request):
    return render(request,"userlogin.html")

def usersavedata(request):
    if request.method=="POST":
        user_r=request.POST.get('usernamel')
        gmail_r = request.POST.get('email')
        password_r=request.POST.get('passwordl')
        c_password=request.POST.get('conformpasswordl')
        obj=userdb(username=user_r,email=gmail_r,password=password_r,confirmpassword=c_password)
        obj.save()
        messages.success(request, "Congratulations..! Account Create Successfully..!")
        return redirect(userloginpg)

def userpg(request):
    if request.method == "POST":
        username_R = request.POST.get('usernamel')
        password_R = request.POST.get('passwordl')
        if userdb.objects.filter(username=username_R, password=password_R).exists():
            data = userdb.objects.filter(username=username_R, password=password_R).values('email', 'id').first()
            request.session['username'] = username_R
            request.session['password'] = password_R
            return redirect(homepage)
        else:
            return redirect(userloginpg)
    else:
        return redirect(userloginpg)

def userlogout(request):
    if request.session:
        request.session.clear()
    return redirect(userloginpg)

def contactpg(request):
    data = fadb.objects.all()
    return render(request,"contact.html",{'data':data})

