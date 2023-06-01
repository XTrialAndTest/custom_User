from django.shortcuts import render


# Create your views here.
def index(request):
    return render(
        request,
        "index.html",
    )


def sign_up(request):
    form = ApplicantRegisterForm(request.POST)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('applicantProfile.html')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign-up.html', {'form': form})
