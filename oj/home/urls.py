from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('logout',views.logout,name='logout'),
    path('createGroup',views.createGroup,name='createGroup'),
    path('joinGroup',views.joinGroup,name='joinGroup'),
    path('practice',views.practice,name='practice'),
]
