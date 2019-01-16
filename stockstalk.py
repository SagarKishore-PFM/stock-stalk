import requests
from bs4 import BeautifulSoup


# TODO:
#   CLI option to add products
#   Store products in a json file or db instead of hard code
#   Maybe a table to display results?
#   Open url on browser if available?
#   Add a handler for Amazon, Flipkart, etc


def stalk(products):
    for pdt in products:
        handlers[pdt[-1]](pdt)


def armyourdesk_handler(pdt):
    name, url, website = pdt
    r = requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    div = soup.find('div', attrs={'id': 'product-ex-action'})
    stock_label = div.find('span', attrs={'class': 'stock'}).text
    sold_out = div.find('div', attrs={'class': 'sold-out'})
    if stock_label == 'Out Stock' and sold_out:
        print(f"Sorry... {name} is still out of stock")
    else:
        print(f"**** {name} is now available! ****")
    return div


handlers = {
    'armyourdesk': armyourdesk_handler,
}

products = [
    (
        "Drevo Calibur White Mechanical Keyboard",
        "https://www.armyourdesk.com/products/drevo-calibur-71-key-rgb-led-backlit-wireless-bluetooth-4-0-mechanical-keyboard-white",
        "armyourdesk",
    ),
    (
        "Drevo Calibur Black Mechanical Keyboard",
        "https://www.armyourdesk.com/products/drevo-calibur-71-key-rgb-led-backlit-wireless-bluetooth-4-0-mechanical-keyboard-black",
        "armyourdesk",
    ),
    (
        "Drevo Tryfing Black Mechanical Keyboard",
        "https://www.armyourdesk.com/collections/usb-wired/products/drevo-tyrfing-v2-87-key-rgb-backlit-mechanical-gaming-keyboard-ansi-us-layout",
        "armyourdesk",
    ),
    ]

a = stalk(products)
