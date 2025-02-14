from django import forms
from .models import *
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class RequestForm(forms.Form):
    name = forms.CharField(label="Ім'я", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'NAME'}), )
    email = forms.EmailField(label="Е-пошта", max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    subject = forms.CharField(label="Тема", max_length=150, required=False, widget=forms.TextInput(attrs={'placeholder': 'SUBJECT'}))
    content = forms.CharField(label="Ваше повідомлення", max_length=1000, widget=forms.Textarea(attrs={'placeholder': 'MESSAGE'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={
            'data-theme': 'dark',
            'data-size': 'compact',
        }))

    class Meta:
        model = Request
        fields = '__all__'