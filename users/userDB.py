""" 
    <> USER
    Métodos para manipular o banco de dados da coleção User
"""
from .models import User
from broker.models import Broker

#! New user
def new_user(first_name, last_name, email, password, current_money:int=10000):
    user = User.objects.create(
        first_name=first_name, last_name=last_name,email=email,password=password,
        current_money=current_money,current_money_unit='usd'
        )
    #TODO: add password

    return user

#! Edit some field (name | email | password)
def edit_profile(user_id, new_first_name=None, new_last_name=None,
                new_email=None,new_password=None):
    user = User.objects.get(id=user_id)
    if new_first_name is not None and new_first_name != user.first_name:
        user.first_name = new_first_name
    if new_last_name is not None and new_last_name != user.last_name:
        user.last_name = new_last_name
    if new_email is not None and new_email != user.email:
        user.email = new_email
    if new_password is not None and new_password != user.password:
        user.password = new_password


    user.save()
    return user

def trade_money(user_id, money_amount):
    user = User.objects.get(id=user_id)
    # Depósito
    if float(money_amount) > 0:
        user.current_money += float(money_amount)
    # Saques
    elif float(money_amount) < 0 and float(money_amount) <= user.current_money:
        user.current_money += float(money_amount)
    # Saques sem fundo
    else:
        raise Exception('You dont have money enough to withdraw')

    user.save()
    return user

#! Delete user
def delete_user(user_id):
    result = User.objects.delete(id=user_id)
    return result

#TODO: Trocar InitialMoney por CurrentMoney
#TODO: Adicionar opção de Depositar/Retirar dinheiro
#TODO: Ao realizar Trade, alterar CurrentMoney

# def check_for_partial_profit(user_id, current_usd_value):
#     #! FRONTEND --> precisa chamar API externa para pegar o valor atual de cada criptomoeda
#     """ 
#         Recebe o id do usuário e o valor atual do dolar.
#         Busca cada uma das transações e checa o lucro parcial 
#         da quantidade líquida de cada criptomoeda

#         > lucro = -Σ(custos de compra) + Σ(preços de vendas) + Σ(preço atual)
        
#     """

#     user = User.objects.get(id=user_id)
#     trades = Broker.objects.filter(user=user)
    
#     purchases   = 0
#     sales       = 0
#     forecast    = 0

#     profit = 0
#     for trade in trades:




    
#     # Checar quantidade líquida de cada moeda.
#     # Se alguma for > 0, checa a variação
#     # Checa data do trade 'sell':
#         # se data < today:
#             # - Contabiliza valor do dolar na época

#     return profit