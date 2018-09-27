import os 
#讀取檔案
def read_file(filename):
	products = []
	with open(filename,'r', encoding='utf-8') as f:
		for line in f:
			if '商品名稱' in line:
				continue
			s = line.strip().split(',')
			products.append(s)
	return products

#請使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱，輸入完成請輸入q:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		quantity = input('了解，那你買了幾個呢：')
		products.append([name, price, quantity])
	print(products)
	return(products)

#引出這次所有購買記錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1], '你總共買了', p[2], '個')

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品名稱' + ',' + '商品價格' + ',' + '商品數量' + '\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + ',' + p[2] + '\n')

def main():
	filename = 'product.csv'
	#檢查檔案在不在
	if os.path.isfile(filename):
		print('Yay 找到檔案了')
		products = read_file(filename)
	else:
		print('找不到檔案....')

	#執行所有 function
	products = user_input(products)
	print_products(products)
	write_file(filename, products)

main()