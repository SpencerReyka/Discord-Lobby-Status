from discord_proxy import DiscordProxy




class Status():


    def __init__(self):
        self.discord_proxy = DiscordProxy()
        pass


    async def run(self):
        await self.discord_proxy.set_up_discord_py()

        await self.discord_proxy.retrieve_channels_from_discord_py()
        
        #self.guilds = self.discord_proxy.retrieve_users_guilds()
        #channels = self.bdiscord_proxyot.retrieve_channels(self.guilds[-1]["id"])
        #print(channels)

        #print(channels)
        #self.bot.retrieve_channel_info(channels[0]["id"])


        #self.bot.retrieve_user_connections()


        #every thirty minutes run a refresh job (refreshes all of the channels)
        #every 1 second run a check status job 
        #once they find me, run it every 30 seconds but add a CHECK INDIVIDUAL CHANNEL 

        #runs jobs every 1 second

        #job is to pull all my guilds, then go through each one and check if i am in the lobby 
        #prob should set the config as which guilds to pull?
        pass

    async def close(self):
        await self.discord_proxy.close()