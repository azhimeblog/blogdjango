from django.conf import settings
from django.db import models
from django.utils import timezone

STATUS = ((0,"Draft"),(1,"Publish"))

class Post(models.Model):
    id = models.AutoField
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_images = models.ImageField(default='Choose Your Images')
    title = models.CharField(max_length=200,unique=True)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    post_viewcount = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=200, default='Enter SEO URL')
    status = models.IntegerField(choices=STATUS , default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title