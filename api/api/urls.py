from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.PersonList.as_view(), name='person-list'),
]
