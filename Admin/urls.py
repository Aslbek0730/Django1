from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Admin", api.AdminViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Admin/Admin/", views.AdminListView.as_view(), name="Admin_Admin_list"),
    path("Admin/Admin/create/", views.AdminCreateView.as_view(), name="Admin_Admin_create"),
    path("Admin/Admin/detail/<int:pk>/", views.AdminDetailView.as_view(), name="Admin_Admin_detail"),
    path("Admin/Admin/update/<int:pk>/", views.AdminUpdateView.as_view(), name="Admin_Admin_update"),
    path("Admin/Admin/delete/<int:pk>/", views.AdminDeleteView.as_view(), name="Admin_Admin_delete"),

)
