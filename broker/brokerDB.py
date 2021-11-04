""" 
    >>BROKER
    Métodos para manipular o banco de dados da coleção Broker
"""
from django.core.checks.messages import Error
from .models import Broker
from users.models import User

def get_trades_from_user(user_id, crypto_id=None):
    user = User.objects.get(id = user_id)
    if crypto_id is not None:
        trades = Broker.objects.filter(user = user, crypto_id=crypto_id).order_by('-datetime')
    else:
        trades = Broker.objects.filter(user = user).order_by('-datetime')

    return trades

def new_trade (user_id, cripto_id, unit_price:float, quantity:float, unit:str='usd'):
    if quantity > 0 : 
        operation = 'buy'
    elif quantity == 0:
        Error("Can't trade 0 amount of cryptocurrencies")
    else:
        quantity = 'sell'

    # Checa se o usuário tem dinheiro o suficiente para realizar a transação
    user = User.objects.get(id=user_id)
    user_current_money = user._check_money_amount()

    if user_current_money >= unit_price * quantity:
        trade = Broker.objects.create(
            cripto_id = cripto_id, 
            operation = operation,
            unit_price = unit_price, 
            unit = unit, 
            quantity = quantity
        )
        return trade
    else:
        return Error('Money amount is not enough')