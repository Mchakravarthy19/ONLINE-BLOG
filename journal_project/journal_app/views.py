from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, JournalForm
from .models import JournalEntry
from .forms import FeedbackForm
import random
from django.shortcuts import render
from datetime import date

def home(request):
    youtube_videos = [
        "https://www.youtube.com/embed/ZToicYcHIOU",  # Mindfulness
        "https://www.youtube.com/embed/1vx8iUvfyCY",  # Deep breathing
        "https://www.youtube.com/watch?v=tmefMWAdAJw",  # Sleep tips
        "https://www.youtube.com/embed/inpok4MKVLM",  # Meditation
        "https://www.youtube.com/embed/4pLUleLdwY4"   # Stress relief
    ]
    selected_video = random.choice(youtube_videos)
    current_date = date.today()

    context = {
        'video_url': selected_video,
        'current_date': current_date
    }
    return render(request, 'journal_app/home.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('journal_list')
    else:
        form = SignUpForm()
    return render(request, 'journal_app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('journal_list')
    else:
        form = AuthenticationForm()
    return render(request, 'journal_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def journal_list(request):
    journals = JournalEntry.objects.filter(user=request.user)  # Correct: user, not author
    current_date = date.today()  # ✅ Get current date
    return render(request, 'journal_app/journal_list.html', {
        'journals': journals,
        'current_date': current_date})

@login_required
def journal_detail(request, pk):
    journal = get_object_or_404(JournalEntry, pk=pk, user=request.user)  # user here
    return render(request, 'journal_app/journal_detail.html', {'journal': journal})

@login_required
def journal_create(request):
    if request.method == 'POST':
        form = JournalForm(request.POST, request.FILES)  # include files for images
        if form.is_valid():
            journal = form.save(commit=False)
            journal.user = request.user  # assign to user, not author
            journal.save()
            return redirect('journal_list')
    else:
        form = JournalForm()
    return render(request, 'journal_app/journal_form.html', {'form': form})

@login_required
def journal_update(request, pk):
    journal = get_object_or_404(JournalEntry, pk=pk, user=request.user)  # user here
    if request.method == 'POST':
        form = JournalForm(request.POST, request.FILES, instance=journal)  # handle files
        if form.is_valid():
            form.save()
            return redirect('journal_detail', pk=pk)
    else:
        form = JournalForm(instance=journal)
    return render(request, 'journal_app/journal_form.html', {'form': form})

@login_required
def journal_delete(request, pk):
    journal = get_object_or_404(JournalEntry, pk=pk, user=request.user)  # user here
    if request.method == 'POST':
        journal.delete()
        return redirect('journal_list')
    return render(request, 'journal_app/journal_confirm_delete.html', {'journal': journal})

@login_required
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Now this works because it’s a ModelForm
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'journal_app/feedback.html', {'form': form})
