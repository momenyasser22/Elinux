import requests

def find_largest_item(lst):
    largest = lst[0]  # Assume the first item is the largest

    for item in lst:
        if item > largest:
            largest = item

    return largest

# Example usage
my_list = [5, 9, 3, 1, 7, 2]
largest_item = find_largest_item(my_list)
print("The largest item in the list is:", largest_item)

#BITCON 

def get_bitcoin_rate():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()
    rate = data["bpi"]["USD"]["rate"]

    return rate

# Example usage
bitcoin_rate = get_bitcoin_rate()
print("The current Bitcoin rate is:", bitcoin_rate)