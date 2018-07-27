from django.shortcuts import render
from .models import listModel

def index(request):
    # Render the HTML template index.html
    return render(request, 'list/index.html')

#### list view
from django.views import generic

class infoListView(generic.ListView):
    model = listModel
    context_object_name = 'info_list'
    template_name = 'list/templates/list/listmodel_list.html'


#### adding view
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import infoAddForm

def add_info_form(request):

    form = infoAddForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            info = form.save(commit=False)
            info.save()
            return HttpResponseRedirect(reverse('list'))
   
    return render(request, 'list/add_info.html', {'form': form})
