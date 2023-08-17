from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# accounts veiws.

def register(request):
    """Register a new user."""
    if request.method != "POST":
        # Display blank registration form.
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            # Log in, redirect to home page.
            login(request, new_user)
            return redirect('letter_app:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

# def register(request):
#     """Register a new user."""
#     return render(request, 'registration/register.html')

# How to response with HttpResponse().
# from django.http import HttpResponse
# import datetime
# 
# def register(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)
