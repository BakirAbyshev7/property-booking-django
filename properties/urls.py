from django.urls import path
from .views import PropertyListView, PropertyDetailView

app_name = 'properties'

urlpatterns = [
    path('', PropertyListView.as_view(), name='list'),
    path('<int:pk>/', PropertyDetailView.as_view(), name='detail'),
]
