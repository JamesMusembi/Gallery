from django .urls import path
from . import views

urlpatterns=[
    path('', views.index, name="indexpage"),
    path('search/', views.show_category, name="search_categories"),
    path('oneimage/<int:pk>', views.viewPhoto, name="viewPhoto"),
    path('searchbylocation/', views.show_by_location, name="showlocation")
]