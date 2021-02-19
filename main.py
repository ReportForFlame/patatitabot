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
        await ws.send_privmsg(self.channel, f"/me ha aparecido!")
    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    # Decorador para los comandos
    @commands.command(name='saludo')
    async def saludo(self, ctx):
        await ctx.send(f'Hola {ctx.author.name}!')
    @commands.command(name='discord')
    async def discord(self, ctx):
        await ctx.send(f'Si queréis formar parte de una gran comunidad, uníos sin faltar https://discord.gg/VaHwkrX')
    @commands.command(name='loots')
    async def loots(self, ctx):
        await ctx.send(f'Consigue un cofre gratis de mi colección de Streamloots https://www.streamloots.com/reportforflame?couponCode=Q1Q65')
    @commands.command(name='twitter')
    async def twitter(self, ctx):
        await ctx.send(f'Puedes seguirme en twitter para estar al tanto de todo twitter.com/crazyannietmi')
    @commands.command(name='abrazar')
    async def abrazar(self, ctx):
        user = ctx.content[9:]
        await ctx.send(f'{ctx.author.name} le da un gran abrazo a {user}!')
    @commands.command(name='verse')
    async def verse(self, ctx):
        await ctx.send(f'Usa mi codigo promocional para ganar 5€ con Verse. Mejor que Bizum. Link: https://verse.me/invite/3GQR4P')
    @commands.command(name='comandos')
    async def comandos(self, ctx):
        comandos = []
        for command in self.commands:
            comandos = comandos + command
        await ctx.send(comandos)
    
    



bot = Bot()
bot.run()    
