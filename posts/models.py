from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile


# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=400)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)


class Post(models.Model):
    image = models.FileField(upload_to='post-images/', null=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    created_data = models.DateField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    like = models.ForeignKey(Like, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.description[:20]

    class Meta:
        db_table = 'posts'