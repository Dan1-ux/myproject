from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Prospect
from .forms import Prospect, ProspectForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


@login_required
def kanban_view(request):
    prospects = Prospect.objects.all()
    context = {
        'fase1': prospects.filter(status='fase1'),
        'fase2': prospects.filter(status='fase2'),
        'fase3': prospects.filter(status='fase3'),
        'fase4': prospects.filter(status='fase4'),
    }
    return render(request, 'kanban.html', context)

@login_required
def dashboard_view(request):
    total_prospects = Prospect.objects.count()
    completed = Prospect.objects.filter(status='fase4').count()
    in_progress = total_prospects - completed
    context = {
        'total': total_prospects,
        'completed': completed,
        'in_progress': in_progress,
        'prospects': Prospect.objects.all()
    }
    return render(request, 'dashboard.html', context)

@login_required
def add_prospect(request):
    if request.method == 'POST':
        form = ProspectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kanban')
    else:
        form = ProspectForm()
    return render(request, 'add_prospect.html', {'form': form})

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirige al usuario a la página que intentaba acceder, o a 'kanban' por defecto
            next_url = request.GET.get('next')  # Obtiene el parámetro 'next' de la URL
            return redirect(next_url if next_url else 'kanban')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')