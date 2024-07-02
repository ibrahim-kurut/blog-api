from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Post(models.Model):

    STATUS = (
    (0, 'Draft'),
    (1, 'Published'),
    )


    title = models.CharField(max_length=200)
    content = models.TextField(null=True, default="content")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    status = models.PositiveIntegerField(choices=STATUS, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.status}"
