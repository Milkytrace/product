import os 

products = []

#確認檔案在，並且讀取檔案
if os.path.isfile('product.csv'):
	print('yay!找到檔案了')
	with open('product.csv','r', encoding='utf-8') as f:
		for line in f:
			if '商品名稱' in line:
				continue
			s = line.strip().split(',')
			products.append(s)
			
#如果找不到檔案，直接跳過讀取檔案的部分，進行寫入
else:
	print('找不到檔案....')

#請使用者輸入
while True:
	name = input('請輸入商品名稱，輸入完成請輸入q:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	quantity = input('了解，那你買了幾個呢：')
	products.append([name, price, quantity])
print(products)

#引出這次所有購買記錄
for p in products:
	print(p[0], '的價格是', p[1], '你總共買了', p[2], '個')

#寫入檔案
with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('商品名稱' + ',' + '商品價格' + ',' + '商品數量' + '\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + ',' + p[2] + '\n')

