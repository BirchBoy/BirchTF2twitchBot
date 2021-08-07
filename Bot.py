"""
    File name: Bot.py
    Author: BirchBoy
    Steam_id:[U:1:355965976]
    Date created: 8/1/2021
    Date last modified: 8/7/2021
    Python Version: 3.9

    Author Comments:
    This program is a twitch bot that interacts with tf2 using the RCON* protocol which allows tf2 to host a port for
    clients to connect to ei this program.
"""

import random
from time import sleep
from twitchio.ext import commands
from rcon import Client

# DO NOT EDIT THIS VAR.
s_error = 0


points_users = {
    "borchboy": 100000
}

# Account stuff
tw_username = "borchboy" # Just put your twitch id here.
tw_token = '' # Twitch chat token here.

# The prefix prefix can be anything. here are some examples: ! @ # $ % % ^ & * < > ?
# There are more just the ones I recommend.
tw_prefix = "#"

# Networking/RCON
tf_ip = "127.0.0.1"
tf_port = 55635
tf_password = "FunnyPasswordForNerds"

# Points
points_time = 60
points_amount = 100
join_points = 200

# Points pricing
attack_points = 50
move_points = 100
look_points = 100
class_points = 200
sp_points = 200

# Settings for how long a command will last.
movement_time = int(1)
attack1_time = int(3)
attack2_time = int(1)
look_time = float(0.45)
medic_call_time = int(20)


# Basic join things
def add_all():
    while True:
        for key in points_users.keys():
            points_users[key] += points_amount
            sleep(points_time)


def join(username_chat, points):
    points_users.update({username_chat: points})
    return points_users


def spend(username_chat, cost):
    global s_error
    num = points_users.get(username_chat)
    if num >= cost:
        num = num - cost
        points_users.update({username_chat: num})
    else:
        s_error = True
    return points_users, s_error


# Command defs.
def attackC():
    global chat_input, client, attack1_time
    chat_input = client.run("say_party \"Used Attack".format())
    chat_input = client.run("+attack")
    sleep(attack1_time)
    chat_input = client.run("-attack")
    return chat_input


def attack2C():
    global chat_input, client, attack2_time
    chat_input = client.run("say_party \"Used Attack2")
    chat_input = client.run("+attack2")
    sleep(attack2_time)
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
    client.run("say_party \"Used back")
    chat_input = client.run("+back")
    sleep(movement_time)
    chat_input = client.run("-back")
    return chat_input


def rstrafeC():
    global chat_input, client, movement_time
    client.run("say_party \"Used Rstrafe")
    chat_input = client.run("+moveright")
    sleep(movement_time)
    chat_input = client.run("-moveright")
    return chat_input


def lstrafeC():
    global chat_input, client, movement_time
    client.run("say_party \"Used Lstrafe")
    chat_input = client.run("+moveleft")
    sleep(movement_time)
    chat_input = client.run("-moveleft")
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
    client.run("say_party \"Used Random Loadout {}"
               .format(rand_load))
    chat_input = client.run("load_itempreset {}"
                            .format(rand_load))
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

    """
    Command with spend template
    
        @commands.command()
    async def points_template(self, ctx: commands.Context):
        global s_error
        spend(username_chat=ctx.author.name, cost=100)
        if s_error == 1:
            await ctx.send("{0}, you can't afford that, you have {1:.0f} points.".format(ctx.author.name, points_users[ctx.author.name]))
        else:
            await ctx.send("{0} it is done.".format(ctx.author.name))
            s_error = 0
    """
    @commands.command()
    async def add(self, ctx: commands.Context):
        join(username_chat=ctx.author.name, points=join_points)
        await ctx.send("Added {0}, You have {1:.0f} points!".format(ctx.author.name, points_users[ctx.author.name]))

    @commands.command()
    async def points(self, ctx: commands.Context):
        await ctx.send("{0}, You have {1:.0f} points!".format(ctx.author.name, points_users[ctx.author.name]))
        print("{0} has {1} points.".format(ctx.author.name, points_users[ctx.author.name]))

    @commands.command()
    async def attack(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=attack_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Attack!".format(ctx.author.name))
            attackC()

    @commands.command()
    async def attack2(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=attack_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Attack2!".format(ctx.author.name))
            attack2C()

    @commands.command()
    async def right(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=look_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Right!".format(ctx.author.name))
            rightC()

    @commands.command()
    async def left(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=look_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Left!".format(ctx.author.name))
            leftC()

    @commands.command()
    async def forward(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=move_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Forward!".format(ctx.author.name))
            forwardC()

    @commands.command()
    async def back(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=move_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Back!".format(ctx.author.name))
            backC()

    @commands.command()
    async def moveright(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=move_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Rstrafe!".format(ctx.author.name))
            rstrafeC()

    @commands.command()
    async def moveleft(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=move_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Lstrafe!".format(ctx.author.name))
            lstrafeC()

    @commands.command()
    async def jump(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=move_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Jump!".format(ctx.author.name))
            jumpC()

    @commands.command()
    async def use(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=sp_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Use!".format(ctx.author.name))
            useC()

    @commands.command()
    async def random_loadout(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=sp_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Random_Loadout!".format(ctx.author.name))
            rand_loadoutC()

    @commands.command()
    async def call_medic(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=sp_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Call_Medic!".format(ctx.author.name))
            helpC()

    @commands.command()
    async def scout(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=class_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Scout!".format(ctx.author.name))
            scoutC()

    @commands.command()
    async def medic(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=class_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Medic!".format(ctx.author.name))
            medicC()

    @commands.command()
    async def demoman(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=class_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Demoman!".format(ctx.author.name))
            demomanC()

    @commands.command()
    async def pyro(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=class_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Pyro!".format(ctx.author.name))
            pyroC()

    @commands.command()
    async def engineer(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=class_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Engineer!".format(ctx.author.name))
            engineerC()

    @commands.command()
    async def sniper(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=class_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Sniper!".format(ctx.author.name))
            sniperC()

    @commands.command()
    async def spy(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=class_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Spy!".format(ctx.author.name))
            spyC()

    @commands.command()
    async def soldier(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=class_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Soldier!".format(ctx.author.name))
            soldierC()

    @commands.command()
    async def heavy(self, ctx: commands.Context):
        spend(username_chat=ctx.author.name, cost=class_points)
        if s_error:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used Heavy!".format(ctx.author.name))
            heavyC()


with Client(tf_ip, tf_port, passwd=tf_password) as client:
    bot = Bot()
    bot.run()
