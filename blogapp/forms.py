from django import forms
from django.contrib.auth.models import User
from blogapp.models import Profile
from django.core.validators import validate_email

class CommentForm(forms.Form):
    comment=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Comment '}),required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email '}), required=True)

class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter UserName'}),
                               required=True, max_length=30)

    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
                            required=True, max_length=30)

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}), required=True,
        max_length=30)

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}), required=True,
        max_length=30)

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}), required=True,
        max_length=30)

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}), required=True,
        max_length=30)

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'confirm_password']

    def clean_username(self):
        username=self.cleaned_data['username']
        if username.isdigit():
            raise forms.ValidationError("user must contain atleast a character")

        return username

    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            verify=validate_email(email)
        except:
             raise forms.ValidationError("Email is not Valid")
        return email

    def clean_confirm_password(self):
        print(self.cleaned_data)
        password=self.cleaned_data.get('password')


        confirm_password=self.cleaned_data.get('confirm_password')


        if(password!=confirm_password):

            raise  forms.ValidationError("confirm password is not matched ")
        else:
            if(len(password)<8):
                raise forms.ValidationError("password must be atleast  8 character")
            if(password.isdigit()):
                raise forms.ValidationError("password must contain atleast a character")
            if(password.isalnum()):
                raise forms.ValidationError("Password must contain atleast a special character")
        return password

YEARS= [x for x in range(1940,2021)]
class ProfileForm(forms.ModelForm):
    phone=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mobile number '}), required=True)
    city= forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}), required=True,
        max_length=30)

    birthday= forms.DateField(label='Birthday', widget=forms.SelectDateWidget(years=YEARS))
    class Meta:
        model = Profile
        fields=['phone','city','gender','birthday']

