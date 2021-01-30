from django.urls import path
from pages.views import home

urlpatterns = [
    path( '', home, name='home' ),
    # path('blog/', home, name='home'),
]
