from django.http import HttpResponseRedirect
from django.shortcuts import render
from bd_calendar.models import ImportantDate
from .email import send_test_email

from .forms import DateForm
# Create your views here.

def index(request):
    template = 'index.html'
    form = DateForm()
    if request.method == "POST":
        form = DateForm(request.POST)
        if form.is_valid():
            new_date = ImportantDate(**form.cleaned_data)
            new_date.save()
            send_test_email()
            return HttpResponseRedirect('index')
            # return render(request, template, {'form': form})
        else:
            return render(request, template, {'form': form})
    else:
        context = {
            'dates': ImportantDate.objects.all().order_by('event_date')
        }
        return render(request, template, {'form': form, **context})
