""" 
    >>BROKER
    Métodos para manipular o banco de dados da coleção Broker
"""
from .models import Broker
from users.models import User

def get_trades_from_user(user_id, crypto_id=None):
    user = User.objects.get(id = user_id)
    if crypto_id is not None:
        trades = Broker.objects.filter(user = user, crypto_id=crypto_id).order_by('-datetime')
    else:
        trades = Broker.objects.filter(user = user).order_by('-datetime')

    return trades

def new_trade (user_id, crypto_id, crypto_name, unit_price, quantity, unit:str='usd'):
    if quantity > 0 : 
        operation = 'buy'
    elif quantity == 0:
        raise Exception("Can't trade 0 amount of cryptocurrencies")
    else:
        operation = 'sell'

    # Checa se o usuário tem dinheiro o suficiente para realizar a transação
    user = User.objects.get(id=user_id)
    user_current_money = user._check_money_amount()

    if operation == 'buy' and (user_current_money >= float(unit_price) * float(quantity)):
        trade = Broker.objects.create(
            user = user,
            crypto_id = crypto_id, 
            crypto_name = crypto_name,
            operation = operation,
            unit_price = unit_price, 
            unit = unit, 
            quantity = quantity
        )

        user.current_money -= float(unit_price) * float(quantity)
        user.save()
        return trade
    #! OBS.: Vendas possuem quantity negativas!!
    elif operation == 'sell':
        user_trades = Broker.objects.filter(user_id = user_id, crypto_id = crypto_id)
        user_crypto_amount = 0

        for trade in user_trades:
            print(trade)
            user_crypto_amount += trade.quantity

        print("crypto_amount: ", user_crypto_amount)
        if user_crypto_amount >= float(abs(quantity)):
            trade = Broker.objects.create(
            user = user,
            crypto_id = crypto_id, 
            crypto_name = crypto_name,
            operation = operation,
            unit_price = unit_price, 
            unit = unit, 
            quantity = quantity
        )

            user.current_money -= float(unit_price) * float(quantity)
            user.save()
            return trade
        else:
            raise Exception('You dont have enough to sell')

    else:
        raise Exception('Money amount is not enough')