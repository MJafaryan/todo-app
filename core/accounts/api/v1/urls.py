from django.urls import include, path
from .views import RegisterView

urlpatterns = [
    path("", include("rest_framework.urls"), name="login-logout"),
    path("register/", RegisterView.as_view(), name="register"),
]
