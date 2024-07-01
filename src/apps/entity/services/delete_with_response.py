from django.http import HttpResponse
from rest_framework import status

from ..models import CoordinateEntity


def get_delete_response(self):
    try:
        result = delete_with_response(self)
        return HttpResponse(result, status=status.HTTP_200_OK)
    except Exception as e:
        return HttpResponse(str(e), status=status.HTTP_400_BAD_REQUEST)


def delete_with_response(self):
    pk = self.kwargs['pk']
    instance = CoordinateEntity.objects.get(pk=pk)
    instance.delete()
    return pk