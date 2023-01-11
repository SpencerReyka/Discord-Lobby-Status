from reader import Reader
import discord
import os
import requests
import asyncio
from status import Status

def main():
    print("Starting runner!")
    reader = Reader()
    reader.set_up_env()

    status = Status()
    status.run()


    # r = requests.get(f'https://discord.com/api/v9/channels/1042344356520149004/messages?limit=5', headers=self.retrieve_message_headers)
    # Request("https://discordapp.com/api/v6/users/513837216741720094", headers={"Authorization": "Your Discord Token"})

    # client = discord.Client(intents=discord.Intents.default())

    # @client.event
    # async def on_ready() :
    #     guilds = [guild.id for guild in client.guilds]
    #     print(f"The {client.user.name} bot is in {len(guilds)} Guilds.\nThe guilds ids list : {guilds}")
    # print(os.getenv('DISCORD_AUTH'))
    # client.run(os.getenv('DISCORD_AUTH'))

    status.close()

if __name__ == "__main__":
    main()
