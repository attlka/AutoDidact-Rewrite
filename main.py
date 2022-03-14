import os
import discord
import asyncio
import os
import openai
my_secret = os.environ['gptkey']
openai.api_key = ('gptkey')

client = discord.Client()

#Summons bot
@client.event
async def on_message(message):
		if message.author == client.user:
				return

		if message.content.startswith('Hey AutoDidact'):
				await message.channel.send('AutoDidact on standby!')

@client.event
async def on_message(message):
	if message.author == bot.user:
		return

		openai.api_key = os.getenv("gpt_key")

		response = openai.Completion.create(
  	engine="text-davinci-001",
 		prompt="You are a knowledgable speaker answering questions about Philosophy as a subject. You can only use information that can be found on the following website, The Wikipedia Page for Philosophy, to inform your answers: https://en.wikipedia.org/wiki/Philosophy. Please do not answer with information from other sources.\n",
		temperature=0.07,
		max_tokens=308,
		top_p=1,
		frequency_penalty=0.68,
		presence_penalty=0.52,
		stop=["Question"]
)
	user_message = message.content
	answer = generate_answer(user_message)
		
	if answer == '':
		await message.channel.send('Hmm, Im not sure I quite understand')
	else:
		await message.channel.send(answer)

client.run(os.getenv('Token'))
