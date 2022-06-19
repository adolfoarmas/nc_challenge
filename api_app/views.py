from itertools import count
from datetime import datetime
from venv import create
from django.db import models
from xml.etree.ElementPath import prepare_self
from rest_framework import status, viewsets, serializers
from rest_framework.response import Response
from base_app.models import Payable, Transaction
from .serializers import PayableSerializer, PayablePendingSerializer, TransactionSerializer, TotalsSerializer

class PayableViewSet(viewsets.ViewSet):
    """ 
    End Point to lists the total number of "Pending status" payables ordered by due_date.
    If service_type comes in the URL (i.e.: http://127.0.0.1:8000/payables/?service_type=COM)
    a filter is applied to the objects to show only payables with this parameter.

    POST function also available passing json:
    i.e:

    {
        "bar_code": "123456789016",
        "service_type":"COM",
        "service_description":"Internet Service June",
        "due_date": "2022-07-05",
        "service_cost": "60.5",
        "payment_status": "PG"
    }

    """

    #serializer_class = PayableSerializer

    def list(self, request):

        queryset = Payable.objects.filter(payment_status='PG').order_by('-due_date')
        url_parameter = request.query_params.get('service_type')

        if url_parameter:
            queryset = queryset.filter(service_type=url_parameter)


        serializer = PayablePendingSerializer(queryset, many=True, context={'request': request})
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response

    def create(self, request, *args, **kwargs):
        serializer = PayableSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response


class TransactionViewSet(viewsets.ViewSet):

    """
    End Point to lists the total number of transactions ordered by transaction_id.
    If date_min and date_max comes in the URL (i.e.: http://127.0.0.1:8000/payables/??date_min=2020-06-18&date_max=2022-03-18)
    a filter is applied to the objects and the Sum of payment_ammount and the Count of total_transaction_ids
    by day will be returned in a unique register.

    POST function also available passing json:
    i.e:

    {
    "bar_code":"123456789016",
    "payment_method":"DC",
    "card_number":"5572883244125698",
    "payment_ammount":"3956.45",
    "payment_date":"2022-06-18"
    }
    """

    def list(self, request):
        queryset = Transaction.objects.all().order_by('-transaction_id')

        #Complete list of transactions
        serializer = TransactionSerializer(queryset, many=True)

        date_min = request.query_params.get('date_min')
        date_max = request.query_params.get('date_max')
        
        if date_min or date_max:
            if self.date_parameters_custom_validation(date_min, date_max):
                queryset = (Transaction.objects.filter(payment_date__range=(date_min, date_max))
                .values('payment_date')
                .annotate(sum_payment_ammount=models.Sum('payment_ammount'), total_transaction_ids=models.Count('transaction_id'))
            )
                #Transactions Filtered by date_min and date_max
                serializer = TotalsSerializer(queryset, many=True)

        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response

    def create(self, request, *args, **kwargs):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response

    def date_parameters_custom_validation(self, date_min, date_max):

        if not date_min or not date_max:
            raise serializers.ValidationError({'date_parameters': 'introduce both arguments values date_min and date_max'})
            
        str_date_min = str(date_min)
        str_date_max = str(date_max)

        format = "%Y-%m-%d"

        try:
            datetime.strptime(str_date_min, format)
        except ValueError:
            raise serializers.ValidationError({'date_parameters': 'verify date format of date_min, must be YYYY-MM-dd'})
        try:
            datetime.strptime(str_date_max, format)
        except ValueError:
            raise serializers.ValidationError({'date_parameters': 'verify date format of date_max, must be YYYY-MM-dd'})
        if date_min > date_max:
            raise serializers.ValidationError({'date_parameters': 'introduce date_min not mayor than date_max'})
        
        return True
