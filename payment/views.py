from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dotenv import load_dotenv, dotenv_values
from cart.cart import Cart
import stripe

KEYS = dotenv_values(".env")


@login_required
def payment_summary(request):
    cart = Cart(request)
    total = int(
        str(cart.get_total()).replace(".", "")
    )  # stripe does not take floats or decimals, remove .
    # build payment intent
    stripe.api_key = KEYS["STRIPE_SK"]

    intent = stripe.PaymentIntent.create(
        amount=total, currency="usd", metadata={"userid": request.user.id}
    )

    return render(
        request=request,
        template_name="payment/checkout.html",
        context={"client_secret": intent.client_secret},
    )
