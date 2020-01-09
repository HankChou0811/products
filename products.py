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