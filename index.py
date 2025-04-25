import discord
import os
import numpy as np

Role_list = np.array(['Main_Role' , 'Guest_Role' , 'Bot_Role' , 'Temp_Role'])
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
    await member.add_roles(Temp_Role)

async def Road_Role():
    Member_Role = client.guild.get_role()

   
client.run(TOKEN)
