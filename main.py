import os
import discord
import asyncio
import os
import openai
my_secret = os.environ['gptkey']
openai.api_key = ('gptkey')

client = discord.Client()

#Summons bot to server
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith('!autodidact'):
		await message.channel.send('Autodidact on standby!')

#lets user ask question to gpt-3
@client.event
async def on_message(message):
	if message.content.startswith('!ask'):
		await message.channel.send('Ask me a question!')
		question = message.content[5:]
		response = openai.Completion.create(engine='text-davinci-001', prompt="You are a knowledgable speaker answering questions about Philosophy as a subject. You can only use information that can be found on the following website, The Wikipedia Page for Philosophy, to inform your answers: https://en.wikipedia.org/wiki/Philosophy. Please do not answer with information from other sources. + question\n", temperature=0.07, max_tokens=300)
		await message.channel.send(response.choices[0]['text'])

@client.event
async def on_message(message):
	if message.content.startswith('!help'):
		await message.channel.send('!ask <question> - Ask me a question!')
		await message.channel.send('!help - Displays all commands!')