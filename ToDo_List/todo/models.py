from django.db import models

# Create your models here.

class ToDo_List(models.Model):
    item=models.CharField(
        max_length=250,
        verbose_name='To-Do List',
        unique=True,
    )
    complated=models.BooleanField(
        default=False
    )
    def __str__(self):
        return self.item + ' | ' + str(self.complated)
    class Meta:
        verbose_name = 'To-Do List'
        verbose_name_plural = 'To-Do Lists'
    