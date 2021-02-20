from twitchio.ext import commands
from twisted.internet import task
from twisted.internet import reactor
import re


#compilarPatrones():
patron1 = re.compile('(?i)ho+la+')

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

        '''if 'hola' in message.content.lower():
            await message.channel.send(f"¡Hola @{message.author.name}, bienvenido/a al stream!")'''

        if patron1.search(message.content.lower()):
            await message.channel.send(f"¡Hola @{message.author.name}, bienvenido/a al stream!")
            

    '''timeout = 30.0 # Segundos del timer

    async def timer(self):
        #do work here
        await self.channel.send(f'Recuerda seguirme en twitter para estar al tanto de todo twitter.com/crazyannietmi\nTambién puedes canjearme un cofre usando este código: https://www.streamloots.com/reportforflame?couponCode=YIT26')

    l = task.LoopingCall(timer)
    l.start(timeout) #Lo invocamos cada 600 segundos

    reactor.run()'''



    # Decorador para los comandos
    @commands.command(name='discord')
    async def discord(self, ctx):
        await ctx.send(f'Si queréis formar parte de una gran comunidad, uníos sin faltar https://discord.gg/VaHwkrX')
    @commands.command(name='loots')
    async def loots(self, ctx):
        await ctx.send(f'Consigue un cofre gratis de mi colección de Streamloots https://www.streamloots.com/reportforflame?couponCode=YIT26')
    @commands.command(name='twitter')
    async def twitter(self, ctx):
        await ctx.send(f'Puedes seguirme en twitter para estar al tanto de todo twitter.com/crazyannietmi')
    @commands.command(name='abrazar')
    async def abrazar(self, ctx):
        if len(ctx.content) >=9:
            user = ctx.content[9:]
            await ctx.send(f'{ctx.author.name} le da un gran abrazo a {user}!')
        else:
            await ctx.send(f'Necesito que me digas a quien quieres abrazar mencionándolo después del comando.')
    @commands.command(name='verse')
    async def verse(self, ctx):
        await ctx.send(f'Usa mi codigo promocional para ganar 5€ con Verse. Mejor que Bizum. Link: https://verse.me/invite/3GQR4P')
    @commands.command(name='comandos')
    async def comandos(self, ctx):
        comandos = []
        seperator = ", "
        for command in self.commands:
            if command != 'comandos':
                comandos.append(command)
        await ctx.send(f'Los comandos del stream son:'+ "\n" + seperator.join(comandos))
        

bot = Bot()
bot.run()  