from twitchio.ext import commands
class Bot(commands.Bot):
    def __init__(self):
        nick = ""
        chanel = ""
        with open("config.secret","r") as fp:
            lines = fp.readlines()
            config = {}
            for line in lines:
                partes = line.replace("\n","").split("=")
                config[partes[0]] = partes[1]
            super().__init__(
                irc_token=config['TOKEN'],
                client_id =config['CLIENT_ID'],
                nick=config['BOT_NICK'],
                prefix=config['BOT_PREFIX'],
                initial_channels=[config['CHANNEL']]
            )
        self.nick = config['BOT_NICK']
        self.channel = config['CHANNEL']
            
    
    async def event_ready(self):
        print(f'Listo! | {self.nick}')
        ws = self._ws 
        await ws.send_privmsg(self.channel, f"/me has landed!")
    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)
    # Decorador para los comandos
    @commands.command(name='saludo')
    async def saludo(self, ctx):
        await ctx.send(f'Hola {ctx.author.name}!')
bot = Bot()
bot.run()
