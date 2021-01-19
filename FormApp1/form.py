from django import forms

class LoginForm(forms.Form):
    login_email = forms.EmailField()
    login_password = forms.CharField(widget=forms.PasswordInput)