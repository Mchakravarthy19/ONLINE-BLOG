from django import forms
from .models import JournalEntry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Feedback
class JournalForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'content', 'image', 'mood', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter a title'}),
            'content': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your thoughts...'}),
            'tags': forms.TextInput(attrs={'placeholder': 'e.g. happy, stress'}),
        }

    def __init__(self, *args, **kwargs):
        super(JournalForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'mood':
                self.fields[field].widget.attrs.update({'class': 'form-select'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control'})


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Choose a username'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-select'}),
        }