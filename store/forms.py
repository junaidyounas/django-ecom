from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=False)
    address = forms.CharField(max_length=200, required=True)
    phone = forms.CharField(max_length=12, required=True)
    message = forms.CharField(max_length=400, widget=forms.Textarea, required=False)