import requests
import sys

if len(sys.argv) != 2:
    sys.exit('Please enter a single argument')
try:
    number = float(sys.argv[1])
except ValueError:
    sys.exit('Enter a postive real number or 0')

r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = r.json()
price = float(data['bpi']['USD']['rate'].replace(',', ''))

print(f'{number * price:,.4f}')



