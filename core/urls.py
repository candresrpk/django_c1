from django.contrib import admin
from django.urls import path, include
from .views import homeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('users/', include('users.urls')),
    path('tasks/', include('tasks.urls'))
    
]
