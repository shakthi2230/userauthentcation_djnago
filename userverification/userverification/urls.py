from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('createaccount', views.createaccount, name="createaccount"),
    path('login', views.login, name="login"), 
    path('records', views.records, name="records"), 
    path('deletedata/<int:id>',views.deletedata ,name="deletedata"),
    path('forgotpassword',views.forgotpassword ,name="forgotpassword"),
    path('updatepassword/<int:id>',views.updatepassword ,name="updatepassword"),
    
    

]
