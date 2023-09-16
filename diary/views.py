
from django.shortcuts import render,redirect
from .models import *
from .forms import EntryForm

def index(request):
    entries = Diary.objects.filter(user=request.user)
    context = {'entries' : entries}
    return render(request, 'diary/index.html',context)

def add(request):
    if request.method == 'POST':
        note = request.POST.get('comment')
        print(note)
        obj = Diary(user=request.user,context=note)
        obj.save()
        return redirect('diary_home')
    return render(request, 'diary/add.html')
