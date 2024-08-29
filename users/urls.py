from django.urls import path
from .views import signupView, signoutView, signinView


app_name = 'users'


urlpatterns = [
    path('signup/', signupView, name='signup'),
    path('signout/', signoutView, name='signout'),
    path('signin/', signinView, name='signin'),
    
]
