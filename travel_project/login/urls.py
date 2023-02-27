from . import views
from django.urls import path

urlpatterns=[
    path('register',views.register,name='register'),
    path('new',views.new,name='new'),
    path('logout',views.logout,name='logout')
]