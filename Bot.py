"""
    File name: Bot.py
    Author: Liam Brennan
    Date created: 8/1/2021
    Date last modified: 03/04/2024
    Python Version: 3.12
"""

import random
import string
import threading
import configparser
import os
from time import sleep
from twitchio.ext import commands
from rcon import source, client


# Account stuff
twitch_username: str
twitch_token: str

# The prefix can be anything. here are some examples: ! # $ % % ^ & * < > ?
twitch_prefix: str = '!'

# Network information
source_rcon_ip: str = "127.0.0.1"
source_rcon_port: int
source_rcon_password: str

# Command activation periods
movement_time: float = 1.0
attack1_time: float = 3.0
attack2_time: float = 1.0
look_time: float = 0.45
medic_call_time: float = 20

# Points
points_time = int(60)
points_amount = int(100)
join_points = int(200)

# Points pricing
attack_points = int(50)
move_points = int(100)
look_points = int(100)
class_points = int(200)
sp_points = int(200)

points_users = dict({
})

    
def get_config_info(path: str) -> None:
    global twitch_username, twitch_token, twitch_prefix, source_rcon_ip, source_rcon_port, source_rcon_password
    config = configparser.ConfigParser()
    if os.path.exists(path):
        config.read(path)
        twitch_username = config.get('Twitch Information', 'Username')
        twitch_token = config.get('Twitch Information', 'Token')
        twitch_prefix = config.get('Twitch Information', 'Prefix')
        source_rcon_ip = config.get('Network information', 'RconIP')
        source_rcon_port = int(config.get('Network information', 'RconPort'))
        source_rcon_password = config.get('Network information', 'RconPassword')
    else:
        config.add_section("Twitch Information")
        config.set('Twitch Information', 'Username', "USERNAME")
        config.set('Twitch Information', 'Token', "TOKEN")
        config.set('Twitch Information', 'Prefix', "!")

        config.add_section("Network information")
        config.set('Network information', 'RconIP', "127.0.0.1")
        config.set('Network information', 'RconPort', str(random.randrange(40000,60000)))
        config.set('Network information', 'RconPassword', random_string(15))
        
        with open(path, 'w') as configfile:
            config.write(configfile)

        breakpoint

    print(config)
    write_launch_options()
    return None


def write_launch_options() -> None:
    format : str = """//Rcon for client to interact with programs
//Needed launch options: -usercon -condebug -conclearlog +exec rcon.cfg
developer 1 
alias developer 
contimes 0 
alias contimes 
ip 0.0.0.0 
alias ip 
sv_rcon_whitelist_address {0}
alias sv_rcon_whitelist_address 
sv_quota_stringcmdspersecond 1000000 
alias sv_quota_stringcmdspersecond 
rcon_password {1}
alias rcon_password
hostport {2} 
alias hostport 
alias cl_reload_localization_files 
net_start 
con_timestamp 1 
alias con_timestamp 
// +ip 0.0.0.0 +rcon_password FunnyPasswordForNerds +hostport 55635""".format(source_rcon_ip,source_rcon_password, source_rcon_port)
    open("rcon.cfg", "w").write(format)
    return None

def random_string(length) -> str:
    letters: str = string.ascii_letters
    return "".join(random.choice(letters) for i in range(length))


def add_all():
    while True:
        for key in points_users.keys():
            points_users[key] += points_amount
            sleep(points_time)


def user_join(username_chat, points):
    points_users.update({username_chat: points})
    return points_users


def spend(username_chat, cost) -> bool:
    error: bool = False
    points: int = points_users.get(username_chat)
    if points >= cost:
        points_users.update({username_chat: points - cost})
    else:
        error = True
    return error


def command_catch_all(command: str, time_active: float = 0.1, command_type: int = 0) -> None:
    client.run("say_party \"Used {0}".format(command))

    match command_type:
        case 0:
            client.run("+{0}".format(command))
            sleep(time_active)
            client.run("-{0}".format(command))

        case 1:
            client.run(str(command))

        case 2:
            client.run(str(command))
            sleep(time_active)
            client.run(str(command))


def command_random_loadout() -> None:
    rand_load = random.randint(1, 4)
    client.run("say_party \"Used Random Loadout {0}".format(rand_load))
    client.run("load_itempreset {0}".format(rand_load))
    return None


def command_voicemenu(index0: int = 0, index1: int = 0) -> None:
    client.run("say_party \"Used voiceline {0} {1}".format(index0, index1))
    client.run("voicemenu {0} {1}".format(index0, index1))
    return None


async def command_select_class(index: int = 0) -> bool:
    class_name: str
    match index:
        case 1:
            class_name = "scout"
        case 2:
            class_name = "soldier"
        case 3:
            class_name = "pyro"
        case 4:
            class_name = "demoman"
        case 5:
            class_name = "heavyweapons"
        case 6:
            class_name = "engineer"
        case 7:
            class_name = "medic"
        case 8:
            class_name = "sniper"
        case 9:
            class_name = "spy"
        case other:
            return True

    await client.run("join_class {0}".format(class_name))
    return False


# The Twitch part of this.
class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=twitch_token, prefix=twitch_prefix, initial_channels=[twitch_username])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    @commands.command()
    async def add(self, ctx: commands.Context):
        user_join(username_chat=ctx.author.name, points=join_points)
        await ctx.send("Added {0}, You have {1:.0f} points!".format(ctx.author.name, points_users[ctx.author.name]))

    @commands.command()
    async def points(self, ctx: commands.Context):
        await ctx.send("{0}, You have {1:.0f} points!".format(ctx.author.name, points_users[ctx.author.name]))
        print("{0} has {1} points.".format(ctx.author.name, points_users[ctx.author.name]))

    @commands.command()
    async def attack(self, ctx: commands.Context):
        error_spend: bool = spend(username_chat=ctx.author.name, cost=sp_points)
        if error_spend:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used {1}!".format(ctx.author.name, ctx.command.name))
            command_catch_all("attack", attack1_time, 0)

    @commands.command()
    async def attack2(self, ctx: commands.Context):
        error_spend: bool = spend(username_chat=ctx.author.name, cost=sp_points)
        if error_spend:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used {1}!".format(ctx.author.name, ctx.command.name))
            command_catch_all("attack2", attack2_time, 0)

    @commands.command()
    async def lookright(self, ctx: commands.Context):
        error_spend: bool = spend(username_chat=ctx.author.name, cost=sp_points)
        if error_spend:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used {1}!".format(ctx.author.name, ctx.command.name))
            command_catch_all("right", movement_time, 0)

    @commands.command()
    async def lookleft(self, ctx: commands.Context):
        error_spend: bool = spend(username_chat=ctx.author.name, cost=sp_points)
        if error_spend:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used {1}!".format(ctx.author.name, ctx.command.name))
            command_catch_all("left", movement_time, 0)

    @commands.command()
    async def forward(self, ctx: commands.Context):
        error_spend: bool = spend(username_chat=ctx.author.name, cost=sp_points)
        if error_spend:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used {1}!".format(ctx.author.name, ctx.command.name))
            command_catch_all("forward", movement_time, 0)

    @commands.command()
    async def back(self, ctx: commands.Context):
        error_spend: bool = spend(username_chat=ctx.author.name, cost=sp_points)
        if error_spend:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used {1}!".format(ctx.author.name, ctx.command.name))
            command_catch_all("back", movement_time, 0)

    @commands.command()
    async def right(self, ctx: commands.Context):
        error_spend: bool = spend(username_chat=ctx.author.name, cost=sp_points)
        if error_spend:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used {1}!".format(ctx.author.name, ctx.command.name))
            command_catch_all("moveright", movement_time, 0)

    @commands.command()
    async def left(self, ctx: commands.Context):
        error_spend: bool = spend(username_chat=ctx.author.name, cost=sp_points)
        if error_spend:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used {1}!".format(ctx.author.name, ctx.command.name))
            command_catch_all("moveleft", movement_time, 0)

    @commands.command()
    async def jump(self, ctx: commands.Context):
        error_spend: bool = spend(username_chat=ctx.author.name, cost=sp_points)
        if error_spend:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used {1}!".format(ctx.author.name, ctx.command.name))
            command_catch_all("jump", movement_time, 0)

    @commands.command()
    async def useitem(self, ctx: commands.Context):
        error_spend: bool = spend(username_chat=ctx.author.name, cost=sp_points)
        if error_spend:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used {1}!".format(ctx.author.name, ctx.command.name))
            command_catch_all("use_action_slot_item", 0.1, 0)

    @commands.command()
    async def randomloadout(self, ctx: commands.Context):
        error_spend: bool = spend(username_chat=ctx.author.name, cost=sp_points)
        if error_spend:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used {1}!".format(ctx.author.name, ctx.command.name))
            command_random_loadout()

    @commands.command()
    async def taunt(self, ctx: commands.Context):
        error_spend: bool = spend(username_chat=ctx.author.name, cost=sp_points)
        if error_spend:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used {1}!".format(ctx.author.name, ctx.command.name))
            command_catch_all("taunt", 0.1, 2)

    @commands.command()
    async def select_class(self, ctx: commands.Context, index: int):
        error_spend: bool = spend(username_chat=ctx.author.name, cost=sp_points)
        if error_spend:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used {1}!".format(ctx.author.name, ctx.command.name))
            error_command: int = command_select_class(index)
            if error_command:
                spend(username_chat=ctx.author.name, cost=-sp_points)
                await ctx.send("{0} that is an invalid input!".format(ctx.author.name))

    @commands.command()
    async def voicemenu(self, ctx: commands.Context, index0: int = 0, index1: int = 0):
        error_spend: bool = spend(username_chat=ctx.author.name, cost=sp_points)
        if error_spend:
            await ctx.send("{0} you don't have enough points!".format(ctx.author.name))
        else:
            await ctx.send("{0} Used {1}!".format(ctx.author.name, ctx.command.name))
            command_voicemenu(index0, index1)


if __name__ == "__main__":
    # Threading  that deals with giving points.

    get_config_info("config.cfg")
    threading.Thread(target=add_all).start()
    points_users.update({twitch_username: 999999})
    with source.Client(source_rcon_ip, source_rcon_port, passwd=source_rcon_password) as client:
        bot = Bot()
        bot.run()
