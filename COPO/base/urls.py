from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('storage/',views.storage, name='storage'),
    path('view/<int:pk>',views.View, name='view')
]
