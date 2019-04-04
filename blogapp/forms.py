from django import forms


class CommentForm(forms.Form):
    comment=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Comment '}),required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email '}), required=True)
