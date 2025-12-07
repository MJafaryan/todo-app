from django.urls import include, path

urlpatterns = [
    path("api/v1/", include("accounts.api.v1.urls"), name="accounts-api-v1"),
]
