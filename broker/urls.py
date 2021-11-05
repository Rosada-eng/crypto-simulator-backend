from django.urls import path

from . import views

urlpatterns = [
    #<> Rotas para API:
    # Retorna as transações de um usuário
    path('broker/<int:user_id>/', views.get_trades, name='get_trades_from_user'),
    
    # Faz novas transações -- Dados necessários são passados pelo body do request (userId, cryptoId, unit_price, quantity, unit)
    path('broker/', views.make_trade, name='new_trade')
]
