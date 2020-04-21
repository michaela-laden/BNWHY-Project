from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')

    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
        k = self.parent

class Post(models.Model):
    title = models.CharField(max_length = 100)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)   #Sets posts created time/date
    author = models.ForeignKey(User, on_delete=models.CASCADE) #If a user is deleted then their posts are deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts-detail', kwargs={'pk':self.pk})

    def get_cat_list(self):
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    