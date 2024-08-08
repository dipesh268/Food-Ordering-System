from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.


#Create the product type model
class product_t(models.Model):
    product_type = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.product_type
    
    #arrenge the product type in Ascending
    class Meta:
        ordering = ['product_type']


#create the product table model
class product_list(models.Model):
    prodct_name = models.CharField(max_length=200)
    product_type = models.ForeignKey(product_t,related_name='type',on_delete=models.CASCADE)
    product_price = models.FloatField()
    product_Description = models.TextField()
    product_image = models.ImageField(upload_to="images")
    
    def __str__(self) -> str:
        return self.prodct_name


#create user model with the baseUser model to store the user details
class user(AbstractBaseUser):
    customer_F_name = models.CharField(max_length=100)
    customer_L_name = models.CharField(max_length=100)
    customer_mobile_no = models.IntegerField()
    customer_address = models.TextField()
    customer_pincode = models.IntegerField()
    customer_gender = models.CharField(max_length=10,default='Male')
    customer_email = models.EmailField(unique=True)
    
    #change the username to Email for LOGIN
    USERNAME_FIELD = 'customer_email'
    REQUIRED_FIELDS = ['customer_F_name','customer_L_name','customer_mobile_no','customer_address','customer_pincode','customer_gender']
    
    
    def set_password(self, password):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for AnonymousUser."
        )
    
    def __str__(self) -> str:
        return self.customer_email
    
    #for the email and mobile number is not store in multiple time in DB
    class Meta:
        unique_together = ['customer_mobile_no','customer_email']

#store the cart item for the user
class cart(models.Model):
    prodct_name = models.CharField(max_length=200)
    product_type = models.ForeignKey(product_t,related_name='type2',on_delete=models.CASCADE)
    product_price = models.FloatField()
    product_Description = models.TextField()
    product_image = models.ImageField(upload_to="images")
    quantity = models.IntegerField(default=1)
    