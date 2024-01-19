from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginpage,name='login'),
    path('reg/',views.registrationpage,name='registration')
]
