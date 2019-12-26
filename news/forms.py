from django import forms

class NewsLetterForm(forms.Form):
    your_name = forms.Charfield(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
