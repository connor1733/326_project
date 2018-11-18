from django.urls import path
from . import views

urlpatterns = [
    path("class-search/", views.class_search, name="class_search"),
    path("search-results/", views.search_results, name="search_results"),
    path("students/", views.StudentListView.as_view(), name="student_list"),
    path("courses/", views.CourseListView.as_view(), name="course_list"),
    path("course-instances/", views.CourseInstanceListView.as_view(), name="course_instance_list"),

    path("course/<int:pk>", views.CourseDetailView.as_view(), name="course_info"),
    path("course-instance/<int:pk>", views.CourseInstanceDetailView.as_view(), name="course_instance_info"),
    path("course-review/<int:pk>", views.AddAReview.as_view(), name="add_a_review"),


    path("professor/<str:pk>", views.ProfessorDetailView.as_view(), name="professor_info"),
    path("professors/", views.ProfessorListView.as_view(), name="professor_list"),

    path("<int:pk>", views.Schedule.as_view(), name="dashboard"),
    path("shopping-cart/<int:pk>", views.ShoppingCartView.as_view(), name="shopping_cart"),
    path("student-info/<int:pk>", views.StudentDetailView.as_view(), name="student_info"),
    path("unenroll-classes/", views.unenroll_classes, name="unenroll"),

    path("", views.index, name="index"),
    
    
]
