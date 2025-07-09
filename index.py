import discord
from discord.ui import Button, View
import os
import numpy as np
import json

# 試験用と本番用のトークン，各種チャンネルIDを取得
boot = input('起動方法を選択してください (test/main): ')
if boot != 'test' and boot != 'main':
    print('無効な起動方法です.')
    exit()
elif boot == 'test':
    TOKEN = os.getenv('DCTOKEN_TEST')
    config = json.load(open('config_t.json', 'r', encoding='utf-8'))
elif boot == 'main':
    TOKEN = os.getenv('DCTOKEN')
    config = json.load(open('config.json', 'r', encoding='utf-8'))

# 各種ロール名，チャンネル名を設定
Role_list = np.array(['Main_Role' , 'Guest_Role' , 'Bot_Role' , 'Temp_Role'])
Channel_list = np.array(['AdminCh' , 'TxCh'])

# クライアントの権限を設定
intents = discord.Intents.default()
intents.presences =True
intents.members = True
intents.messages = True
client = discord.Client(intents=intents)

# 起動時の処理
@client.event
async def on_ready():
    print('起動')

# サーバー参加時の処理
@client.event
async def on_member_join(member):
    print(f'{member.name} が参加しました.')
    channel = member.guild.get_channel(int(config["User"][Channel_list[0]]))
    await channel.send(f'@everyone\n{member.display_name} さんが参加しました.', view=ButtonView())
    await member.add_roles(member.guild.get_role(int(config["User"][Role_list[3]])))

# ボタンの設定
class ButtonView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    @discord.ui.button(label="メンバー権限を与える", style=discord.ButtonStyle.secondary)
    async def mem_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(f'{interaction.user.display_name}がメンバー権限を与えました.')
        self.stop()

    @discord.ui.button(label="ゲスト権限を与える", style=discord.ButtonStyle.secondary)
    async def guest_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(f'{interaction.user.display_name}がゲスト権限を与えました.')
        self.stop()

# 起動
try:
    client.run(TOKEN)
except discord.errors.LoginFailure: 
    print('無効なトークンです.')