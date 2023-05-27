from django.shortcuts import render
from .models import Employee


def dashboard(request):
    context = {
        'employees': Employee.objects.all()
    }

    return render(request, 'resident/index.html', context)