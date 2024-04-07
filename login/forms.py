from django import forms

class LogInForm(forms.Form):
    user_name=forms.CharField(label=('user name'),max_length=50, required=True)
    password=forms.CharField(label=('password'),strip=False,widget=forms.PasswordInput)
    # password=forms.PasswordInput()
    