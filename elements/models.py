from django.db import models

from groups.models import Group


class ElementManager(models.Manager):
    def get_queryset(self, *args, full_query=False, **kwargs):
        if full_query:
            return super().get_queryset(*args, **kwargs)
        return super().get_queryset(*args, **kwargs).filter(moderator_checked=True)


class Element(models.Model):
    parent_group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='elements')
    image = models.ImageField('img', upload_to='elements_images/')
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    moderator_checked = models.BooleanField(default=None, null=True)
    objects = ElementManager()
