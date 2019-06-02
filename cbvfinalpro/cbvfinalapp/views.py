from django.shortcuts import render
from cbvfinalapp.models import Beer
from django.urls import reverse_lazy
from django.views.generic import \
    ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.

class BeerListView(ListView):
    model = Beer

class BeerDetailView(DetailView):
    model = Beer

class BeerCreateView(CreateView):
    model = Beer
    #fields = ('name','teste','color','price')
    fields = '__all__'

class BeerUpdateView(UpdateView):
    model = Beer
    fields = ('teste','color','price')

class BeerDeleteView(DeleteView):
    model = Beer
    success_url = reverse_lazy('home')




