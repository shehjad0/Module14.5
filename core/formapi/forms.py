from django import forms
from django.forms.widgets import TextInput, Textarea, SelectDateWidget

# Create your forms here.

GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
COUNTRY_CHOICES = [('bangladesh', 'Bangladesh'), ('usa', 'USA'), ('uk', 'UK'), ('other', 'Other')]

class customForm(forms.Form):
    full_name = forms.CharField(label='Full Name', widget=TextInput(attrs={'placeholder': 'Enter your full name'}))
    email = forms.EmailField(label='Email Address', widget=TextInput(attrs={'placeholder': 'example@example.com'}))
    date_of_birth = forms.DateField(label='Date of Birth', widget=SelectDateWidget(years=range(1970, 2010)))
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    country = forms.ChoiceField(label='Country', choices=COUNTRY_CHOICES)
    message = forms.CharField(label='Message', widget=Textarea(attrs={'rows': 4, 'placeholder': 'Enter your message here'}))
    favorite_number = forms.IntegerField(label='Favorite Number', help_text='Enter your favorite number')
    is_subscribed = forms.BooleanField(label='Subscribe to Newsletter', required=False)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)