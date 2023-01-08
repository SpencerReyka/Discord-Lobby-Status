import requests
import json
import os
import discord
from discord import VoiceChannel

class DiscordProxy():
    def __init__(self):
        print("initializing discord proxy")

        if "DISCORD_AUTH" in os.environ: 
           self.auth = os.getenv('DISCORD_AUTH')
        else:
            print("No Fishing Auth in env")

        if "DISCORD_BOT_AUTH" in os.environ: 
           self.bot_auth = "bot " + os.getenv('DISCORD_AUTH')
        else:
            print("No Fishing Auth in env")

        self.retrieve_message_headers = {
            'authorization': self.auth
        }

        self.bot_headers = {
            'authorization': self.bot_auth
        }
        
        self.fish_headers = {
            'Content-Type': 'application/json',
            'authorization': self.auth
        }

        self.fish_payload = {
            'type': 2,
            'application_id': os.getenv('FISH_APPLICATION_ID'),
            'channel_id': os.getenv('FISH_CHANNEL_ID'),
            'guild_id': os.getenv('FISH_GUILD_ID'),
            'session_id': os.getenv('FISH_SESSION_ID'),
            'data': {
                'version': os.getenv('FISH_VERSION'),
                'id': os.getenv('FISH_ID'),
                'name': "fish",
                'type': '1',
                #'options': [],# [parameters] if parameters else [],
                #'application_command': '',# cmd_data,
                #'attachments': []
            },
        }

    async def set_up_discord_py(self):
        intents = discord.Intents.all()

        self.client = discord.Client(intents=intents)

        @self.client.event
        async def on_ready():
            print(f'We have logged in as {self.client.user}')
            print(f'{self.client.user} has {self.client.guilds}')
            print(f'{self.client.user} has {self.client.voice_clients}')
            for guild in self.client.guilds:
                print(f'{guild} has {guild.channels}')
                for channel in guild.channels:
                    if isinstance(channel, VoiceChannel):
                        print(channel.members)
            await self.client.close()

        await self.client.login(os.getenv('DISCORD_BOT_AUTH'))

    async def retrieve_channels_from_discord_py(self):
        guild = await self.client.fetch_guild(os.getenv('FIRDAY_DISC_ID'))

        # print(self.client.voice_clients)
        # channels = await guild.fetch_channels()
        # print(channels)
        # for channel in channels:
        #     if channel.name == "horsey go neigh":
        #         print(channel.members)
        #         fleshed_channel = await guild.fetch_channel(channel.id)

        #         print(fleshed_channel.members)
            #chan = await client.get_channel(channel.id) #gets the channel you want to get the list from

            #print(chan.members)
        
        await self.client.connect()

        pass

    async def close(self):
        if self.client:
            print("closing client")
            await self.client.close()


    def retrieve_messages(self):
        r = requests.get(f'https://discord.com/api/v9/channels/1042344356520149004/messages?limit=5', headers=self.retrieve_message_headers)
        print(r)
        return json.loads(r.text)

    def fish(self):
        print("fishing")

        #r = requests.post(f'https://discord.com/api/v9/interactions', headers=self.fish_headers, json=self.fish_payload)

    def retrieve_users_guilds(self): #cache for a 30 min call
        r = requests.get(f'https://discord.com/api/v9/users/@me/guilds', headers=self.retrieve_message_headers)

        ret = []
        for guild in json.loads(r.text):
            ret.append(guild)
        return ret

    def retrieve_channels(self, guild_id):
        print(guild_id)
        r = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/members', headers=self.bot_headers)
        print(r)
        # ret = []
        # for channel in json.loads(r.text):
        #     if channel["type"] == 2:
        #         ret.append(channel)
        # return ret


    def retrieve_channel_info(self, channel_id):
        r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}', headers=self.retrieve_message_headers)
        print(r.json())

        return json.loads(r.text)

    def retrieve_user_connections(self): #cache for a 30 min call
        r = requests.get(f'https://discord.com/api/v9/channels/473648919700701184', headers=self.retrieve_message_headers)
        print(r.text)
