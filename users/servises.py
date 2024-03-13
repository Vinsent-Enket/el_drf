import asyncio
import time

import stripe

from config import settings

stripe.api_key = settings.STRIPE_API_KEY


def get_payment_link(products_name, price):
    name = products_name
    stripe_product = stripe.Product.create(name=name)  # судя по документации можно сразу указать параметры для прайса, но у меня не вышло
    stripe_price = stripe.Price.create(currency="rub",
                                       unit_amount=price * 100,
                                       product=stripe_product['id']
                                       )
    stripe_session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": stripe_price['id'], "quantity": 1}], mode="payment", )
    return stripe_session


def get_session_status(stripe_session_id):
    status = stripe.checkout.Session.retrieve(stripe_session_id)
    return status['payment_status']

# test_product = stripe.Product.create(name='Test_product')
#
# test_price = stripe.Price.create(currency="rub",
#                                  unit_amount=333 * 100,
#                                  product=test_product['id']
#                                  )
#
# test_session = stripe.checkout.Session.create(
#     success_url="https://example.com/success",
#     line_items=[{"price": test_price['id'],  "quantity": 1}], mode="payment",)
#
#
# print(test_session)
