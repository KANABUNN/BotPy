import discord
import os
import numpy as np
import json

Role_list = np.array(['Main_Role' , 'Guest_Role' , 'Bot_Role' , 'Temp_Role'])
config = json.load(open('config_t.json', 'r', encoding='utf-8'))
for i in range(len(Role_list)):
    Role_list[i] = config[Role_list[i]]
TOKEN = os.getenv('DCTOKEN2')
intents = discord.Intents.none()
intents.presences =True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.activity.Game(name='テスト中'))

@client.event
async def on_member_join(member):
    print(f'{member.name} が参加しました.')
    await member.add_roles(Role_list[3])

client.run(TOKEN)
