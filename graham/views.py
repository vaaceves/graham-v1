from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'


def error_404(request):
    return render(request, 'error_404.html', {})
