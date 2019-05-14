from rest_framework import serializers

from groups.models import Group


class GroupSerializer(serializers.ModelSerializer):
    number_of_child_groups = serializers.ReadOnlyField()
    number_of_child_elements = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = Group
        depth = 2
        fields = ('id', 'parent_group', 'image', 'name', 'description',
                  'number_of_child_groups', 'number_of_child_elements', 'elements', 'child_groups')
