"""Custom_Motors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.taskHome, name='home'),
    path('home', views.taskHome, name='home'),
    path('quemSomos', views.taskQSomos, name='sobre'),
    path('sobre', views.taskSobre, name='sobre'),
    path('login', views.taskLogin, name='login'),
    path('user', views.taskUser, name='user'),
    path('produtos', views.taskProduto, name='produto'),
    path('contato', views.taskContato, name='contato'),

    path('moto/<int:id>', views.taskViewM, name='view'),
    path('acessorio/<int:id>/<str:tipo>', views.taskViewA, name='view'),
    path('ferramenta/<int:id>/<str:tipo>', views.taskViewF, name='view'),
    path('catalogo', views.taskList, name='list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)