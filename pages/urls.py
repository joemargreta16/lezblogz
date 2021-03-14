from django.conf.urls import url
from django.urls import path
from pages.views import home, my_profile, ChangePassword, update_profile
from . import views

app_name = 'pages'

urlpatterns = [
    path( '', home, name='home' ),
    # url( r'^my_profile/(?P<username>\w{0,50})/$', views.my_profile, name='my_profile' ),
    path( 'my_profile/', my_profile, name='my_profile' ),
    path( 'my_profile/update/', update_profile, name='update_profile' ),
    # path( 'my_profile/<int:pk>/', UpdateProfilePageForm.as_view(), name='my_profile_update' ),
    path( 'change-password/', ChangePassword.as_view( template_name='pages/change_password.html' ),
          name='change-password' ),
    path( 'password_success/', views.password_success, name='password_success' ),
]
