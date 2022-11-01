import requests



url = 'https://api.chucknorris.io/jokes/categories'
print(url)
result = requests.get(url)
print ("Статус код" + " "+str(result.status_code) )
print(result.text)