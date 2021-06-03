from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    surname = forms.CharField(label='Фамилия', max_length=100)
    phone = forms.CharField()
    subject = forms.TextInput()
    order = forms.BooleanField(label='Заказать фотосессию', required=False)
    date = forms.CharField()
    message = forms.Textarea()
