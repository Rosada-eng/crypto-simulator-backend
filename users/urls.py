from django.urls import path

from . import views

urlpatterns = [
    #<> Rotas para API:
    # GET   -- retorna os dados de um usuário
    # POST  -- permite editar os campos de um usuário 
    #TODO: autenticar se foi o próprio usuário quem solicitou as mudanças
    path('user/<str:user_email>/', views.get_user, name='get_or_edit_user'),

    # Cria um novo usuário
    path('new_user/', views.create_new_user, name='create_user'),
    
    # Edita os dados de um usuário
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),

    # Transfere dinheiro para a conta
    path('trade_to_account/<int:user_id>/', views.trade_money_to_account, name='trade_money_to_account'),

    # Deleta um usuário
    path('remove_user/<int:user_id>/', views.remove_user, name='remove_user'),

]