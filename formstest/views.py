from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from .models import Person


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = request.POST['your_name']
            p = Person(name=name)
            p.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    person = Person.objects.all()
    return render(request, 'formstest/home.html', {'form': form, 'data': person})


def thanks(request):
    return render(request, 'formstest/thanks.html')
