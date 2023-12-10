from django.db import models

# Create your models here.

class CustomModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.TextField()
    description = models.TextField()
    is_verified = models.BooleanField(default=False)
    
    # auto_field = models.AutoField(primary_key=True)
    # big_integer_field = models.BigIntegerField()
    # binary_field = models.BinaryField()
    # boolean_field = models.BooleanField()
    # char_field = models.CharField(max_length=255)
    # date_field = models.DateField()
    # date_time_field = models.DateTimeField()
    # decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    # duration_field = models.DurationField()
    # email_field = models.EmailField()
    # file_field = models.FileField(upload_to='files/')
    # float_field = models.FloatField()
    # url_field = models.URLField()
    # time_field = models.TimeField()
    # slug_field = models.SlugField()
    # positive_small_integer_field = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f'{self.id} {self.name}'