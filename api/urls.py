from django.urls import path , include
from search import views

urlpatterns = [
    path('mentors/', views.use_api, name="mentors"),
    path('search_mentors/', views.search_api, name="search_mentors"),   
]
