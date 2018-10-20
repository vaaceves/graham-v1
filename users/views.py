from django.contrib.auth.models import User
from django.db import transaction

from .models import *

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate, update_session_auth_hash, login
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import *

from django.views.generic import View, DetailView, CreateView, ListView, UpdateView, TemplateView

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# CLASS BASED VIEWS
# LOGIN
class LoginUserView(View):
    login_form = LoginUserForm()
    login_error_message = None
    template = 'home.html'

    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated():
        #     return redirect('users:dashboard')
        return render(request, self.template, self.get_context())

    def post(self, request, *args, **kwargs):
        username_post = request.POST['username']
        password_post = request.POST['password']
        user = authenticate(username=username_post, password=password_post)
        if user is not None:
            login_django(request, user)
            return redirect('dashboard')
        else:
            self.login_error_message = "Username or Password invalid"
        return render(request, self.template, self.get_context())

    def get_context(self):
        return {
            'login_form': self.login_form,
        }


# DASHBOARD
class DashboardUserView(LoginRequiredMixin, View):
    login_url = 'home'
    section_name = 'Dashboard'
    context_dic = {
        'section_name': section_name
    }

    def get(self, request, *args, **kwargs):
        return render(request, 'users/dashboard.html', self.context_dic)


# CREATE USER
class CreateUserView(LoginRequiredMixin, CreateView):
    # success_url = reverse_lazy('clients:projects_list')
    login_url = 'home'
    template_name = 'users/create-user.html'
    model = User
    form_class = CreateUserForm
    section_name = 'Crear Nuevo Usuario'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('dashboard')

    def get_context(self):
        return {
            'section_name': self.section_name,
            'form': self.form_class,
        }

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['section_name'] = 'Crear Nuevo Usuario'
        data['page_title'] = 'Crear Nuevo Usuario'
        return data


# FUNCTION BASED VIEWS
# LOGOUT
@login_required(login_url='home')
def logout(request):
    logout_django(request)
    return redirect('home')



