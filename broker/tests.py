from django.test import TestCase
from users.userDB import *
from broker.brokerDB import *

class BrokerTestCase(TestCase):
    def setUp(self):
        new_user(
            first_name='Guilherme',
            last_name='Teste',
            email='gui_rosada@hotmail.com',
        )
    def test_transaction(self):
        user = User.objects.get(email="gui_rosada@hotmail.com")
        # Trades: 1 BUY | 1 SELL
        new_trade(user.id, crypto_id='btc', unit_price=100, quantity=20)
        new_trade(user.id, crypto_id='btc', unit_price=90, quantity=-5)

        trades = get_trades_from_user(user_id=user.id)
        self.assertEqual(len(trades), 2)

        # a transação mais recente deve ser do tipo 'sell'
        self.assertEqual(trades[0].operation, 'sell')

        # Checa quantia atual de dinheiro
        actual_money = user._check_money_amount()
        self.assertEquals(actual_money, user.current_money)


    def test_invalid_transaction(self):
        user = User.objects.get(email="gui_rosada@hotmail.com")
        # Tenta comprar uma ação com valor maior que a quantia atual
        with self.assertRaises(Exception) as context:
            new_trade(user.id, crypto_id='btc', unit_price=1000000, quantity=10)

        self.assertTrue('Money amount is not enough' in str(context.exception))
 