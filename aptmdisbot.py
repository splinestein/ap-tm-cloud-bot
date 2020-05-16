import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '-------')

#tm ally sign #711211043212492880
#red ally sign #711210923192352840



#698525731839279175


#ap ally sign-ins channel #711271480041668698
@client.event
async def on_message(message):
#692990720113639434

#when sign in comes from red
    if message.channel.id == 701673305647743006:

        #Send it to TM.
        channel = client.get_channel(711211043212492880)
        await channel.send(str("[RED] -> : ")+str(message.content)+" | Discord User : "+str(message.author))

        #Send it to AP.
        channel = client.get_channel(711271480041668698)
        await channel.send(str("[RED] -> : ")+str(message.content)+" | Discord User : "+str(message.author))


#Aps sign in
    if message.channel.id == 698525731839279175:

        #Send it to RED
        channel = client.get_channel(711210923192352840)
        await channel.send(str("[AP] -> : ")+str(message.content)+" | Discord User : "+str(message.author))

        #Send it to TM.
        channel = client.get_channel(711211043212492880)
        await channel.send(str("[AP] -> : ")+str(message.content)+" | Discord User : "+str(message.author))


#TM sign in
    if message.channel.id == 692990720113639434:

        #Send it to AP
        channel = client.get_channel(711271480041668698)
        await channel.send(str("[TM] -> : ")+str(message.content)+" | Discord User : "+str(message.author))

        #Send it to RED
        channel = client.get_channel(711210923192352840)
        await channel.send(str("[TM] -> : ")+str(message.content)+" | Discord User : "+str(message.author))


client.run('NzEwOTM4ODQwOTIzMjQyNTI3.Xr7xzw.rlIQdTmKnifHE4Se2kd_pHOMwzU')