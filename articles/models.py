from django.db import models
from users.models import User
from django.urls import reverse

class Article(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to = '%Y/%m/')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    like = models.ManyToManyField(User, related_name="like")
    
    def __str__(self) :
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse("article_detail_view", kwargs={"article_id": self.id})


class Comment(models.Model) :
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name="comment")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self) :
        return str(self.content)