from django.conf import settings
from django.db import models
from django.utils import timezone

STATUS = ((0,"Draft"),(1,"Publish"))

class Post(models.Model):
    id = models.AutoField
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_images = models.ImageField(default='media/noimg-l.jpg')
    title = models.CharField(max_length=200,unique=True,default='ใส่ชื่อบทความ')
    content = models.TextField(default='ใส่เนื้อหาบทความ')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    post_viewcount = models.PositiveIntegerField(default=0,)
    slug = models.SlugField(max_length=200, default='ใส่ลิงค์บทความ ตัวอย่าง /your-post-content')
    status = models.IntegerField(choices=STATUS , default=1)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Option(models.Model):
    sitename = models.TextField(default='ใส่ชื่อเว็บไซต์')
    sitedescription = models.TextField(default='ใส่รายละเอียดเว็บไซต์')

    