from rest_framework import serializers

from .models import BoardModel


class BoardModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardModel
        fields = '__all__'  # 또는 ['id', 'name', 'description']