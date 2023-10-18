from django.shortcuts import render
from .models import govt_sign
from .forms import application_form

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = application_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'upload.html')
    else:
        form = application_form()
    return render(request, 'upload.html', {'form': form})    