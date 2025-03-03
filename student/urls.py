from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("student", api.studentViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("student/student/", views.studentListView.as_view(), name="student_student_list"),
    path("student/student/create/", views.studentCreateView.as_view(), name="student_student_create"),
    path("student/student/detail/<int:pk>/", views.studentDetailView.as_view(), name="student_student_detail"),
    path("student/student/update/<int:pk>/", views.studentUpdateView.as_view(), name="student_student_update"),
    path("student/student/delete/<int:pk>/", views.studentDeleteView.as_view(), name="student_student_delete"),

)
