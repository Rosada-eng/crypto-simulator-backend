from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import Http404
from .userDB import *
from .serializers import UserSerializer

@api_view(['GET'])
def get_user(request, user_email):
    """ 
        @GET:
        Devolve os dados de um usuário. Faz o matching pelo e-mail
        """

    try:
        user = User.objects.get(email=user_email)
        serialized_user = UserSerializer(user)

        return Response(serialized_user.data)

    except User.DoesNotExist:
        raise Http404()

@api_view(['POST'])
def edit_user(request, user_id):
    """
        @POST:
        Altera os dados de um usuário. Faz o matchin pelo _id
        Formato do body esperado para post:
        body = {
            ...
            new_<nome do campo com alteração>: str,
            ...
        }
    """
    try:
        edited_user = edit_profile(user_id, **request.data)
        serialized_user = UserSerializer(edited_user)
        return Response(serialized_user.data)
    except User.DoesNotExist:
        raise Http404()

@api_view(['POST'])
def trade_money_to_account(request, user_id):
    """ 
        @POST:
        Depoista (money_amount > 0) ou Retira (money_amount < 0) dinheiro da conta do usuário

        body = {
            amount: float,
        }
    """
    requested_amount = request.data.get('amount')
    try:
        new_user = trade_money(user_id = user_id, money_amount = requested_amount)
        serialized_user = UserSerializer(new_user)
        return Response(serialized_user.data)

    except User.DoesNotExist:
        raise Http404()

@api_view(['POST'])
def create_new_user(request):
    """ 
        API que cria um novo usuário no banco de dados
        TODO: criar autenticação e password

        Formato do body esperado para post:
        body = {

            -- required --
            "first_name": str,
            "last_name": str,
            "email": str,
            "password": str,

            -- optional --
            "current_money": int,
        }
    """
    print(request.data)
    user = new_user(**request.data)

    serialized_user = UserSerializer(user)
    return Response(serialized_user.data)

@api_view(['POST'])
def remove_user(request, user_id):
    """ 
        API que deleta um usuário no banco de dados
    """
    try:
        print("user_id = ", user_id)
        result = delete_user(user_id)
        print("r=",result)
        return Response(data = {'deleted': True}, status=status.HTTP_200_OK)

    except:
        raise Http404()
