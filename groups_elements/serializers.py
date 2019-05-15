from rest_framework import serializers

from groups_elements.models import Element, Group


class GroupSerializer(serializers.ModelSerializer):
    number_of_child_groups = serializers.ReadOnlyField()
    number_of_child_elements = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = Group
        depth = 2
        fields = ('id', 'parent_group', 'image', 'name', 'description',
                  'number_of_child_groups', 'number_of_child_elements', 'elements', 'child_groups')


class ElementSerializer(serializers.HyperlinkedModelSerializer):
    creation_date = serializers.ReadOnlyField()

    class Meta:
        model = Element
        fields = ('parent_group', 'image', 'name', 'description', 'creation_date')
