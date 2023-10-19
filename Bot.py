import discord
import os
import requests
import json
import random

client = discord.Client()

# Function to fetch interesting quotes and facts from an API and display one of them.
def get_quote():
    response = requests.get("https://api.example.com/quotes")
    json_data = json.loads(response.text)
    quote = json_data['quote']
    return quote

# Similar to the get_quote function but returns fun facts.
def get_fun_fact():
    response = requests.get("https://api.example.com/fun-facts")
    json_data = json.loads(response.text)
    fact = json_data['data'][random.randint(0, 24)]['fact']
    return fact

# Notification that the bot is up and running correctly.
@client.event
async def on_ready():
    print('Bot is now online: {0.user}'.format(client))

# Listens for specific messages in discord and responds accordingly.
@client.event
async def on_message(message):
    if message.content.startswith('!quote'):
        quote = get_quote()
        await message.channel.send(quote)
    if message.content.startswith('!funfact'):
        fact = get_fun_fact()
        await message.channel.send(fact)

# Replace 'YOUR_TOKEN_HERE' with your actual bot token.
client.run(os.environ.get('YOUR_TOKEN_HERE'))
