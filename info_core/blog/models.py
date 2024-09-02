from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
    def __str__(self):
        return self.name
class Hashtag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Хештеги'
        verbose_name = 'Хештег'
    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=800)
    description = models.TextField(default=True)
    image = models.ImageField()
    is_active = models.BooleanField()
    created_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    hashtags = models.ManyToManyField(Hashtag, default=True)

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'

class PublicationComment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)


class ContactClient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=130)
    message = models.TextField()
