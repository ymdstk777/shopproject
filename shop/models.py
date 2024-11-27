from django.db import models
 
# Create your models here.
from accounts.models import CustomUser
 
class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ',max_length=20
    )
   
    def __str__(self):
        return self.title
   
   
class ShopPost(models.Model):
    user = models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.CASCADE)
    title = models.CharField(verbose_name='商品名',max_length=200)
    description = models.TextField(verbose_name='商品説明',max_length=500)
    price = models.IntegerField(verbose_name='価格')
    category = models.ForeignKey(Category,verbose_name='カテゴリ',on_delete=models.PROTECT)
    condition = models.CharField(choices=[('great','新品に近い状態'),('good','状態が良い'),('bad','状態があまり良くない')],max_length=50,verbose_name='状態')
    product_image = models.ImageField(verbose_name='商品写真',upload_to='product_images')
    posted_at = models.DateTimeField(verbose_name='出品日時',auto_now_add=True)
   
    def __str__(self):
        return self.title
   
   
class Order(models.Model):
    user = models.ForeignKey(CustomUser,verbose_name='購入者名',on_delete=models.CASCADE)
    products_id = models.ForeignKey(ShopPost,verbose_name='商品id',on_delete=models.CASCADE)
    payment = models.CharField(choices=[('creditcard','クレジットカード',),('realmoney','現金'),('electronic_money','電子マネー')],max_length=50,verbose_name='支払方法')
    order_day = models.DateTimeField(verbose_name='注文日',auto_now_add=True)
    def __str__ (self):
        return str(self.order_day)