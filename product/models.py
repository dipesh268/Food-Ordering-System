from django.db import models

# Create your models here.

class product_t(models.Model):
    product_type = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.product_type
    
    class Meta:
        ordering = ['product_type']



class product_list(models.Model):
    prodct_name = models.CharField(max_length=200)
    product_type = models.ForeignKey(product_t,related_name='type',on_delete=models.CASCADE)
    product_price = models.FloatField()
    product_Description = models.TextField()
    product_image = models.ImageField(upload_to="images")
    
    def __str__(self) -> str:
        return self.prodct_name



class customer(models.Model):
    customer_F_name = models.CharField(max_length=100)
    customer_L_name = models.CharField(max_length=100)
    customer_mobile_no = models.IntegerField()
    customer_address = models.TextField()
    customer_pincode = models.IntegerField()
    customer_gender = models.CharField(max_length=10,default='Male')
    customer_email = models.EmailField()
    password = models.CharField(max_length=16,null=False,default=None)
    
    
    def set_password(self, password):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for AnonymousUser."
        )
    
    def __str__(self) -> str:
        return f'{self.customer_F_name}{self.customer_L_name}'
    
    class Meta:
        unique_together = ['customer_mobile_no','customer_email']


class cart(models.Model):
    prodct_name = models.CharField(max_length=200)
    product_type = models.ForeignKey(product_t,related_name='type2',on_delete=models.CASCADE)
    product_price = models.FloatField()
    product_Description = models.TextField()
    product_image = models.ImageField(upload_to="images")
    quantity = models.IntegerField(default=1)
    