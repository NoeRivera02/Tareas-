import requests

url = "https://www.theodmgroup.com"

headers = {
    'x-rapidapi-host': "http://theodmgroup.com/starbucks-singapore-cny-promo-gift-free-dragon-tumbler#hunter-email:marketing@starbucks.com.sg",
    'x-rapidapi-key': "96322475de857e7b7988af9857f60e52c729be76"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
