from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


# Create your models here.
class CustomUser(AbstractUser):
    type_user = (
        ("Admin", "Admin"),
        ("applicant", "Applicant"),
        ("Employer", "Employer"),
    )

    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    full_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    last_login = models.DateTimeField(auto_now=True, null=True)
    user_type = models.CharField(max_length=200, choices=type_user)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "full_name"]

    def __str__(self):
        return self.username


class ApplicantManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(user_type="applicant")


class Applicant(CustomUser):
    user_type = "applicant"
    applicant = ApplicantManager()

    class Meta:
        proxy = True


class ApplicantProfile(models.Model):
    user = models.OneToOneField(Applicant, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    profile_Pic = CloudinaryField("profile_pic")
    contact = models.CharField(max_length=12)

    def __str__(self):
        return self.user.full_name
