from django.shortcuts import get_object_or_404, render,redirect,HttpResponseRedirect
from django.http import HttpRequest,HttpResponse
from DiaryApp.models import diaryModel
from DiaryApp.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login

# Create your views here.

# <----------------------entries display---------------------->
def entries(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        entry = diaryModel.objects.all()
        context = {'entry':entry}
        return render(request,'entries.html',context)
# -------------------------------------------------------------


# <-------------------add entry --------------------------->
def addentry(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        entry = diaryModel.objects.all()
        form =  EntryForm()
        if request.method == 'POST':
            form = EntryForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/entries')
        context = {'entry':entry,'form':form}
        return render(request,'add.html',context)
# --------------------add entry ends------------------------>


# <----------updation starts----------------------------->
def update_entry(request,pk):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        update_entry = diaryModel.objects.get(id=pk)
        form = EntryForm(request.POST or None,instance=update_entry)
        if form.is_valid():
            form.save()
            return redirect('/entries')
        context = {'form':form,'update_entry':update_entry}
        return render(request,'update.html',context)
# <----------updation ends----------------------------->


# <----------deletion starts----------------------------->
def delete_entry(request,pk):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        delete_entry = diaryModel.objects.get(id=pk)
        if request.method == 'POST':
            delete_entry.delete()
            return redirect('/entries')
        return render(request,'delete.html')
# <----------deletion ends----------------------------->


def login(request):
    if request.method == "POST":
        username=request.POST.get('username',False)
        password=request.POST.get('password',False)
        user = authenticate(username=username, password=password)
        # print(username,password)
        if user is not None:
            auth_login(request,user)
            return redirect("/entries")
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        username=request.POST.get('username',False)
        email=request.POST.get('email',False)
        password=request.POST.get('password',False)
        created = User.objects.create_user(username=username,email=email,password=password)
        created.save()
        return redirect("/registered")
    return render(request,'signup.html')

def registered(request):
    return render(request,'registered.html')

def loggedout(request):
    logout(request)
    return render(request,'loggedout.html')