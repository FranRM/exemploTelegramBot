import telebot, sys, requests, json

# Definición del bot.
bot = telebot.TeleBot(Token, parse_mode=None)

# Definicion de las funciones mediante comandos del bot.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Boas, e ti de quen ves sendo?")

@bot.message_handler(commands=['chat'])
def send_pepitas(message):
	bot.send_message("idchat","Hola @Femio23")

@bot.message_handler(commands=['david'])
def send_pepitas(message):
	bot.send_message("idchat","Habeeere tipoooooooooo.")

@bot.message_handler(commands=['pavel'])
def send_pepitas(message):
	bot.send_message("idchat","Hola Pavel")

@bot.message_handler(commands=['group'])
def send_pepitas(message):
	bot.send_message("idchat","Hola @Femio23 en GrupoBot")

# Función de reenvio de los mensajes al propietario de todos los mensajes recibidos por el bot.
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	nome=message.from_user.username
	if (message.from_user.id == idchat):
		nome= "Pavel"
	elif (message.from_user.id == idchat):
		nome= "Fran"
	elif (message.from_user.id == idchat):
		nome= "David"
		elif (message.from_user.id == idchat):
		nome= "Ivan Libreinnova"
	else:
		nome = "alguen (" + str(message.from_user.id) +")"
	bot.send_message(idchat,"Hola @Femio23, "+ nome + " díxome que '" + message.text+ "'.")

bot.polling()
