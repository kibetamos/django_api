# from core.abstract.serializers import AbstractSerializer
# from core.user.models import User


from rest_framework import serializers


class AbstractSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
# class UserSerializer(AbstractSerializer):
#     class Meta:
#         model = User
#         # List of all the fields that can be included in a request or a response
#         fields = ['id', 'username', 'first_name', 'last_name', 'bio', 'avatar', 'email', 'is_active',
#                   'created', 'updated']
#         # List of all the fields that can only be read by the user
#         read_only_field = ['is_active']