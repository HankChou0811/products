#二維清單介紹
products = []
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

with open('products.txt','w') as f: #將會在電腦創造此檔案，已有的話將會覆蓋此檔案
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #write into the 'f' file
#open只是打開檔案而已，真正寫入是在f.write開始
#檔名改成csv就變成excel了