from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .brokerDB import *
from .serializers import BrokerSerializer

@api_view(['GET'])
def get_trades(request, user_id):
    """ 
        API que devolve as transações de um usuário
    """
    try:
        trades = get_trades_from_user(user_id)
        serialized_trades = BrokerSerializer(trades, many=True)
        
        return Response(serialized_trades.data)

    except Broker.DoesNotExist:
        raise Http404()

@api_view(['POST'])
def make_trade(request):
    """
        API que chama o método para gerar novas transações:
        
            body = {
                -- required -- 
                "user_id": any,
                "crypto_id": any,
                "crypto_name": any,
                "unit_price": float,
                "quantity": int(+ | -),
            }

    """

    trade = new_trade(**request.data)
    serialized_trade = BrokerSerializer(trade)
    return Response(serialized_trade.data)