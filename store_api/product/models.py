from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255, blank=True, null=True)
    colors = models.ManyToManyField('Color')
    sizes = models.ManyToManyField('Size')

    def __str__(self):
        return self.title
