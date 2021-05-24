from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    surname = forms.CharField(label='Фамилия', max_length=100)
    phone = forms.CharField()
    subject = forms.TextInput()
    message = forms.Textarea()
