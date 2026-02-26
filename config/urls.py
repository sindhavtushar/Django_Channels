# config.urls

from django.contrib import admin
from django.urls import path, include
from .views import home
from apps.livecalculator.views import live_calculator_view
from apps.echo.views import echo_room

urlpatterns = [
    path('', home, name='home'), 
    # Django Admin URLs
    path('admin/', admin.site.urls),
    
    # Live calculators URLs
    path('calculator/', live_calculator_view, name='live_calc_page'),
    
    # Bingo Game URLs
    path("bingo/<str:room_name>/", echo_room, name="bingo_room"),

    # Chat URLs
    path('chat/', include('apps.chat.urls')),

]