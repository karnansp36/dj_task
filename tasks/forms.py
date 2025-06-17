from django import forms
from .models import Task, User

class TaskForm(forms.Form):
    """
    Form for creating and updating tasks
    """
    title = forms.CharField(max_length=200, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Task title'}
    ))
    description = forms.CharField(max_length=2000, required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Task description', 'rows': 4}
    ))
    status = forms.ChoiceField(choices=(
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ), widget=forms.Select(attrs={'class': 'form-control'}))
    priority = forms.ChoiceField(choices=(
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent')
    ), widget=forms.Select(attrs={'class': 'form-control'}))
    due_date = forms.DateTimeField(required=False, widget=forms.DateTimeInput(
        attrs={'class': 'form-control', 'type': 'datetime-local'}
    ))
    completed = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input'}
    ))
    tags = forms.CharField(max_length=200, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Tags (comma-separated)'}
    ))
    
    def clean_tags(self):
        """Converts comma-separated tags into a list"""
        tags_text = self.cleaned_data.get('tags', '')
        if not tags_text:
            return []
        return [tag.strip() for tag in tags_text.split(',') if tag.strip()]

class UserForm(forms.Form):
    """
    Form for creating and updating users
    """
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}
    ))
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}
    ))
    first_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First name'}
    ))
    last_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last name'}
    ))