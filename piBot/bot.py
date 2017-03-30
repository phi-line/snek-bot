from datetime import datetime
from urllib.parse import urlencode

from discord.ext.commands import Bot

import secrets

pibot = Bot(command_prefix=";")


@pibot.async_event
async def on_ready():
	print("piB0t logged in")


@pibot.command()
async def ls(*args):
	print(args)
	topic = format(args[0])
	print(len(topic))
	if topic == "help":
		return await pibot.say("Command list: ;tw ;yt ;dd ;py ;dpy ;ti ;pyg"
								"\n\nType ;ls \"command\" for help on that topic.")
	elif topic == "tw":
		return await pibot.say("This command is used to link a twitch user's stream."
								"\n\n<syntax> ;tw \"username\"")
	elif topic == "yt":
		return await pibot.say("This command is used to link youtube searches."
								"\n\n<syntax> ;yt \"term1\" \"term2\" \"term3\"")
	elif topic == "dd":
		return await pibot.say("This command is used to link Duck Duck Go searches."
								"\n\n<syntax> ;dd \"term1\" \"term2\" \"term3\"")
	elif topic == "py":
		return await pibot.say("This command is used to link Python documentation searches."
								"\n\n<syntax> ;py \"term1\" \"term2\" \"term3\"")
	elif topic == "dpy":
		return await pibot.say("This command is used to link discord.py documentation searches."
								"\n\n<syntax> ;dpy \"term1\" \"term2\" \"term3\"")
	elif topic == "ti":
		return await pibot.say("This command is used to post the local time of the bot (usually eastern)."
								"\n\n<syntax> ;ti [does not take arguments]")
	elif topic == "pyg":
		return await pibot.say("This command is a simple piglatin translator."
								"\n\n<syntax> ;pyg \"word\"")
	else:
		return await pibot.say("Invalid help topic.")

@pibot.command()
async def tw(*args):
	print(args)
	url = ("https://www.twitch.tv/{}".format(args[0]))
	return await pibot.say(url)

@pibot.command()
async def yt(*args):
	print(args)
	url = ("https://www.youtube.com/results?search_{}".format(
				urlencode({'query': ' '.join(args)})
			))
	return await pibot.say(url)

@pibot.command()
async def dd(*args):
	print(args)
	url = ("https://duckduckgo.com/?{}".format(
				urlencode({'q': ' '.join(args)})
			))
	return await pibot.say(url)

@pibot.command()
async def py(*args):
	print(args)
	url = ("https://docs.python.org/3/search.html?{}"
			"&check_keywords=yes&area=default".format(
				urlencode({'q': ' '.join(args)})
			))
	return await pibot.say(url)

@pibot.command()
async def dpy(*args):
	print(args)
	url = ("https://discordpy.readthedocs.io/en/latest/search.html?{}"
			"&check_keywords=yes&area=default".format(
				urlencode({'q': ' '.join(args)})
			))
	return await pibot.say(url)

@pibot.command()
async def ti(*args):
	now = datetime.now()
	print(now)
	return await pibot.say("piB0t time (eastern) is %s:%s:%s   %s/%s/%s"
							% (now.hour, now.minute, now.second, now.month,
							now.day, now.year))

@pibot.command()
async def pyg(*args):
	print(args)
	word = format(args[0])
	latin = word.lower()[1:len(word.lower())] + word.lower()[0] + 'ay'
	if len(word) > 0 and word.isalpha():
		print(latin)
		return await pibot.say('Your word is: ' + latin)
	else:
		print('invalid word')
		return await pibot.say('That isn\'t a word, stupid!')

pibot.run(secrets.BOT_TOKEN)