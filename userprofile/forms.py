from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'py-4 px-4 p-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'})
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'py-4 px-4 p-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'})
    )
