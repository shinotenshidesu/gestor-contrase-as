from django.urls import include, path
from rest_framework import routers
from passmanager import views

router = routers.DefaultRouter()
router.register(r"passmanager", views.PassManagerView, "passmanager")

urlpatterns = [
    path("passmanager/", include(router.urls)),
]