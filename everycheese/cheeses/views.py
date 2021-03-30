from django.shortcuts import render
from django.views.generic import ListView
from everycheese.cheeses.models import Cheese


class CheesesListView(ListView):
    model = Cheese
