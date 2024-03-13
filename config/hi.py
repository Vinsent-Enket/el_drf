import stripe

from config import settings

stripe.api_key = settings.STRIPE_API_KEY


def create_product(product):
    name = product.name
    description = product.description

def create_price(amount):
    return stripe.Price.create()




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
