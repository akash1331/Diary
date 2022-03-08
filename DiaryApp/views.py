from django.shortcuts import get_object_or_404, render,redirect,HttpResponseRedirect
from django.http import HttpRequest,HttpResponse
from DiaryApp.models import diaryModel
from DiaryApp.forms import *

# Create your views here.

# <----------------------entries display---------------------->
def entries(request):
    entry = diaryModel.objects.all()
    context = {'entry':entry}
    return render(request,'entries.html',context)
# -------------------------------------------------------------


# <-------------------add entry --------------------------->
def addentry(request):
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
    delete_entry = diaryModel.objects.get(id=pk)
    if request.method == 'POST':
        delete_entry.delete()
        return redirect('/entries')
    return render(request,'delete.html')
# <----------deletion ends----------------------------->