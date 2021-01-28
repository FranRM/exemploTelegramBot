import telebot, sys, requests, json

bot = telebot.TeleBot("1667967944:AAHXEmCF0CaP6mUtqAg9S6xuIrZv5j9s0Rc", parse_mode=None)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Boas, e ti de quen ves sendo?")

@bot.message_handler(commands=['chat'])
def send_pepitas(message):
	bot.send_message("217250736","Hola @Femio23")

@bot.message_handler(commands=['david'])
def send_pepitas(message):
	bot.send_message("25216209","Habeeere tipoooooooooo.")

@bot.message_handler(commands=['pavel'])
def send_pepitas(message):
	bot.send_message("148714029","Hola Pavel")

@bot.message_handler(commands=['group'])
def send_pepitas(message):
	bot.send_message("-578948572","Hola @Femio23 en GrupoBot")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	nome=message.from_user.username
	if (message.from_user.id == 148714029):
		nome= "Pavel"
	elif (message.from_user.id == 217250736):
		nome= "Fran"
	elif (message.from_user.id == 25216209):
		nome= "David"
		elif (message.from_user.id == 141747937):
		nome= "Ivan Libreinnova"
	else:
		nome = "alguen (" + str(message.from_user.id) +")"
	bot.send_message(217250736,"Hola @Femio23, "+ nome + " díxome que '" + message.text+ "'.")

bot.polling()