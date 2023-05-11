from .models import currency
import json
from django.db.utils import IntegrityError
import pprint


def update_currency(json_data):
    # set the data passed in to variable data
    data = json.loads(json_data)
    # take the length of the list and subtract 1 to use this as an index
    index = len(data) - 1 
    names = []
    # take the names from the data and append it to the empty list we initialized above
    for num in range(0,(index + 1)):
        name = data[num]['name']
        names.append(name)
    
    # if a coin already exists within the database, then we will delete the coin before we add the new coin in 
    items = currency.objects.filter(name__in = names).delete()
    try:
        while index >= 0: 
            cryptocurrency = currency()
            crypto = data[index]
            cryptocurrency.name = crypto['name']
            cryptocurrency.rank = crypto['rank']
            cryptocurrency.volume24= round(float(crypto['volume24']),2)
            cryptocurrency.ticker = crypto['ticker']
            cryptocurrency.price = round(float(crypto['priceUsd']),2)
            cryptocurrency.save()
            index = index - 1 
    except IntegrityError as e:
        print(e, crypto)





