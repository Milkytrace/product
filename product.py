#學習建立二維度清單
products = []
while True:
	name = input('請輸入商品名稱，輸入完成請輸入q:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	quantity = input('了解，那你買了幾個呢：')
	products.append([name, price, quantity])
print(products)

for p in products:
	print(p[0], '的價格是', p[1], '你總共買了', p[2], '個')

