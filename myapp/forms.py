from .modles import *


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('email', 'username', 'first_name', 'last_name')


class ApplicantProfileForm(forms.ModelForm):
    class Meta:
        model = ApplicantProfile
        fields = ['first_name', 'last_name', 'email', 'bio', 'contact']
