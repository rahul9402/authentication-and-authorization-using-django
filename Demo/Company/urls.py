
from django.urls import path
from . import views

urlpatterns = [

    path('',views.registerpage),
    path('userlog/',views.userlogin),
    path('adminlog/',views.adminlogin),
    path('adminhome/',views.adminhome),
    path('pending/',views.pending),
    path('approve/<int:id>/',views.approve),
    path('approved/',views.approved)

]

