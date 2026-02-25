"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from apps.livecalculator.views import live_calculator_view
from apps.echo.views import room

urlpatterns = [
    # Django Admin URLs
    path('admin/', admin.site.urls),
    
    # Live calculators URLs
    path('calculator/', live_calculator_view, name='live_calc_page'),
    
    # Bingo Game URLs
    path("bingo/<str:room_name>/", room, name="bingo_room"),
]
