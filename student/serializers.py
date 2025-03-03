from rest_framework import serializers

from . import models


class studentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.student
        fields = [
            "created",
            "last_updated",
        ]
