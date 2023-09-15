from django.urls import path  
from fisrtApp import views  

urlpatterns = [  
    path('register/', views.register, name='register'),
    path('add', views.emp,name="create"),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('show/<int:id>', views.get_product),
]  