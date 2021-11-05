from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .userDB import *
from .serializers import UserSerializer

@api_view(['GET', 'POST'])
def get_user(request, user_id):
    """ 
        @GET:
        Devolve os dados de um usuário.
        @POST:
        Altera os dados de um usuário.
        Formato do body esperado para post:
        body = {
            ...
            new_<nome do campo com alteração>: str,
            ...
        }
        #TODO: Validar se quem está pedindo as alterações é o próprio usuário
    """
    if request.method == 'GET':
        try:
            user = User.objects.get(id=user_id)
            serialized_user = UserSerializer(user)

            return Response(serialized_user)

        except User.DoesNotExist:
            raise Http404()

    elif request.method == 'POST':
        try:
            edited_user = edit_profile(user_id, **request.body)
            return edited_user
        except User.DoesNotExist:
            raise Http404()


@api_view(['POST'])
def create_new_user(request):
    """ 
        API que cria um novo usuário no banco de dados
        TODO: criar autenticação e password

        Formato do body esperado para post:
        body = {
            (req) - first_name: str, last_name: str, email: str,
            (opcional) - initial_money: int, birth_date: date 
        }
    """
    user = new_user(**request.body)
    return user

@api_view(['POST'])
def delete_user(request, user_id):
    """ 
        API que deleta um usuário no banco de dados
    """
    result = delete_user(user_id)
    return result

        