#二維清單介紹
import os # operating system

 #檢查有沒有檔案的指令 (在該地址中)
def read_file(filename):
	products = []
	with open(filename , 'r', encoding='utf-8') as f:
		for line in f:
			if 'product, price' in line:
				continue #要是for loop 遇到以上字串 則跳過此輪，直接從下一行開始 
			name, price = line.strip().split(',') #split就是分隔的意思，後面括弧輸入要分隔的方式
			products.append([name, price])   #strip就是刪掉換行跟空白
			#這樣印出來s他會是清單(被split之後就是)
	return products

#使用者輸入
def user_input(products):
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
	return products

#products[0][0] # 第一格是大清單中的第0個，而第二格是小清單中的第0個

#印出
def print_products(products):
	for p in products:
		print(p[0])# 這樣只會印出每個清單的第0格
		print(p[0], 'the price is', p[1] )

#'abd' + '123' = 'abc123' #字串可以做合併 挺常用
#'abc' * 3 = 'abcabcabc' #不能做除法跟減法

#寫入!
def write_file(filename, products):
	with open(filename,'w', encoding='utf-8') as f: #將會在電腦創造此檔案，已有的話將會覆蓋此檔案
		f.write('products, price\n') #寫這個還不能加逗號 要直接字串''全概括
		for p in products:
			f.write(str(p[0]) + ',' + p[1] + '\n') #write into the 'f' file
#open只是打開檔案而已，真正寫入是在f.write開始
#檔名改成csv就變成excel了

#加法只能字串跟字串或整數跟整數
#要變字串就要在前面加上str


def main(): #這邊裝者主要的執行程式碼!!
	filename = 'products.csv'
	if os.path.isfile(filename): 
		products = read_file(filename)
		print('yeah! we found it')
	else:
		print('not found')


	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)
main() #有這個 程式才會有動作，沒有的話 上面都只是function 不會有動作

#把我們的程式重購整齊(加入function) 的行為叫做refactor!