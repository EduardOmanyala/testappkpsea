from django.contrib import admin
from storepage.models import Order, OrderFiles, PayInfo

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderFiles)
admin.site.register(PayInfo)