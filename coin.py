#196, 245, 191, 207, 137, 252, 152, 239, 170, 45, 1, 36, 48, 139, 97, 164, 229,
#89, 89, 50, 152, 143, 149, 164, 155, 136, 12, 72, 197, 26, 55, 242
#200-256 animal, 22 numbers
#
import random
import flask 

class CoinGen:

 	def __init__(self, hashfn):

	 	def which_item(n, hashfn):

	 		# 101-220 animal
		 	# 1-100 coin
		 	#221-256 item

	 		if (n <= 100):
	 			print("I'm a Coin.")
	 			return (0, Coin())
	 		elif (n <= 220):
	 			print("I'm a Creature.")
	 			return (1, CoinCreature(hashfn))
	 		else:
	 			print("I'm an Item.")
	 			return (2, CoinItem(hashfn))

	 	self.item = which_item(hashfn[10], hashfn)
	 	print(hashfn)
	 	print(hashfn[10])

# octopus is now the most rare
class CoinCreature:

	def __init__(self, hashfn):

	 	self.animal_type =  self.animal_type(hashfn[11])
	 	self.eye = self.eye_type(hashfn[12])
	 	self.color_1 = (hashfn[13],hashfn[14],hashfn[15])
	 	self.color_2 = (hashfn[16],hashfn[17],hashfn[18])
	 	self.color_3 = (hashfn[19],hashfn[20],hashfn[21])

	def animal_type(self, n):

		if(n <= 75):
			return "bear"
		elif(n <= 110):
			return "bunny"
		elif(n <= 140):
			return "squirrel"
		elif(n <= 160):
			return "fox"
		elif(n <= 180):
			return "panda"
		elif(n <= 200):
			return "deer"
		elif(n <= 220):
			return "dalmation"
		elif(n <= 253):
			return "hedgehog"
		else:
			return "octopus"

	def eye_type(self, n):

		if (n <= 100):
			return "basic"
		elif(n <= 200):
			return "cute"
		elif(n <= 255):
			return "crazy"
		else:
			return "angry"

class Coin:

	def __init__(self):
		self.coin = 1

class CoinItem:

	def __init__(self, hashfn):
		self.item_type = self.type_picker(hashfn[22])
		self.item_name = self.name_picker(hashfn[23], self.item_type)

	def type_picker(self, n):
		return "food"

	def name_picker(self, n, item_type):

		if(item_type == "food"):
			if(n <= 100):
				return "ice_cream"
			elif(n <= 200):
				return "cake"
			else:
				return "drumstick"

def test(hashfn):

	init_coin = CoinGen(hashfn)

	item = init_coin.item

	animal_string = ""

	if item[0] == 1:
		animal = item[1]
		animal_string = "I'm a "
		animal_string += str(animal.animal_type)
		animal_string += " with "
		animal_string += str(animal.eye)
		animal_string += " eyes and "
		animal_string += str(animal.color_1)
		animal_string += " fur."
		print(animal_string)

	if item[0] == 2:
		item = item[1]
        item_string = "I am a "
        item_string += str(item.item_type)
        item_string += ". I am a "
        item_string += str(item.item_name)
        item_string += "."
        print(item_string)

	return 

def gen_list():

	rand_list = []

	for i in range(32):
		rand_list.append(random.randint(1,256))

	return rand_list

# test(gen_list())

def sha_to_list(sha):

	byte_list = []

	for i in range(32):
		byte_list.append(int("0x"+sha[:2],0))
		sha = sha[2:]

	return byte_list

app = flask.Flask(__name__)

@app.route('/token/<sha>')
def show_token(sha=None):
	byte_list = sha_to_list(sha)
	coin = CoinGen(byte_list).item
	print(coin[0])
	return flask.render_template("token.html", coin=coin)


@app.route('/static/<path:path>')
def serve_static_files(path):
    return send_from_directory('static', path)

def replace(fname):

    f = open(fname, 'r')
    content = f.read()
    
    color1 = (hashfn[13],hashfn[14],hashfn[15])
    color2= (hashfn[16],hashfn[17],hashfn[18])
    color3= (hashfn[19],hashfn[20],hashfn[21])
    
    content = content.replace('#bebebe', color1)
    content = content.replace('#725af7', color3)
    content = content.replace('#6edaf4', color2)
    f.close()
    
    new_f = open('new_'+fname, 'w')
    new_f.write(content)
    new_f.close()
