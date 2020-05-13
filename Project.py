import mysql.connector

mydb = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'root')

mycursor = mydb.cursor()

def left_from_db(product):
	sql = 'SELECT `left` FROM dispenser.products_left WHERE product = %s'
	mycursor.execute(sql,(product,))
	myresult = mycursor.fetchone()
	return myresult[0]

class Product():
	"""Product class
	Subclasses - Drinks, Chips, Choclate"""
	def __init__(self, product_name, *left):
		self.product_name = product_name
		self.left = left_from_db(product = product_name)

class Drinks(Product):
	"""docstring for Drinks
	Take 2 args - litre and price"""
	def __init__(self, product_name, *left, litre, price):
		super().__init__(product_name, left)
		self.litre = litre
		self.price = price

class Chips(Product):
	"""docstring for Chips
	Takes 2 args - grams of product and the price"""
	def __init__(self, product_name, *left, grams, price):
		super().__init__(product_name, left)
		self.grams = grams
		self.price = price

class Choclate(Product):
	"""docstring for Chocklate
	Takes 2 args - grams of product and the price"""
	def __init__(self, product_name, *left, grams, price):
		super().__init__(product_name, left)
		self.grams = grams
		self.price = price

class Coin():
	"""docstring for Coin"""
	def __init__(self, value, name = 'coin'):
		self.value = value
		self.name = str(str(value) + ' coin')

def select_product():
	'''Gives opportunity to choose an item and checks if it is aviable'''
	st = False
	while st == False:
		product_number = input('\nInput product index: ')
		order_number = 0

		if product_number == '1':
			order_number = product_number
		elif product_number == '2':
			order_number = product_number
		elif product_number == '3':
			order_number = product_number
		elif product_number == '4':
			order_number = product_number
		elif product_number == '5':
			order_number = product_number
		elif product_number == '6':
			order_number = product_number
		elif product_number == '7':
			order_number = product_number
		elif product_number == '8':
			order_number = product_number
		elif product_number == '9':
			order_number = product_number
		else:
			print('Sry, there is no such index')
			continue
	
		if int(list_of_products[int(int(order_number) - 1)].left) == 0:
			print('Sry, there is no: ' + str(list_of_products[int(int(order_number) - 1)].product_name))
			continue
		else:
			print('You choose: ' + str(list_of_products[int(int(order_number) - 1)].product_name))
			st = True
		return int(int(order_number) - 1)

def input_money():
	'''Gives opportuniy to input coins and counts final amount'''
	list_of_aviable_coins = [50, 100, 200, 500]
	input_coin_list = []
	def  input_coin(input_coin_value):
		while int(input_coin_value) not in list_of_aviable_coins:
			print("Wrong coin value")
			input_coin_value = input('(Aviable coins: 50, 100, 200, 500)\nInput coin: ')
		else:
			input_coin = Coin(int(input_coin_value))
			input_coin_list.append(input_coin)
	list_of_aviable_coins = [50, 100, 200, 500]
	input_coin_list = []
	total_money = []
	how_many_coins = input('How many coins do you want to use: ')
	
	for _ in range(int(how_many_coins)):
		input_coin(input_coin_value = input('(Aviable coins: 50, 100, 200, 500)\nInput coin: '))
	
	for i in range(int(how_many_coins)):
		total_money.append(int(input_coin_list[i].value))

	return sum(total_money)

def info(product):
	'''Gives grams/litre of product and its price'''
	if isinstance(product, Drinks):
		print(str(product.product_name) + " " +  str(product.litre) + 'L')
	elif isinstance(product, (Chips, Choclate)):
		print(str(product.product_name) + " " +  str(product.grams) + 'g')
	print('Price is ' + str(product.price))

def order_process(order_number,money):
	stt = False
	while stt == False:
		if money >= list_of_products[order_number].price:
			print('Sucess, you can take your order')
			print('Your balance is ' + str(money - list_of_products[order_number].price))
			stt = True
			sql = 'UPDATE dispenser.products_left SET `left` = `left` - 1 WHERE `product` = %s'
			mycursor.execute(sql,(list_of_products[order_number].product_name,))
			mydb.commit()
		else:
			print('Sry, you have no enough balance')
			print('Take your money back')

#Add some drinks		
coca_cola =  Drinks(product_name = 'Coca-Cola', litre = 0.5, price = 300)
sprite =  Drinks(product_name = 'Sprite', litre = 0.5, price = 300)
fanta =  Drinks(product_name = 'Fanta', litre = 0.5, price = 300)

#Add some chips
lays = Chips(product_name = 'Lays', grams = 80 , price = 500)
cheetos = Chips(product_name = 'Cheetos', grams = 85 , price = 800)
doritos = Chips(product_name = 'Doritos', grams = 77 , price = 550)

#Add some choclate
snickers = Choclate(product_name = 'Snickers', grams = 55, price = 250)
mars = Choclate(product_name = 'Mars', grams = 50, price = 250)
kitkat = Choclate(product_name = 'KitKat', grams = 45, price = 200)

list_of_products = [coca_cola, sprite, fanta, lays, cheetos, doritos, snickers, mars, kitkat]

#Manu part
print('Welcome to the secret shop\nYou can buy:\n')

for i in range(9):
	print(str(i+1) + ':' + str(list_of_products[i].product_name) + ' Left - ' + str(list_of_products[i].left))

order_process(order_number = select_product(), money = input_money())

