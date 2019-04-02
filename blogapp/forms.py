from django import forms


class CommentForm(forms.Form):
    comment=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Comment '}),required=False)
