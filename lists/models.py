from django.db import models
# from django.template.defaultfilters import default
# from django.urls import reverse

# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=30, default='')

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

    def __str__(self):
        return self.name


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.PROTECT)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text
