from rest_framework import serializers

from elements.models import Element


class ElementSerializer(serializers.HyperlinkedModelSerializer):
    creation_date = serializers.ReadOnlyField()

    class Meta:
        model = Element
        fields = ('parent_group', 'image', 'name', 'description', 'creation_date')
