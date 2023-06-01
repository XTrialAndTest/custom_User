from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login


# Create your views here.
def index(request):
    return render(
        request,
        "index.html",
    )


def applicant_sign_up(request):
    form = Applicant_Creation_Form(request.POST)
    if request.method == "POST":
        form = Applicant_Creation_Form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            applicant_type = user
            applicant_type.user_type = "applicant"
            applicant_type.save()
            login(request, user)

            return redirect("applicant_profile")
    else:
        form = Applicant_Creation_Form()

    return render(request, "registration/applicant_sign_up.html", {"form": form})


def applicant_profile(request):
    form = ApplicantProfileForm(request.POST)
    if request.method == "POST":
        form = ApplicantProfileForm(request.POST)
        if form.is_valid():
            applicant_profile = form.save()
            login(request, applicant_profile)

    return render(request, "applicant_profile.html", {"form": form})


def overrall_register(request):
    return render(request, "registration/overrall_register.html")


def employer_sign_up(request):
    form = Employer_Creation_Form(request.POST)
    if request.method == "POST":
        form = Employer_Creation_Form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            applicant_type = user
            applicant_type.user_type = "applicant"
            applicant_type.save()
            login(request, user)

            return redirect("applicant_profile")
    else:
        form = Employer_Creation_Form()

    return render(request, "registration/employer_sign_up.html", {"form": form})


def employer_profile(request):
    form = EmployerProfileForm(request.POST)
    if request.method == "POST":
        form = EmployerProfileForm(request.POST)
        if form.is_valid():
            employer_profile = form.save()
            login(request, applicant_profile)

    return render(request, "employer_profile.html", {"form": form})
