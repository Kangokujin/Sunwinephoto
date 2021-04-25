from django.db import models


class Category(models.Model):

    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default=''
    )

    slug = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default=''
    )

    order = models.IntegerField(
        null=False,
        default=0
    )

    image = models.ImageField(
        upload_to="images/category/"
    )

    def __str__(self):
        return f'{self.order} - {self.title}'


class Photo(models.Model):

    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default=''
    )

    description = models.TextField(
        default='',
        null=False,
        blank=False
    )

    category = models.ForeignKey(
        Category,
        null=True,
        blank=False,
        default=None,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to="images/photo/"
    )

    def __str__(self):
        return self.title

