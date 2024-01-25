from django import forms
from django.forms import ClearableFileInput

from storepage.models import Order, OrderFiles



class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title','subject', 'pages', 'hours', 'days' ]


class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = OrderFiles
        fields = ['instructions','file']



