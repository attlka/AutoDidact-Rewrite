import os
import discord
import asyncio
import os
import openai

openai.api_key = ("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")

#GPT3 Engine, Settings and Prompt Fragment
response = openai.Completion.create(
  engine="davinci",
  prompt="Answer the following question using answers from the following wiki: https://pixar.fandom.com/wiki/Lightning_McQueen\n\nQuestion: What are Lightning McQueen's sponsors?\n\nAnswer: Dinoco, Rust-eze, and Flo's V8 Cafe.\n\nQuestion:",
  temperature=0.18,
  max_tokens=63,
  top_p=1,
  frequency_penalty=0.68,
  presence_penalty=0.52,
  stop=["Question"]
)
client = discord.Client()
my_secret = os.environ['Token']

#Summons bot
@client.event
async def on_ready():
	print('Autodidact on stand-by')

@client.event
async def on_message(message):
		if message.author == client.user:
				return

		if message.content.startswith('Hey AutoDidact'):
				await message.channel.send('Hello!')

#Prevents bot from replying to self or responding to cross-chatter
@client.event
async def on_message(message):
	if message.author == bot.user:
		return

	user_message = message.content
	answer = generate_answer(user_message)
		
	if answer == '':
		await message.channel.send('Hmm, Im not sure I quite understand')
	else:
		await message.channel.send(answer)

			
client.run(os.getenv('Token'))

