from rest_framework import serializers, viewsets

from ..models import CoordinateEntity
from .label import LabelSerializer
from ..services import get_delete_response, create_with_m2m, update_with_m2m


class CoordinateEntitySerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True)

    def create(self, validated_data):
        return create_with_m2m(self, validated_data)

    def update(self, instance, validated_data):
        return update_with_m2m(self, instance, validated_data)

    class Meta:
        model = CoordinateEntity
        fields = '__all__'


class CoordinateEntityViewSet(viewsets.ModelViewSet):
    serializer_class = CoordinateEntitySerializer
    queryset = CoordinateEntity.objects.all()

    def destroy(self, request, *args, **kwargs):
        return get_delete_response(self)
