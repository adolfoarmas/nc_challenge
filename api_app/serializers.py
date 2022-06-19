from rest_framework import serializers
from base_app.models import Payable, Transaction

class PayableSerializer(serializers.ModelSerializer):
    """
    Sender of serialized Payable Model data, used by create/POST function
    """
    class Meta:
        model = Payable
        fields = '__all__'

class PayablePendingSerializer(serializers.ModelSerializer):
    """
    Sender of serialized Payable Model data, used by list/GET function
    """
    class Meta:
        model = Payable
        fields = [
                'bar_code',
                'service_type',
                'due_date',
                'service_cost'
                ]

    def to_representation(self, instance):
        """
        overwrited function to eliminate de service_type field if it is
        requested in the url
        """
        response_data = super().to_representation(instance)
        request_data = self.context.get('request', None)
        is_a_service_type_filter = request_data.query_params.get('service_type')
        if is_a_service_type_filter:
            response_data.pop('service_type')
        return response_data


class TransactionSerializer(serializers.ModelSerializer):
    """
    Sender of serialized Payable Model data, used by list/GET function 
    """
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate(self, attrs):
        print(attrs)
        payment_method = attrs['payment_method']
        card_number = attrs['card_number']
        if  payment_method == 'CC' or payment_method == 'DC':
            if not card_number:
                raise serializers.ValidationError({'card_number':'Introduce card_number parameter'})
        return super().validate(attrs)

class TotalsSerializer(serializers.Serializer):
    """
    Utilitary serializer to group daily transactions by payment_date
    totalize the daily payment_ammount and the number of transactions
    """
    payment_date = serializers.DateField()
    sum_payment_ammount = serializers.DecimalField(max_digits=12, decimal_places=2)
    total_transaction_ids = serializers.IntegerField()


