from django.contrib import admin
from django.urls import path
from myapp import views  

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  
    path('add',views.add, name='add'),  
    path('show.html',views.show, name='show'),  
    path('about.html',views.about, name='about'),  
    path('edit/<int:id>', views.edit, name='edit'),  
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.destroy, name='destroy'),  
    
]

