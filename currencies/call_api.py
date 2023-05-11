import requests 
import pprint
import json

# Start with out api endpoint and the parameters 
# in this case the only parameter we really need is the id, which will be the name of the coin(s)
api_endpoint = "http://api.coincap.io/v2/assets"




def latest_news_page():
    api_endpoint = "https://www.cryptopanic.com/api/v1/posts/"

    params = {
        'auth_token': '59f1577dc7d9d5966929a053ab71598708bbbd25',
        'currencies': 'BTC',
        'kind': 'news'
    }

    response = requests.get(api_endpoint, params=params)
    all_stories = response.json()['results']
    return all_stories


def landing_page_api():
    params = {
        'limit': 8
    }
    response = requests.get(api_endpoint, params = params)
    data = response.json()
    coins = data['data']
    index = len(coins) - 1
    start = 0
    lst = []
    while start <= index:
        coin_data = {}
        coin_data['name'] = coins[start]['name']
        coin_data['priceUsd'] = round(float(coins[start]['priceUsd']),4)
        coin_data['ticker'] = coins[start]['symbol']
        coin_data['rank'] = coins[start]['rank']
        coin_data['volume24'] = round(float(coins[start]['volumeUsd24Hr']))
        lst.append(coin_data)
        start = start + 1 
    return lst

def selected_coins_api_call(coin):
    params = {
            'ids': coin
        }

# now make a request to the api endpoint, with a params as an argument
# saving the response in a variable called response
# the data we will want is the json part of the response. store that in a variable called data
# the returned data will contain a dictionary with a key "data" and value of a list
# we want only the list so we index ['data']
    response = requests.get(api_endpoint, params=params)
    data = response.json()['data']

# initialized an emppty list to return
# set our index to the length of the list, so we know we are indexing through every item in the 
# dictionary

    return_data = []
    index = len(data) - 1
    start = 0
# while loop to make sure to only index the total number of items in the list
# grab only the keys we want to return back to the user 
# intialize an empty dictionary, since each dictionary can only contain a unique key 
# every time this loop is run, we append that dictionary to the list, and start with an empty
# dictionary to then retrieve the specific keys for that coin until the loop meets its condition
# to end 
    while start <= index:
        values = {}
        coins = data[start]
        values['name'] = coins['name']
        values['ticker'] = coins['symbol']
        values['priceUsd'] = round(float(coins['priceUsd']),4)
        values['rank'] = int(coins['rank'])
        values['volume24'] = round(float(coins['volumeUsd24Hr']),2)
        return_data.append(values)
        start = start + 1
    data  = json.dumps(return_data)
    return data

