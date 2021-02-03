from django.urls import path
from pages.views import home, my_profile

urlpatterns = [
    path( '', home, name='home' ),
    path('my_profile/', my_profile, name='my_profile'),
]
