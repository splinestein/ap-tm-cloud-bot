import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '-------')

@client.event
async def on_message(message):

    if message.channel.id == 710945711449178213:
        #if msg from tm, send to ap sign in channel or whatever tm sign in channel they will have.
        channel = client.get_channel(710946067549782146)
        await channel.send(str(message.content))
    if message.channel.id == 710945675357061254:
        channel = client.get_channel(710946203545632811)
        await channel.send(str(message.content))

client.run('NzEwOTM4ODQwOTIzMjQyNTI3.Xr7xzw.rlIQdTmKnifHE4Se2kd_pHOMwzU')