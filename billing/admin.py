from django.contrib import admin
from billing.models import Post, Contact, PaymentDetails, PaymentUpdates, PaymentInfo
# Register your models here.
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(PaymentDetails)
admin.site.register(PaymentUpdates)
admin.site.register(PaymentInfo)