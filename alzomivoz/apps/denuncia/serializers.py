from rest_framework import serializers
from .models import Denuncia


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Denuncia
        fields = ('titulo', 'imagen', 'autor')
