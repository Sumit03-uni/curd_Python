from django.contrib import admin
from django.urls import path, include
from crudOperation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crudOperation.urls')),
    path('',views.show),
]