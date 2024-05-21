import stripe
import os
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

price = os.getenv('PRICE')
if price is None or price == '':
    print('You must set a Price ID in .env. Please see the README.')
    exit(0)

# setup stripe 
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

def index(request):
    return render(request, "donatetemplates/index.html")

@csrf_exempt
def charge(request):
    if(request.method == "POST"):
        quantity = request.POST.get('coffee_input')
        DOMAIN = os.getenv('DOMAIN')
        print(DOMAIN + '/success.html')
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url = DOMAIN + '/success.html',
                cancel_url = DOMAIN + '/canceled.html',
                mode = 'payment',
                line_items = [{
                    'price': os.getenv('PRICE'),
                    'quantity': quantity,
                }]
            )
            print('aqui')
            print(checkout_session)
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            print(e)
            return HttpResponse("Charge problem")
        
def success(request): 
    return HttpResponse("Success")

def cancel(request):
    return HttpResponse("Cancel")