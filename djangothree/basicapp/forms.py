from django import forms
from django.core import validators

def cekvalid(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError('nama harus di awali A')

class FormName (forms.Form):
    name = forms.CharField(validators=[cekvalid])
    email = forms.EmailField()
    vemail = forms.EmailField(label="input lagi")
    text = forms.CharField(widget=forms.Textarea)
    

    def clean(self):
        allcleandata = super().clean()
        email = allcleandata['email']
        verifemail = allcleandata['vemail']

        if email != verifemail:
            raise forms.ValidationError("email anda harus sama")