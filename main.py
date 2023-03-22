import discord
from discord.ext import commands
import openai

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='#', intents=intents)
openai.api_key = "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" # replace with your API key

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def greet(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')

@client.command()
async def flip(ctx):
    import random
    result = random.choice(['heads', 'tails'])
    await ctx.send(f'{ctx.author.name} flipped {result}')

@client.command()
async def roll(ctx):
    import random
    result = random.randint(1, 6)
    await ctx.send(f'{ctx.author.name} rolled {result}')

@client.command()
async def joke(ctx):
    import requests
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    if response.status_code == 200:
        joke_data = response.json()
        setup = joke_data['setup']
        punchline = joke_data['punchline']
        await ctx.send(setup)
        await ctx.send(punchline)
    else:
        await ctx.send('Sorry, could not retrieve joke')

async def generate_image(ctx, prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        await ctx.send(image_url)

    except Exception as e:
        await ctx.send(f"Error: {e}")

@client.command()
async def paint(ctx, *, question):
    await generate_image(ctx, question)

@client.command(name='delete')
@commands.has_permissions(administrator=True)
async def delete_messages(ctx, amount=1):
    """
    Deletes a specified number of messages in the current channel.

    Usage: !delete [amount]
    """
    await ctx.channel.purge(limit=amount+1)

#Discord BOT AUTH TOKEN
client.run('MTA2ODM4NjE4MDExNjI1NDc3MQ.GvxV09.dps2zNi-7eX8bs5tbaKboaJ1p8RrO1rffwHzPA')
