from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'index.html'

class Homepage(TemplateView):
    template_name = 'homepage.html'
