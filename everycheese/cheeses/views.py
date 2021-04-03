from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from everycheese.cheeses.models import Cheese


class CheeseDetailView(DetailView):
    model = Cheese


class CheesesListView(ListView):
    model = Cheese


class CheeseCreateView(CreateView):
    model = Cheese
    fields = ['name', 'description', 'firmness', 'country_of_origin']

