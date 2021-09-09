import datetime
from django.contrib import admin
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.utils import timezone
from django.utils.timezone import now

class SupportRequest(models.Model):
    sender_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, blank=True)
    company_name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    problem_description = models.TextField(max_length=500)
    comment = models.TextField(max_length=500,blank=True)
    callback_date = models.DateField(null=True, blank=True)
    callback_time = models.TimeField(null=True, blank=True)
    callback_date_time = models.DateTimeField(null=True, blank=True)
    pub_date = models.DateTimeField(default=now, editable=False)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
    
    def save(self, force_insert=False, force_update=False):
        if self.callback_date  and self.callback_time:
            self.callback_date_time = datetime.datetime.combine(self.callback_date, self.callback_time)

        super(SupportRequest, self).save(force_insert, force_update)
