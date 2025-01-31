import discord
import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

from Request import Request, handle_request
from credentials import keys_and_credentials


class TextApp:

	def __init__(self):
		self.bot_token = keys_and_credentials.bot_token
		intents = discord.Intents.default()
		intents.message_content = True
		self.client = discord.Client(intents=intents)

		@self.client.event
		async def on_ready():
			print('> Started Discord. //bot= {0.user}'.format(self.client))

		@self.client.event
		async def on_message(message: discord.message):
			if message.author == self.client.user or message == '' :
				return
			req = Request(message.author.name, message.channel, message.content[:])
			res = await asyncio.get_event_loop().run_in_executor(threads_executor, handle_request, req)
			#if private discssion, then doesnt need to mention me
			if message.channel.type != discord.enums.ChannelType.private:
				res = message.author.mention + '  ' + res
			await message.channel.send(res)
			return

	def run(self):
		self.client.run(self.bot_token)


if __name__ == "__main__":

	# Initialize the Thread_Pool that handles the requests
	threads_executor = ThreadPoolExecutor(50)

	d = TextApp()
	d.run()
