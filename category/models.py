from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    ppe_sign = models.ImageField(upload_to='PPE_SIGN/%Y/%m/%d', blank=True)
    cat_type = models.IntegerField()

    def __str__(self):
        return self.name