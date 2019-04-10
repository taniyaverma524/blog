from django import forms
from django.contrib.auth.models import User
from blogapp.models import Phoneno

class CommentForm(forms.Form):
    comment=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Comment '}),required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email '}), required=True)

class UserForm(forms.ModelForm):

    confirm=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),required=True,max_length=50)
    class meta():
        model =User
        fields= ('first_name', 'last_name', 'username', 'email', 'password')

class PhoneForm(forms.ModelForm):
    model=Phoneno
    class meta():
        fields=" __all__     "