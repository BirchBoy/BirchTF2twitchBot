import random
from time import sleep

from twitchio.ext import commands
from rcon import Client

# Settings for how long a command will last.

# Account stuff
username = "borchboy"
tw_token = 'y3lxl3uxpghaqq2u2yrgy4cs96ipss'
# The prefix prefix can be anything. here are some examples: ! @ # $ % % ^ & * < > ?
tw_prefix = "#"

# Networking
tf_ip = "127.0.0.1"
tf_port = 55635
tf_password = "FunnyPasswordForNerds"

# Timing for the commands
movement_time = int(2)
attack_time = int(3)
look_time = int(1)
medic_call_time = int(30)
# 0-1 not yet added.
taunt_active = int(0)
random_class = int(0)


def attackC():
    global chat_input, client, attack_time
    chat_input = client.run("say_party \"Used Attack1")
    chat_input = client.run("+attack")
    sleep(attack_time)
    chat_input = client.run("-attack")
    return chat_input


def attack2C():
    global chat_input, client, attack_time
    chat_input = client.run("say_party \"Used Attack2")
    chat_input = client.run("+attack2")
    sleep(attack_time)
    chat_input = client.run("-attack2")
    return chat_input


def rightC():
    global chat_input, client, look_time
    chat_input = client.run("say_party \"Used Right")
    chat_input = client.run("+right")
    sleep(look_time)
    chat_input = client.run("-right")
    return chat_input


def leftC():
    global chat_input, client, look_time
    client.run("say_party \"Used Left")
    chat_input = client.run("+left")
    sleep(look_time)
    chat_input = client.run("-left")
    return chat_input


def forwardC():
    global chat_input, client, movement_time
    client.run("say_party \"Used Forward")
    chat_input = client.run("+forward")
    sleep(movement_time)
    chat_input = client.run("-forward")
    return chat_input


def backC():
    global chat_input, client, movement_time
    client.run("say_party \"Used Backwards")
    chat_input = client.run("+back")
    sleep(movement_time)
    chat_input = client.run("-back")
    return chat_input


def jumpC():
    global chat_input, client
    client.run("say_party \"Used Jump")
    chat_input = client.run("+jump")
    sleep(1)
    chat_input = client.run("-jump")
    return chat_input


def useC():
    global chat_input, client
    client.run("say_party \"Used Use")
    chat_input = client.run("+use_action_slot_item")
    sleep(1)
    chat_input = client.run("-use_action_slot_item")
    return chat_input


def rand_loadoutC():
    rand_load = random.randint(1, 4)
    client.run("say_party \"Used Random Loadout {}".format(rand_load))
    chat_input = client.run("load_itempreset {}".format(rand_load))
    return chat_input


def tauntC():
    client.run("say_party \"Used Taunt")
    chat_input = client.run("taunt")
    return chat_input


def helpC():
    global chat_input, client
    client.run("say_party \"Used HELP!")
    count = medic_call_time
    while count > 0:
        count = count - 1
        chat_input = client.run("voicemenu 0 0")
        sleep(2)
    return chat_input


def scoutC():
    global chat_input, client
    client.run("say_party \"Used Scout")
    chat_input = client.run("join_class scout")
    return chat_input


def medicC():
    global chat_input, client
    client.run("say_party \"Used Medic")
    chat_input = client.run("join_class medic")
    return chat_input


def demomanC():
    global chat_input, client
    client.run("say_party \"Used Demoman")
    chat_input = client.run("join_class demoman")
    return chat_input


def pyroC():
    global chat_input, client
    client.run("say_party \"Used Pyro")
    chat_input = client.run("join_class pyro")
    return chat_input


def engineerC():
    global chat_input, client
    client.run("say_party \"Used Engineer Gaming")
    chat_input = client.run("join_class engineer")
    return chat_input


def sniperC():
    global chat_input, client
    client.run("say_party \"Used Sniper")
    chat_input = client.run("join_class sniper")
    return chat_input


def spyC():
    global chat_input, client
    client.run("say_party \"Used Spy")
    chat_input = client.run("join_class spy")
    return chat_input


def soldierC():
    global chat_input, client
    client.run("say_party \"Used Soldier")
    chat_input = client.run("join_class soldier")
    return chat_input


def heavyC():
    global chat_input, client
    client.run("say_party \"Used Heavy")
    chat_input = client.run("join_class heavyweapons")
    return chat_input


class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=tw_token, prefix=tw_prefix, initial_channels=[tw_username])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    @commands.command()
    async def stop(self, ctx: commands.Context):
        await ctx.send("{0} Used stop program stopping.".format(ctx.author.name))
        sleep(1)
        await ctx.send("3")
        sleep(1)
        await ctx.send("2")
        sleep(1)
        await ctx.send("1")
        sleep(1)
        await ctx.send("Program terminated")

    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send("{0} Used Help".format(ctx.author.name))

    @commands.command()
    async def attack1(self, ctx: commands.Context):
        await ctx.send("{0} Used Attack1!".format(ctx.author.name))
        attackC()

    @commands.command()
    async def attack2(self, ctx: commands.Context):
        await ctx.send("{0} Used Attack2!".format(ctx.author.name))
        attack2C()

    @commands.command()
    async def right(self, ctx: commands.Context):
        await ctx.send("{0} Used Right!".format(ctx.author.name))
        rightC()

    @commands.command()
    async def left(self, ctx: commands.Context):
        await ctx.send("{0} Used Left!".format(ctx.author.name))
        leftC()

    @commands.command()
    async def forward(self, ctx: commands.Context):
        await ctx.send("{0} Used Forward!".format(ctx.author.name))
        forwardC()

    @commands.command()
    async def back(self, ctx: commands.Context):
        await ctx.send("{0} Used Back!".format(ctx.author.name))
        backC()

    @commands.command()
    async def jump(self, ctx: commands.Context):
        await ctx.send("{0} Used Jump!".format(ctx.author.name))
        jumpC()


with Client(tf_ip, tf_port, passwd=tf_password) as client:
    bot = Bot()
    bot.run()
