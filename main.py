from twitchio.ext import commands
import threading
import time
import re
import asyncio
from datetime import datetime
from random import choice
from datetime import datetime, date
from twitchtools import sendCommercial, setTitle, setGame, streamLive, followSince


#compilarPatrones
patron1 = re.compile('(?i)ho+l[aiou]+')
patron2 = re.compile('(?i)co+fre+s*')
ADMIN = 'reportforflame'
MODS = ('darkor12', 'betterkrau')

#Clase Bot
class Bot(commands.Bot):
    def __init__(self):
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
        self.lastPredictedDate = datetime.now()
        self.lastHelloDate = datetime.now()
        self.lastInstaDate = datetime.now()
        self.lastTwitterDate = datetime.now()
        self.live = False


    async def event_ready(self):
        print(f'Listo! | {self.nick}')
        ws = self._ws
        await ws.send_privmsg(self.channel, f"/me ha aparecido!")

    def isPredictAvailable(self, type=0):
        timeNow = datetime.now()
        if type == 0:
            seconds = (timeNow - self.lastPredictedDate).total_seconds()
            available = seconds >= 60
            if available:
                self.lastPredictedDate = timeNow
        elif type == 1:
            seconds = (timeNow - self.lastHelloDate).total_seconds()
            available = seconds >= 20
            if available:
                self.lastHelloDate = timeNow
        elif type == 2:
            seconds = (timeNow - self.lastInstaDate).total_seconds()
            available = seconds >= 120
            if available:
                self.lastInstaDate = timeNow
        elif type == 3:
            seconds = (timeNow - self.lastTwitterDate).total_seconds()
            available = seconds >= 120
            if available:
                self.lastTwitterDate = timeNow
        return available

    async def event_message(self, message):
        print(message.content)

        if patron1.search(message.content.lower()) and self.isPredictAvailable(1):
            if message.author.is_subscriber:
                hello = f'Holaaa @{message.author.name}! 💜💜💜'
            else:
                hello = choice((
                    f'Hola @{message.author.name}!',
                    f'Hola @{message.author.name}! ❤️',
                    f'Hola @{message.author.name}! 😊'
                ))
            await message.channel.send(hello)

        elif patron2.search(message.content.lower()) and self.isPredictAvailable(1):
            await message.channel.send(f'¿He leido cofre? Puedes conseguir un cofre gratis de la colección de @ReportForFlame en Streamloots https://www.streamloots.com/reportforflame?couponCode=YIT26')

        if ('insta' in message.content.lower() or 'instagram' in message.content.lower()) and self.isPredictAvailable(2):
            await message.channel.send('Sigue a @ReportForFlame en Instagram! ❤️')
            return
        if ('twitter' in message.content.lower() or 'tweet' in message.content.lower()) and self.isPredictAvailable(3):
            await message.channel.send('Sigue a @CrazyAnnieTMI en Twitter! 🐥')
            return

        await self.handle_commands(message)


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

    @commands.command(name='ig', aliases=['instagram'])
    async def ig(self, ctx):
        await ctx.send('Sigue a @ReportForFlame en Instagram! ❤️')

    @commands.command(name='sw', aliases=['switch', 'nintendo'])
    async def switch(self, ctx):
        await ctx.send('Agrégame en Nintendo Switch: SW-0044-5826-1325 🎮')


    @commands.command(name='platanomelon', aliases=['pm', 'platano', 'melon'])
    async def platanomelon(self, ctx):
        await ctx.send(
            'Obtén 5€ de descuento en tu primer pedido de al menos '
            '50€ en Platanomelón utilizando este enlace '
            'https://prz.io/mvgoP1u8 🍌🍈')

    @commands.command(name='letyshops', aliases=['lety', 'cashback'])
    async def letyshops(self, ctx):
        await ctx.send(
            'Gana 5€ al registrarte en Letyshops con este enlace y realizar '
            'una compra de al menos 20€ '
            'https://letyshops.com/es/winwin?ww=12937023 🛒🛍')

    @commands.command(name='startstream')
    async def startstream(self, ctx):
        if ctx.author.name.lower() != ADMIN and self.live: return
        await ctx.send('He iniciado las tareas programadas ✅')
        self.live = True
        while self.live:
            await asyncio.sleep(60 * 15)
            if not self.live: break
            await ctx.send(f'Puedes canjearme un cofre usando este código: https://www.streamloots.com/reportforflame?couponCode=YIT26 de StreamLoots! 🎁')
            await ctx.send('Recuerda seguirme en twitter para estar al tanto de todo twitter.com/crazyannietmi 💜 ^^')
            await asyncio.sleep(60 * 15)
            if not self.live: break
            await ctx.send(f'No olvides usar tu prime para apoyarme si te gusta mi stream 🤩')
            await ctx.send('Tengo un canal de Discord por si os apetece uniros https://discord.gg/VaHwkrX 🥰 ^^')
            addTime = choice((30, 30, 60))
            sendCommercial(addTime)

    @commands.command(name='endstream', aliases=['stopstream'])
    async def endstream(self, ctx):
        if ctx.author.name.lower() != ADMIN: return
        self.live = False
        await ctx.send('He desactivado las tareas programadas ✅')
        global TRACKER_ENABLED
        TRACKER_ENABLED = False


    @commands.command(name='abrazar')
    async def abrazar(self, ctx):
        if len(ctx.content) >=9:
            user = ctx.content[9:]
            await ctx.send(f'{ctx.author.name} le da un gran abrazo a {user}!')
        else:
            await ctx.send(f'Necesito que me digas a quien quieres abrazar mencionándolo después del comando.')


    @commands.command(name='add')
    async def add(self, ctx):
        if ctx.author.name.lower() != ADMIN: return
        if len(ctx.content) >=5:
            time = ctx.content[5:]
            sendCommercial(int(time))
        else:
            sendCommercial(30)

    @commands.command(name='verse')
    async def verse(self, ctx):
        await ctx.send(f'Usa mi codigo promocional para ganar 5€ con Verse. Mejor que Bizum. Link: https://verse.me/invite/3GQR4P')

    @commands.command(name='title')
    async def title(self, ctx):
        if ctx.author.name.lower() != ADMIN: return
        if len(ctx.content) >=7:
            title = ctx.content[7:]
            setTitle(title)
        else:
            await ctx.send(f'Tienes que especificar el nuevo titulo para el stream.')

    @commands.command(name='game')
    async def game(self, ctx):
        if ctx.author.name.lower() != ADMIN: return
        if len(ctx.content) >=6:
            game = ctx.content[6:]
            setGame(game)
        else:
            await ctx.send(f'Tienes que especificar el nuevo juego para el stream.')

    '''@commands.command(name='live')
    async def live(self, ctx):
        live = streamLive()
        await ctx.send(live)'''

    @commands.command(name='follow')
    async def follow(self, ctx):
        if ctx.author.id != 68307698:
            fecha = followSince(ctx.author.id)

            today = datetime.now()
            past_date = datetime.strptime(fecha, '%Y-%m-%dT%H:%M:%SZ')
            print(past_date)
            days = (today - past_date).days
            await ctx.send(f'Llevas siguiendo a ReportForFlame desde el ' + str(past_date.day) + '/' + str(past_date.month) + '/' + str(past_date.year) + ', o lo que es lo mismo, ' + str(days) + ' dias.')


    @commands.command(name='comandos', aliases={'help'})
    async def comandos(self, ctx):
        comandos = []
        seperator = ", "
        for command in self.commands:
            if command != 'comandos' and command != 'startstream' and command != 'endstream' and command != 'title' and command != 'game':
                comandos.append(command)
        await ctx.send(f'Los comandos del stream son:'+ "\n" + seperator.join(comandos))


#Ejecutar bot
bot = Bot()
bot.run()
