from django.db import models

class Chemistry(models.Model):
    #เกี่ยวกับรายวิชา
    COURSE_CHOICES = (
                        ('เคมี', 'เคมี'),
                        ('ชีววิทยา', 'ชีววิทยา'),
    )
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    course_number = models.CharField(max_length=100)
    titile = models.CharField(max_length=200)
    book_number = models.CharField(max_length=50)
    #การทดลอง
    experiment_number = models.CharField(max_length=50)
    experiment_name = models.CharField(max_length=200)
    #สารเคมีที่ใช้
    chemical_name = models.CharField(max_length=200)
    chemical_properties =  models.TextField()
    ghs_sign = models.ImageField(upload_to='GHS_SIGN/%Y/%m/%d', blank=True)
    #การทิ้งของเสีย
    w1 = models.CharField(max_length=100)
    w2 = models.CharField(max_length=100)
    w3 = models.CharField(max_length=100)
    w4 = models.CharField(max_length=100)
    w5 = models.CharField(max_length=100)
    w6 = models.CharField(max_length=100)
    w7 = models.CharField(max_length=100)
    w = models.CharField(max_length=100)
    #ปฏิกิริยาที่เกิดขึ้นจากการทดลอง
    reactions = models.TextField()

    def __str__(self): 
        return self.experiment_name