from rest_framework import viewsets, permissions

from . import serializers
from . import models


class studentViewSet(viewsets.ModelViewSet):
    """ViewSet for the student class"""

    queryset = models.student.objects.all()
    serializer_class = serializers.studentSerializer
    permission_classes = [permissions.IsAuthenticated]
