"""
URL configuration for stema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# stema/urls.py

from django.contrib import admin
from django.urls import path, include
from stema.views import home,  handler404_view, profile_view, mentions_legales
from django.contrib.auth.decorators import login_required

#,#, handler500_view

handler404 = handler404_view
# handler500 = handler500_view
from game_app.controllers.GameController import GameController

urlpatterns = [
    path('', GameController.home, name='home'),
    path('admin/', admin.site.urls),
    path('game_app/', include('game_app.urls')),
    path('accounts/', include('allauth.urls')),
    path('mentions_legales/', mentions_legales, name='mentions_legales'), 
    path('social/', include('app_chat.urls')),
]
