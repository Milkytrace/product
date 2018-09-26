#學習建立二維度清單
products = []
while True:
	name = input('請輸入商品名稱，輸入完成請輸入q:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	products.append([name, price])
print(products)

print(products[0][0])