from django.contrib import admin
from billing.models import Post, Contact, PaymentDetails
# Register your models here.
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(PaymentDetails)