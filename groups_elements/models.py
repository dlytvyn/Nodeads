from django.db import models

from groups_elements.manager import ElementManager


class Group(models.Model):
    parent_group = models.ForeignKey('Group', on_delete=models.CASCADE, blank=True, null=True, related_name='child_groups')
    image = models.ImageField('img', upload_to='groups_images/')
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=512, blank=True)

    @property
    def number_of_child_elements(self):
        return self.elements.count()

    @property
    def number_of_child_groups(self):
        return self.child_groups.count()

    def __str__(self):
        return str(self.name)


class Element(models.Model):
    parent_group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='elements')
    image = models.ImageField('img', upload_to='elements_images/')
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=512, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    moderator_checked = models.NullBooleanField(default=None, null=False, verbose_name='Checked by moderator')
    objects = ElementManager()

    def __str__(self):
        return str(self.name)
