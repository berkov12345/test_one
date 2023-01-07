import requests
# https://github.com/berkov12345/test-Git-1/tree/work-1


url = 'https://api.chucknorris.io/jokes/categories'
print(url)
result = requests.get(url)
print ("Статус код" + " "+str(result.status_code) )
assert 200 == result.status_code
if result.status_code == 200:
	print('четко статус 200')
	print (result.text)
else:
	print ('pнг')
	
