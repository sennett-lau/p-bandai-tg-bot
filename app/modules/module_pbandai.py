import requests
from bs4 import BeautifulSoup

def get_item_availability(item_id):
    item_url = 'https://p-bandai.com/hk/item/'

    combine_url = item_url + item_id

    try:

        response = requests.get(combine_url)

        soup = BeautifulSoup(response.text, 'html.parser')

        # get the h1 with class o-product__name
        product_name = soup.find('h1', {'class': 'o-product__name'}).text

        # get the button with the id addToCartButton
        button = soup.find('button', {'id': 'addToCartButton'})

        # check if the button is disabled
        if button.has_attr('disabled'):
            return {
                'name': product_name,
                'is_available': False
            }

        return {
            'name': product_name,
            'is_available': True
        }
    except Exception as e:
        print(e)
        return {
            'name': '',
            'is_available': False
        }
    pass