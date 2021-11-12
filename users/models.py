from django.db import models

class User(models.Model):
    first_name          = models.CharField(max_length=40)
    last_name           = models.CharField(max_length=40)
    email               = models.EmailField(max_length=150, unique=True)
    password            = models.CharField(max_length=50)
    current_money       = models.FloatField(verbose_name='amount of initial money')
    current_money_unit  = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.id}. {self.email}'

    def _check_money_amount(self):
        return self.current_money