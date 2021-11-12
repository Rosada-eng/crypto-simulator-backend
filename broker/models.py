from django.db import models

class Broker(models.Model):
    user        = models.ForeignKey('users.user', on_delete=models.CASCADE)
    crypto_id   = models.CharField(max_length=60)
    crypto_name = models.CharField(max_length=60)
    operation   = models.CharField(max_length=4)
    unit_price  = models.FloatField()
    unit        = models.CharField(max_length=10, default='usd')
    quantity    = models.FloatField()
    datetime    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.id} - {self.operation.upper()} {self.quantity} {self.crypto_id} * ' +
               f'{self.unit_price} {self.unit} at {self.datetime}')