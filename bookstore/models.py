from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books',
    )
    image = models.ImageField(upload_to='covers/', null=True, blank=True)
    file = models.FileField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.author})"