from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from everycheese.cheeses.models import Cheese
from django.contrib.auth.mixins import LoginRequiredMixin


class CheeseDetailView(DetailView):
    model = Cheese


class CheesesListView(ListView):
    model = Cheese


class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese
    fields = ['name', 'description', 'firmness', 'country_of_origin']

