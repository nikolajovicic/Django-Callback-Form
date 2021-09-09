from django.forms import ModelForm
from django import forms
from django.forms.widgets import DateTimeBaseInput
from .models import SupportRequest
from django.contrib.admin.widgets import AdminDateWidget
import datetime as dt
class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

#HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(9, 18)]

HALF_HOUR_CHOICES = [
        ('08:00', dt.time(8,0)),
        ('08:30', dt.time(8,30)),
        ('09:00', dt.time(9,0)),
        ('09:30', dt.time(9,30)),
        ('10:00', dt.time(10,0)),
        ('10:30', dt.time(10,30)),
        ('11:00', dt.time(11,0)),
        ('11:30', dt.time(11,30)),
        ('12:00', dt.time(12,0)),
        ('12:30', dt.time(12,30)), #9
        ('13:00', dt.time(13,0)),
        ('13:30', dt.time(13,30)),
        ('14:00', dt.time(14,0)),
        ('14:30', dt.time(14,30)),
        ('15:00', dt.time(15,00)),
        ('15:30', dt.time(15,30)),
        ('16:00', dt.time(16,00)),
        ('16:30', dt.time(16,30)),
        ('17:00', dt.time(17,00)),
        ('17:30', dt.time(17,30)),
        ('18:00', dt.time(18,00)),
        ('18:30', dt.time(18,30)),
        ('19:00', dt.time(19,00)),
        ('19:30', dt.time(19,30)),
        ('20:00', dt.time(20,00)), #24
    ]

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
                'callback_date': DateInput(),
                'callback_time': forms.Select(choices=HALF_HOUR_CHOICES)
            }
        labels = {
            'sender_name': "Your name",
            'email': "E-mail",
            'callback_date': "Date when we can contact You",
            'callback_time': 'Time'
        }   