from twitchio.ext import commands



with open("config.secret","r") as fp:
    lines = fp.readlines()
    config = {}
    for line in lines:
        partes = line.replace("\n","").split("=")
    config[partes[0]] = partes[1]


bot = commands.Bot(
    irc_token=config['TOKEN'],
    client_id =config['CLIENT_ID'],
    nick=config['BOT_NICK'],
    prefix=config['BOT_PREFIX'],
    initial_channels=[config['CHANNEL']]
)

@bot.event
async def event_ready():
    print(f"{data['BOT_NICK']} online!")
    ws = bot._ws  # solo se necesita en event_ready
    await ws.send_privmsg(data['CHANNEL'], f"/Ha llegado")
@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'
    print(ctx.author.name)

bot.run()

@bot.command(name='test')
async def test(ctx):
    print(ctx)
    await ctx.send(f'Test Pasado! Gracias {ctx.author.name}')
#Cambiamos el manejador de mensajes, para que maneje los comandos
@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'
    await bot.handle_commands(ctx)