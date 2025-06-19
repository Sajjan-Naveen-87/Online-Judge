from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home/login',views.login,name='login'),
    path('home/logout',views.logout,name='logout'),
    path('createGroup',views.createGroup,name='createGroup'),
    path('joinGroup',views.joinGroup,name='joinGroup'),
    path('practice',views.practice,name='practice'),
]
