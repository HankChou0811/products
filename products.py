#二維清單介紹
products = []

with open('products.csv' , 'r', encoding='utf-8') as f:
	for line in f:
		name, price = line.strip().split(',') #split就是分隔的意思，後面括弧輸入要分隔的方式
	 #strip就是刪掉換行跟空白
		#這樣印出來s他會是清單(被split之後就是)



while True:
	name = input('please enter the name of the product:')
	if name == 'q':
		break
	price = input('please enter the price:')
	p = []
	p.append(name)
	p.append(price)
	#快速寫法: P = [name. price] 這樣能夠直接取代上面三行
	products.append(p)
	#更進階快速寫法: products.append([name,price]) 這樣可以取代上面四行!!
print(products)

products[0][0] # 第一格是大清單中的第0個，而第二格是小清單中的第0個

for p in products:
	print(p[0])# 這樣只會印出每個清單的第0格
	print(p[0], 'the price is', p[1] )

#'abd' + '123' = 'abc123' #字串可以做合併 挺常用
#'abc' * 3 = 'abcabcabc' #不能做除法跟減法

with open('products.csv','w', encoding='utf-8') as f: #將會在電腦創造此檔案，已有的話將會覆蓋此檔案
	f.write('products, price\n') #寫這個還不能加逗號 要直接字串''全概括
	for p in products:
		f.write(str(p[0]) + ',' + p[1] + '\n') #write into the 'f' file
#open只是打開檔案而已，真正寫入是在f.write開始
#檔名改成csv就變成excel了

#加法只能字串跟字串或整數跟整數
#要變字串就要在前面加上str


