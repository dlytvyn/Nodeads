from django.db import models


class ElementManager(models.Manager):
    def get_queryset(self, *args, full_query=True, **kwargs):
        if full_query:
            return super().get_queryset(*args, **kwargs)
        return super().get_queryset(*args, **kwargs).filter(moderator_checked=True)
