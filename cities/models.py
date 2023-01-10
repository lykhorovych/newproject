from django.db import models
from django.shortcuts import reverse


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Місто')

    class Meta:
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'
        ordering = ('-id',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('city', args=(self.pk,))
