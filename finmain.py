import discord
import time
from discord.ext import commands
from datetime import datetime

client = commands.Bot(command_prefix = '-')

msgids = []
temparray = []

#in case someone writes same time, we wanna use another temparray, like for every, do this later.

@client.event
async def on_message(message):

    global temparray
    global msgids

    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")

    #MESSAGE FROM LordDankStorm SIGN IN, TM.
    if message.channel.id == 692990720113639434:
        temparray.append(message)

        #--------------------------------
        #Send it to Zucker, AP
        channel = client.get_channel(711271480041668698)
        await channel.send(str("[TM] -> : ")+str(message.content)+" / discord: "+str(message.author)+" / @ -> "+str(dt_string))
        #Send it to Whacky, RED
        channel = client.get_channel(711210923192352840)
        await channel.send(str("[TM] -> : ")+str(message.content)+" / discord: "+str(message.author)+" / @ -> "+str(dt_string))
        #--------------------------------

        if len(temparray) == 3:
            msgids.append(temparray)
            temparray = []

    #MESSAGE FROM Zucker, AP.
    if message.channel.id == 698525731839279175:
        temparray.append(message)

        #--------------------------------
        #Send it to Lord
        channel = client.get_channel(711211043212492880)
        await channel.send(str("[AP] -> : ")+str(message.content)+" / discord: "+str(message.author)+" / @ -> "+str(dt_string))
        #Send it to Whacky.
        channel = client.get_channel(711210923192352840)
        await channel.send(str("[AP] -> : ")+str(message.content)+" / discord: "+str(message.author)+" / @ -> "+str(dt_string))
        #--------------------------------

        if len(temparray) == 3:
            msgids.append(temparray)
            temparray = []

    #MESSAGE FROM Whacky, RED.
    if message.channel.id == 701673305647743006:
        temparray.append(message)

        #--------------------------------
        #Send it to Lord.
        channel = client.get_channel(711211043212492880)
        await channel.send(str("[RED] -> : ")+str(message.content)+" / discord: "+str(message.author)+" / @ -> "+str(dt_string))
        #Send it to Zucker.
        channel = client.get_channel(711271480041668698)
        await channel.send(str("[RED] -> : ")+str(message.content)+" / discord: "+str(message.author)+" / @ -> "+str(dt_string))
        #--------------------------------

        if len(temparray) == 3:
            msgids.append(temparray)
            temparray = []





    #When bot writes to, we store them. Lord, Zucker, Whacky servers.
    if message.channel.id == 711211043212492880:
        temparray.append(message)
        #temparray = [tmorigin, ap-allysignin]
        if len(temparray) == 3:
            msgids.append(temparray)
            temparray = []

    if message.channel.id == 711271480041668698:
        temparray.append(message)
        #temparray = [tmorigin, ap-allysignin]
        if len(temparray) == 3:
            msgids.append(temparray)
            temparray = []

    if message.channel.id == 711210923192352840:
        temparray.append(message)
        #temparray = [tmorigin, ap-allysignin]
        if len(temparray) == 3:
            msgids.append(temparray)
            temparray = []

@client.event
async def on_message_delete(message):

    #If someone in LORD deletes their sign in vvv. proceed normally
    if message.channel.id == 692990720113639434:
        for x in msgids:
            if message in x:
                indexoffound = x.index(message)
                if indexoffound == 0:
                    #if our original tm login got deleted, we wanna respectively delete both ap and red ally thingies.
                    #However, if someone deleted the bot messages it prolly wont find one of these.
                    #Lets try though.

                    try:
                        #Delete from AP ally-sign-in.
                        deletethis = x[1]
                        channel = client.get_channel(711271480041668698)
                        msg = deletethis
                        await msg.delete()
                    except:
                        pass
                    try:
                        deletethis2 = x[2]
                        #Delete from RED ally-sign-in.
                        channel = client.get_channel(711210923192352840)
                        msg = deletethis2
                        await msg.delete()
                    except:
                        pass

                    #Should be the correct array order ^

                    msgids.remove(x) #we clear the entire array.

#---------------------------------------------------------

    #If someone in Zucker deletes their sign in vvv. proceed normally
    if message.channel.id == 698525731839279175:
        for x in msgids:
            if message in x:
                indexoffound = x.index(message)
                if indexoffound == 0:

                    try:
                        #RED
                        deletethis = x[1]
                        channel = client.get_channel(711211043212492880)
                        msg = deletethis
                        await msg.delete()
                    except:
                        pass
                    try:
                        #tm
                        deletethis2 = x[2]
                        channel = client.get_channel(711210923192352840)
                        msg = deletethis2
                        await msg.delete()
                    except:
                        pass

                    #Should be the correct array order ^

                    msgids.remove(x) #we clear the entire array since everything went WELL.
#---------------------------------------------------------
    #If someone in Whacky deletes their sign in vvv. proceed normally
    if message.channel.id == 701673305647743006:
        for x in msgids:
            if message in x:
                indexoffound = x.index(message)
                if indexoffound == 0:

                    try:
                        #TM
                        deletethis = x[1]
                        channel = client.get_channel(711211043212492880)
                        msg = deletethis
                        await msg.delete()
                    except:
                        pass
                    try:
                        #ap
                        deletethis2 = x[2]
                        channel = client.get_channel(711271480041668698)
                        msg = deletethis2
                        await msg.delete()
                    except:
                        pass

                    #Should be the correct array order ^

                    msgids.remove(x) #we clear the entire array since everything went WELL.

    #If gets deleted in Lords ally sign in ?
    if message.channel.id == 711211043212492880:
        for x in msgids:
            if message in x:
                try:
                    indexoffound = x.index(message)
                    if indexoffound == 2:
                        msgids.remove(x[2])
                    if indexoffound == 1:
                        msgids.remove(x[1])
                    if indexoffound == 0:
                        msgids.remove(x[0])
                except:
                    pass
    #in Zuckerss ally sign in?
    if message.channel.id == 711271480041668698:
        for x in msgids:
            if message in x:
                try:
                    indexoffound = x.index(message)
                    if indexoffound == 2:
                        msgids.remove(x[2])
                    if indexoffound == 1:
                        msgids.remove(x[1])
                    if indexoffound == 0:
                        msgids.remove(x[0])
                except:
                    pass
    #in Whackys ally sign in?
    if message.channel.id == 711210923192352840:
        for x in msgids:
            if message in x:
                try:
                    indexoffound = x.index(message)
                    if indexoffound == 2:
                        msgids.remove(x[2])
                    if indexoffound == 1:
                        msgids.remove(x[1])
                    if indexoffound == 0:
                        msgids.remove(x[0])
                except:
                    pass
client.run('NzEwOTM4ODQwOTIzMjQyNTI3.Xr7xzw.rlIQdTmKnifHE4Se2kd_pHOMwzU')
