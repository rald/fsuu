from django.shortcuts import render

from django.views.generic import TemplateView

def index(request):
  return render(request, 'fsuu/index.html', None)

def base(request):
  return render(request, 'fsuu/base.html', None)

def Fpage(request):
  return render(request, 'fsuu/Fpage.html', None)

class Cpage(TemplateView):
  template_name = 'fsuu/Cpage.html'
