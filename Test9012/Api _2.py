import requests

class Price_post():
	
	def art_452853 (self):
	
		url_1 = 'http://core.test.fozzy.lan:8167/Price/'
		
		
		jsona = [
    {
        "guid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "priceDate": "2022-08-23T13:38:33.885Z",
        "client": "R058",
        "supplier": "0036998450",
        "supplierEntityCode": "",
        "taxpayer": 1,
        "priceType": 0,
        "status": 0,
        "errorMessage": "string",
        "lines": [
            {
                "article": 452853,
                "lv": 0,
                "price": 0,
                "vat": 0,
                "mrc": 1,
                "status": 0,
                "errorMessage": "string"
            }
            
        ]
    }
]
		
		result_post = requests.post (url_1, json = jsona)
		print (result_post.text)
		assert 200 == result_post.status_code
		if result_post.status_code == 200:
			print ('цена получена')
price_art = Price_post()
price_art.art_452853()
		