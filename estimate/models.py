from django.db import models

class Product(models.Model):
    item_name = models.CharField(max_length=20)
    unit_price = models.IntegerField(default=400000)

    def __str__(self):
        return self.item_name
 
   
class Receiver(models.Model):
    receiver_name = models.CharField(max_length=20)
    receiver_company = models.CharField(max_length=20)
    estimate_date = models.DateTimeField('published')

class Supplier(models.Model):
    corp_reg_number = models.IntegerField()     # 사업자 등록번호
    corp_name = models.CharField(max_length=20)
    tel = models.IntegerField()
    ceo_name = models.CharField(max_length=15)
    address = models.CharField(max_length=80)
    business_type = models.CharField(max_length=15)
    business_item = models.CharField(max_length=15)
