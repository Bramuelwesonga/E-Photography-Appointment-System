from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'phob'

urlpatterns = [
    path('', views.home, name='home'),
    path('events.html', views.events, name='events'),
    path('schedule.html', views.schedule, name='schedule'),
    path('street.html', views.street, name='street'),
    path('studio.html', views.studio, name='studio'),
    path('tours.html', views.tours, name='tours'),
    path('wedding.html', views.wedding, name='wedding'),
]


