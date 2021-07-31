import os
import random
from twitchio.ext import commands
from rcon import Client
from time import sleep

chat_input = ""

# Settings for how long a command will last.
movement_time = int(2)
attack_time = int(1)
look_time = int(2)
# 0-1 not yet added.
taunt_active = int(0)
random_class = int(0)


# Random class logic. Not yet added.
def ran_class():
    if random_class == 1:
        rand_num = random.randint(1, 9)
    return rand_num


# Commands for twitch chat
def attack():
    global chat_input, client, attack_time
    chat_input = client.run("+attack")
    sleep(attack_time)
    chat_input = client.run("-attack")
    return chat_input


def alt():
    global chat_input, client, attack_time
    chat_input = client.run("+attack2")
    sleep(attack_time)
    chat_input = client.run("-attack2")
    return chat_input


def right():
    global chat_input, client, look_time
    chat_input = client.run("+right")
    sleep(look_time)
    chat_input = client.run("-right")
    return chat_input


def left():
    global chat_input, client, look_time
    chat_input = client.run("+left")
    sleep(look_time)
    chat_input = client.run("-left")
    return chat_input


def forward():
    global chat_input, client, movement_time
    chat_input = client.run("+forward")
    sleep(movement_time)
    chat_input = client.run("-forward")
    return chat_input


def back():
    global chat_input, client, movement_time
    chat_input = client.run("+back")
    sleep(movement_time)
    chat_input = client.run("-back")
    return chat_input


def jump():
    global chat_input, client
    chat_input = client.run("+jump")
    sleep(1)
    chat_input = client.run("-jump")
    return chat_input


def use():
    global chat_input, client
    chat_input = client.run("+use_action_slot_item")
    sleep(1)
    chat_input = client.run("-use_action_slot_item")
    return chat_input


def rand_loadout():
    rand_load = random.randint(1, 4)
    chat_input = client.run("load_itempreset {}".format(rand_load))
    return chat_input


def taunt():
    rand_load = random.randint(1, 4)
    chat_input = client.run("taunt")
    return chat_input


def help():
    global chat_input, client
    count = 30
    while count > 0:
        count = count - 1
        chat_input = client.run("voicemenu 0 0")
    return chat_input


def scout():
    global chat_input, client
    chat_input = client.run("join_class scout")
    return chat_input


def medic():
    global chat_input, client
    chat_input = client.run("join_class medic")
    return chat_input


def demoman():
    global chat_input, client
    chat_input = client.run("join_class demoman")
    return chat_input


def pyro():
    global chat_input, client
    chat_input = client.run("join_class pyro")
    return chat_input


def engineer():
    global chat_input, client
    chat_input = client.run("join_class engineer")
    return chat_input


def sniper():
    global chat_input, client
    chat_input = client.run("join_class sniper")
    return chat_input


def spy():
    global chat_input, client
    chat_input = client.run("join_class spy")
    return chat_input


def soldier():
    global chat_input, client
    chat_input = client.run("join_class soldier")
    return chat_input


def heavy():
    global chat_input, client
    chat_input = client.run("join_class heavyweapons")
    return chat_input


"""
Dear dev,
Be attracted to who you are attracted to.
sincerely
Birch
"""

# set up the bot
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)


# Twitch chat commands
@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ["CHANNEL"], f"/me has landed!")


@bot.event
async def event_message(ctx):
    """Runs every time a message is sent in chat."""

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)

    if 'hello' in ctx.content.lower():
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")


@bot.command(name='attack')
async def jumper(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        attack()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='alt')
async def alt_attack(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        attack()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='right')
async def righter(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        attack()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='left')
async def lefter(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        attack()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='forward')
async def righter(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        forward()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='back')
async def backer(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        back()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='jump')
async def jumper(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        jump()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='use')
async def user(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        use()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='random loadout')
async def rand_loader(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        rand_loadout()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='taunt')
async def taunt(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        rand_loadout()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='!MEDIC')
async def backer(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        help()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='scout')
async def scouter(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        scout()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='medic')
async def medicer(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        medic()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='demoman')
async def demomaner(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        demoman()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='pyro')
async def pyroer(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        pyro()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='engineer')
async def engineerer(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        engineer()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='sniper')
async def sniperer(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        sniper()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='spy')
async def spyer(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        spy()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='soldier')
async def soldierer(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        soldier()
    print(chat_input)
    await ctx.send('E')


@bot.command(name='heavy')
async def heavyer(ctx):
    with Client('127.0.0.1', 55636, passwd='FunnyPasswordForNerds') as client:
        heavy()
    print(chat_input)
    await ctx.send('E')


if __name__ == "__main__":
    bot.run()
