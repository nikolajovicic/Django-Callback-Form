from django.forms import ModelForm
from django import forms
from .models import SupportRequest
from django.contrib.admin.widgets import AdminDateWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class SupportRequestForm(ModelForm):
    class Meta:
        model = SupportRequest
        fields = ['sender_name',
                'email',
                'phone_number',
                'company_name',
                'subject',
                'problem_description',
                'callback_date',
                'callback_time']
        widgets = {
            #'callback_date_time': DateTimeInput())
            #'callback_date': forms.DateField(widget=AdminDateWidget())
            'callback_date': DateInput(),
            'callback_time': TimeInput()
        }