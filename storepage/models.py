from django.db import models
from custom_user.models import User
from tinymce.models import HTMLField
from django import forms
import os

# Create your models here.
LEVEL_CHOICES = (
    ('High School','High School'),
    ('College', 'College'),
    ('Masters','Masters'),
    ('PhD', 'PhD'),
)

SUBJECT_CHOICES = (
    ('Accounting','Accounting'),
    ('Management', 'Management'),
    ('Nursing','Nursing'),
    ('English', 'English'),
    ('Marketing','Marketing'),
    ('Art', 'Art'),
    ('History','History'),
    ('Law', 'Law'),
    ('Economics','Economics'),
    ('Writing', 'Writing'),
)

TYPE_CHOICES = (
    ('1','1'),
    ('2', '2'),
    ('3','3'),
    ('4', '4'),
    ('5','5'),
    ('6', '6'),
    ('7','7'),
    ('8', '8'),
    ('9','9'),
    ('10', '10'),
)

HOUR_CHOICES = (
    ('0','0'),
    ('6', '6'),
    ('7','7'),
    ('8', '8'),
    ('9','9'),
    ('10', '10'),
)

DAY_CHOICES = (
    ('0','0'),
    ('1','1'),
    ('2', '2'),
    ('3','3'),
    ('4', '4'),
    ('5','5'),
    ('6', '6'),
    ('7','7'),
    ('8', '8'),
    ('9','9'),
    ('10', '10'),
)

def file_size(value):
    limit = 10 * 1024 * 1024

    if isinstance(value, (list, tuple)):
        for file in value:
            if file.size > limit:
                raise forms.ValidationError('Files size should not exceed 10 MB.')
            else:
                if value.size > limit:
                    raise forms.ValidationError('Files size should not exceed 10 MB.')







class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=500, blank=True, null=True, choices=SUBJECT_CHOICES, default='Accounting')
    pages = models.CharField(max_length=500, blank=True, null=True, choices=TYPE_CHOICES, default='1')
    hours = models.CharField(max_length=500, blank=True, null=True, choices=HOUR_CHOICES, default='0')
    days = models.CharField(max_length=500, blank=True, null=True, choices=DAY_CHOICES, default='0')
    level = models.CharField(max_length=500, choices=LEVEL_CHOICES, default='College')
    title = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    
    

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.title
    
class OrderFiles(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    instructions = HTMLField(blank=True, null=True)
    file = models.FileField(upload_to='order_doc/', blank=True, null=True)
    created_at =  models.DateTimeField(auto_now_add=True)

    def filename(self):
        return os.path.basename(self.file.name)

    

class PayInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.CharField(max_length=500)
    created_at =  models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Payments'

    def __str__(self):
        return self.amount
    


class Answers(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    description = HTMLField(blank=True, null=True)
    file = models.FileField(upload_to='Final/', blank=True, null=True)
    created_at =  models.DateTimeField(auto_now_add=True)
