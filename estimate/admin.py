from django.contrib import admin
from estimate.models import Product, Receiver, Supplier

#admin.site.register(Product)   # 이렇게 사용하면 Admin 페이지에서 Product 조회시 item_name만 출력됨. (unit_price는 출력안됨)
admin.site.register(Receiver)
admin.site.register(Supplier)

# Admin 페이지에서 Product의 item_name, unit_price를 출력함 (Django admin page customizing)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'unit_price')

admin.site.register(Product, ProductAdmin)
