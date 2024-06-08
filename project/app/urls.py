from django.urls import path
from .views import home,about,contact,register,login,registerdata,logindata,Querydata,Show,delete,editpage,updatedata

urlpatterns= [
     path('',home,name='home'),
     path('about/',about,name='about'),
     path('contact/',contact,name='contact'),
     path('register/',register,name='register'),
     path('login/',login,name='login'),
     path('registerdata/',registerdata,name='registerdata'),
     path('logindata/',logindata,name='logindata'),
     path('Querydata/',Querydata,name='Querydata'),
     path('Show/',Show,name='Show'),
     path('delete/<int:pk>/<ml>',delete,name='delete'),
     path('editpage/<int:pk>',editpage,name='editpage'),
      path('update/<int:pk>/',updatedata,name='update'),
]