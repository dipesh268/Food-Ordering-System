from django.contrib import admin
from product.models import *
# Register your models here.
class customerAdmin(admin.ModelAdmin):
    list_display = ['customer_F_name','customer_L_name','customer_mobile_no','customer_address','customer_pincode','customer_email','customer_gender','password']
admin.site.register(customer,customerAdmin)
class product_tAdmin(admin.ModelAdmin):
    list_display = ['product_type']
admin.site.register(product_t,product_tAdmin)
class product_listAdmin(admin.ModelAdmin):
    list_display = ['id','prodct_name','product_type','product_price','product_Description','product_image']
admin.site.register(product_list,product_listAdmin)
