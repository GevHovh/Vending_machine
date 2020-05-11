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




class Drinks():
	def __init__(self,name,*left):
		self.name = name
		self.left = left_from_db(product = name)

coca = Drinks(name = 'Coca-Cola')

print(coca.left)