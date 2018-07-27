from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import listModel

class infoAddForm(forms.ModelForm):

    class Meta:
        model = listModel
        fields = ('lst_name', 'lst_email',)