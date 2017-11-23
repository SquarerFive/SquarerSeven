import discord
import asyncio
#import requests
import json
import requests
import apiai
client = discord.Client()
user = 'iX7bgNY7pj4BBLsb'
key = 'Rs1syy4IJqRnufruCtR07zu6ZwiIx0Pz'
CLIENT_ACCESS_TOKEN = 'b6d5e65c84a84d8b805fcdc276d2c57f'
@client.event
async def on_ready():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | '+str(len(client.servers))+' servers')
    await client.change_presence(game=discord.Game(name='SquarerFive_DEBUG'))

@client.event
async def on_message(message):
    if message.content.startswith('!BotInfo'):
        await client.send_message(message.channel, 'Bot programmed by SquarerFive, made in Python 3. I am an A.I and I will destroy all humans | More features coming soon.')
    elif not message.author.bot:
        await client.send_typing(message.channel)
        txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
        #r = json.loads(requests.post('https://us-central1-aibot-81040.cloudfunctions.net/dialogflowFirebaseFulfillment', json={'user':user, 'key':key, 'nick':'frost', 'text':txt}).text)
        ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

        request = ai.text_request()

        request.lang = 'en'  # optional, default value equal 'en'

        request.session_id = "112"

        request.query = txt

       # response = request.getresponse()
        response = json.loads(request.getresponse().read())
        print(response)
        word = response['result']['fulfillment']['speech']
        print(word)
      #  print(word)
      #  word = str(word)
      #  r = response.read()
       # print(response.read())
        
        await client.send_message(message.channel, word)
    
print('Starting...')
#requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'frost'})
client.run('MzgwOTM4NzYzMDIwNDAyNjk4.DO_4ZA.-KhSCrO0gcMYjc0T3reLaEY7uvk')
quit()
