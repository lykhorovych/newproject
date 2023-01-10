from django.urls import path

from cities.views import *
from .views import CityUpdateView

urlpatterns = [
    path('', index, name='base'),
    path('cities/', CityListView.as_view(), name='all_cities'),
    path('cities/<int:pk>/', CityView.as_view(), name='city'),
    path('cities/add/', CreateCity.as_view(), name='add'),
    path('cities/<int:pk>/update/', CityUpdateView.as_view(), name='update-city'),
    path('cities/<int:pk>/delete/', CityDeleteView.as_view(), name='delete-city'),

]