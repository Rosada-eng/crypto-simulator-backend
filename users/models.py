from django.db import models
from broker.models import Broker


class User(models.Model):
    first_name          = models.CharField(max_length=40)
    last_name           = models.CharField(max_length=40)
    email               = models.EmailField(max_length=150, unique=True)
    password            = models.CharField(max_length=50)
    initial_money       = models.FloatField(verbose_name='amount of initial money')
    initial_money_unit  = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.id}. {self.email}'

    def _check_money_amount(self):
        """ 
            Recebe o id do usuário e retorna quanto ele tem disponível
            em dólares (usd)
        """

        trades = Broker.objects.filter(user=self)

        actual_money = self.initial_money
        for trade in trades:
            # se quantity>0 (BUY), desconta o valor na carteira
            # se quantity<0 (SELL), incrementa o valor na carteira
            actual_money -= trade.unit_price * trade.quantity


        return actual_money