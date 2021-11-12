from rest_framework import serializers
from .models import Broker

class BrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broker
        fields = ['id', 'user', 'crypto_id', 'crypto_name', 'operation', 'unit', 'unit_price', 'quantity', 'datetime']