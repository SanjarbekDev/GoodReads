from django  import forms
from django.contrib.auth.models import User

class UserCreateForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password']

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=128)