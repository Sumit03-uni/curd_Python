from django.urls import path  
from crudexample import views  
urlpatterns = [  
      
    path('show',views.show, name='show'),  
    path('epe', views.epe, name='epe'),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  