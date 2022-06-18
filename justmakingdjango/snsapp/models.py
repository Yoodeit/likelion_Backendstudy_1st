from django.db import models

# 게시물 모델

class Model1forUpload(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Model1forComment(models.Model):
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    foreign_key = models.ForeignKey(Model1forUpload,null=True, blank=True, on_delete=models.CASCADE )

    def __str__(self):
        return self.comment