from django.urls import path  
from crudOperation import views  

urlpatterns = [  
    path('', views.show, name='home'),  # Landing page 
    path('add_emp/', views.create, name='add_emp'),  
    path('edit/<int:id>/', views.edit, name='edit'),  
    path('update/<int:id>/', views.update, name='update'),  
    path('delete/<int:id>/', views.destroy, name='delete'),  
]  