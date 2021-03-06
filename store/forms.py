from django.forms import ModelForm, TextInput, EmailInput
from django.forms.utils import ErrorList
from .models import CustomersContact

class ParagraphErrorList(ErrorList):

    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class"small error text-danger">%s</p>' % e for e in self])


class ContactForm(ModelForm):
    class Meta:
        model = CustomersContact
        fields = ["name", "email"]
        widget = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'})
        }