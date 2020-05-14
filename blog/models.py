from django.conf import settings
from django.db import models
from django.utils import timezone

STATUS = ((0,"Draft"),(1,"Publish"))

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="ชื่อหมวดหมู่")
    content = models.TextField(default='ใส่เนื้อหาบทความ')
    slug = models.SlugField(max_length=200, default='ใส่ลิงค์บทความ ตัวอย่าง /your-post-content')
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"  

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    

class Post(models.Model):
    id = models.AutoField
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_images = models.ImageField(upload_to='media')
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

    def get_cat_list(self):
        k = self.category # for now ignore this instance method
        
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

class Option(models.Model):
    sitename = models.TextField(default='ใส่ชื่อเว็บไซต์')
    sitedescription = models.TextField(default='ใส่รายละเอียดเว็บไซต์')

    def __str__(self):
        return self.title
    