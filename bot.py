import discord
client = discord.Client()
@client.event
async def on_ready() :
    guilds = [guild.id for guild in client.guilds]
    print(f"The {client.user.name} bot is in {len(guilds)} Guilds.\nThe guilds ids list : {guilds}")

client.run("token here")