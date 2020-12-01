from django.shortcuts import render, redirect

from accounts.forms import SignUpForm


def user_profile(request, pk):
    pass


def signup_user(request):
    if request.method == "GET":
        context = {'form': SignUpForm()}
        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)

