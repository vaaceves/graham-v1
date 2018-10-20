"""graham URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import Home, error_404
from django.conf import settings
from django.conf.urls.static import static
from users.views import DashboardUserView, LoginUserView, logout, CreateUserView


urlpatterns = [
    path('users', include('users.urls')),
    path('dashboard', DashboardUserView.as_view(), name='dashboard'),
    path('', LoginUserView.as_view(), name='home'),
    path('logout', logout, name='logout'),
    path('create-user', CreateUserView.as_view(), name='create_user'),
    path('admin/', admin.site.urls),
]

handle404 = error_404

# if the DEBUG is on in settings, then append the urlpatterns as below
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

