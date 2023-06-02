from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "applicant_sign_up",
        views.applicant_sign_up,
        name="applicant_sign_up",
    ),
    path("applicant_profile/", views.applicant_profile, name="applicant_profile"),
    path("overrall_register", views.overrall_register, name="overrall_register"),
    path(
        "employer_sign_up",
        views.employer_sign_up,
        name="employer_sign_up",
    ),
    path("employer_profile/", views.employer_profile, name="employer_profile"),
    path('job_creation', views.job_creation, name="job_creation"),
]
