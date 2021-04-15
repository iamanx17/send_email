from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('delete/',views.delete, name='delete'),
    path('addemail/',views.addemail, name='addemail'),
    path('update/',views.updatemail,name='updatemail'),
    path('update/<int:id>',views.update,name='update'), 
    #account 
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]
