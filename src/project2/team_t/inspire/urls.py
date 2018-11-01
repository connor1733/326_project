from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("class-search/", views.class_search, name="class_search"),
    path("search-results/", views.search_results, name="search_results"),
    path("shopping-cart/<int:pk>", views.shopping_cart, name="shopping_cart"),
    path("studentinfo/<int:pk>", views.studentinfo.as_view(), name="studentinfo"),
    path("course/<int:pk>", views.course.as_view(), name="courseinfo"),
    path("professors/<int:pk>", views.professors.as_view(), name="professorinfo"),
    
    
    
]