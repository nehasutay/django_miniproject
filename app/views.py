from django.shortcuts import render, redirect
from app.form import createuserform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from app.form import memberform
from app.models import userdetail 
from app.models import loanapply,transaction,transactionhistory
from app.form import loanform
from app.form import transform, histform



# Create your views here.
def home(request):
    return render(request,"home.html")

def apply(request):
    form=loanform(request.POST)
    # obj=loanapply.objects.filter(member__username=request.user).values()
    # # print(obj1)
    if(request.method=='POST'):
        if(form.is_valid()):
            Instant=form.save(commit=False)
            Instant.member=request.user
            Instant.save()
    return render(request,"apply.html",{'forms':form})

def loan(request):
    return render(request,"loan.html")
 

def aboutus(request):
    return render(request,"aboutus.html")

def profile(request):
    detail=userdetail.objects.filter(owner__username=request.user).values()
    #print(detail)
    return render(request,"profile.html",{'detail':detail})


def seeprofile(request):
    detail=userdetail.objects.filter(owner__username=request.user).values()
    return render(request,"seeprofile.html",{'detail':detail})

def seedetails(request):
    ldetail=loanapply.objects.filter(member__username=request.user).values()
    return render(request,"seedetails.html",{'ldetail':ldetail})

def transactionmain(request):
    hdetail=transactionhistory.objects.filter(owner__username=request.user).values()
    return render(request,"transactionmain.html",{'hdetail':hdetail})

def admin1(request):
	return render(request,"adminlogin.html")

def member(request):
    if(request.user.is_authenticated):
        return redirect('/home')
   


    elif request.method == "POST":

        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request, username=username, password=password)
        print(user)
        if(user is not None):
            login(request,user)
            return redirect('/home')
        else:
            return redirect('/')
         
    return render(request,"memberlogin.html")

def logoutuser(request):
    logout(request)
    return redirect('/')

# def register(request):
#     form=createuserform(request.POST)
#     if(request.method=="POST"):
#         if(form.is_valid()):
#             form.save()
#     return render(request,"register.html",{'forms':form})

def formupload(request):
    form=memberform(request.POST)
    if(request.method=='POST'):
        if(form.is_valid()):
            Instant=form.save(commit=False)
            Instant.owner=request.user
            Instant.save()
    return render(request,"userdetail.html",{'forms':form})

# def emi(request):
#     form=emiform(request.POST)
#     if(request.method=='POST'):
#         if(form.is_valid()):
#             Instant=form.save(commit=False)
#             Instant.member=request.user
#             Instant.save()
#     return render(request,"emi.html",{'forms':form})

def trans(request):
    form=transform(request.POST)
    # obj=transaction.objects.filter().values()
    # print(obj)
    if(request.method=='POST'):
        if(form.is_valid()):
            Instant=form.save(commit=False)
            Instant.owner=request.user
            Instant.save()
    return render(request,"transaction.html",{'forms':form})

def transdis(request):
    obj=transaction.objects.filter(owner__username=request.user).values()
    obj5=loanapply.objects.filter(member__username=request.user).values()
    # print(obj)
    # if(obj) :
    #     print("none")
    print(obj[0]['id'])
    balance=obj[0]['principal'] - obj[0]['paid']
    transaction.objects.filter(owner__username=request.user).update(remaining=balance)
    A=transaction.objects.filter(owner__username=request.user).values()

    # print(obj4)
    return render(request,"transaction.html",{'obj':A,'obj5':obj5})

def status(request):
    obj=transaction.objects.filter(owner__username=request.user).values()
    obj2=loanapply.objects.filter(member__username=request.user).values()
    return render(request,"status.html", {'a':zip(obj,obj2)})

