from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .client_num_to_words import convert_to_word
from .serializers import NumberSerializer
from .constants import RESPONSE_OK, RESPONSE_ERROR

class ConvertionViewSet(GenericViewSet):

    """ViewSet for Person"""

    queryset = None
    serializer_class = NumberSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get', 'post'], url_path='num_to_english')
    def convertion_to_english(self, request):
        """
        Receive a number and convert into the english words
        """
        data = dict()
        if request.method == 'GET':
            data = { 'number': request.GET.get('number','')}
        else:
            data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            converted = convert_to_word(serializer.data['number'])
            return Response(
                data={
                    'status': RESPONSE_OK,
                    'num_in_english': converted
                },
                status=status.HTTP_200_OK
            )
        return Response(
            data={
                'status': RESPONSE_ERROR,
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
