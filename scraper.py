import random
import requests
from bs4 import BeautifulSoup

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
]

def get_headers():
    return {"User-Agent": random.choice(USER_AGENTS)}

def scrape_amazon(product):
    search_url = f"https://www.amazon.in/s?k={product.replace(' ', '+')}"
    headers = get_headers()
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        try:
            title = soup.find("span", {"class": "a-size-medium"}).text
            price = soup.find("span", {"class": "a-price-whole"}).text
            return {"site": "Amazon", "title": title, "price": float(price.replace(",", ""))}
        except AttributeError:
            return {"site": "Amazon", "error": "Product not found"}
    else:
        print(f"Failed to fetch Amazon data, status code: {response.status_code}")
        return {"site": "Amazon", "error": "Request failed"}

def scrape_flipkart(product):
    search_url = f"https://www.flipkart.com/search?q={product.replace(' ', '%20')}"
    headers = get_headers()
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        try:
            title = soup.find("a", {"class": "_1fQZEK"}).text.strip()
            price = soup.find("div", {"class": "_30jeq3"}).text.replace("₹", "").replace(",", "")
            return {"site": "Flipkart", "title": title, "price": price}
        except AttributeError:
            return {"site": "Flipkart", "error": "Product not found"}
    else:
        print(f"Failed to fetch Flipkart data, status code: {response.status_code}")
        return {"site": "Flipkart", "error": "Request failed"}

def scrape_snapdeal(product):
    search_url = f"https://www.snapdeal.com/search?keyword={product.replace(' ', '%20')}"
    headers = get_headers()
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        try:
            title = soup.find("p", {"class": "product-title"}).text.strip()
            price = soup.find("span", {"class": "lfloat product-price"}).text.replace("₹", "").replace(",", "")
            return {"site": "Snapdeal", "title": title, "price": price}
        except AttributeError:
            return {"site": "Snapdeal", "error": "Product not found"}
    else:
        print(f"Failed to fetch Snapdeal data, status code: {response.status_code}")
        return {"site": "Snapdeal", "error": "Request failed"}

def scrape_meesho(product):
    search_url = f"https://www.meesho.com/search?q={product.replace(' ', '%20')}"
    headers = get_headers()
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        try:
            title = soup.find("p", {"class": "ProductName"}).text.strip()
            price = soup.find("span", {"class": "ProductPrice"}).text.replace("₹", "").replace(",", "")
            return {"site": "Meesho", "title": title, "price": price}
        except AttributeError:
            return {"site": "Meesho", "error": "Product not found"}
    else:
        print(f"Failed to fetch Meesho data, status code: {response.status_code}")
        return {"site": "Meesho", "error": "Request failed"}

def get_prices(product):
    prices = [
        scrape_amazon(product),
        scrape_flipkart(product),
        scrape_snapdeal(product),
        scrape_meesho(product),
    ]
    print(f"Prices fetched: {prices}")  # Debug statement to show all results

    valid_prices = [p for p in prices if "price" in p]
    if valid_prices:
        lowest_price = min(valid_prices, key=lambda x: x["price"])
        return {"product": product, "best_price": lowest_price}
    else:
        return {"error": "No valid prices found"}
