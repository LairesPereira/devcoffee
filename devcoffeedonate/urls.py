from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("charge", views.charge),
    path("success", views.success),
    path("cancel", views.cancel)

]