from django.db import models


class Group(models.Model):
    parent_group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, blank=True, null=True, related_name='child_groups')
    image = models.ImageField('img', upload_to='groups_images/')
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, blank=True)

    @property
    def number_of_child_elements(self):
        return self.elements.count()

    @property
    def number_of_child_groups(self):
        return self.child_groups.count()
