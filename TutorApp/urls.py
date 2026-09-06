from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name = "home"),
    path('courses',views.Course, name = "Course"),
    path('reviews',views.review, name = "reviews"),
    path('givereview',views.review_forms, name = "reviewsForm"),
    path('edit/<int:id>/',views.edit,name='edit_review'),
    path('delete/<int:id>/',views.delete,name="delete_review"),
]










