from django.urls import path, register_converter, re_path
from . import views
from . import converters

# converter is used solely for educational purposes
register_converter(converters.WorkNumberConverter, "workconv")

urlpatterns = [
    path('', views.index, name='index'),
    path('biography/', views.biography, name='biography'),
    path('works/', views.works, name='works'),
    path('work/<workconv:no>/', views.work_no, name='work_no'),
    path('contacts/', views.contacts, name='contacts')
]
