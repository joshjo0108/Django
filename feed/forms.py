from django import forms

class PostForm(forms.Form):
    image = forms.FileField()
    # IT WILL SHOW AS "Description"
    text = forms.CharField(label="Description")