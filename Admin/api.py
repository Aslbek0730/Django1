from rest_framework import viewsets, permissions

from . import serializers
from . import models


class AdminViewSet(viewsets.ModelViewSet):
    """ViewSet for the Admin class"""

    queryset = models.Admin.objects.all()
    serializer_class = serializers.AdminSerializer
    permission_classes = [permissions.IsAuthenticated]
