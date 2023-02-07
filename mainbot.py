import pkg_resources
__requires__= 'discord==1.7.3'
import pkg_resources
pkg_resources.require("discord==1.7.3")
from discord.ext import commands
import discord,asyncio
#client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(intents=discord.Intents.all(),command_prefix="!", case_insensitive=True)
global vc,stor

print("Initiating Bot")


with open("interact.txt","w+",encoding="utf8") as interact: 
    with open("start.txt","r+",encoding="utf8") as start: 
        x=start.read()
    interact.write(x)


with open("interact.txt","r+",encoding="utf8") as interact: 
    z=interact.read()
stor={"interact":z}
with open("config.txt","r+",encoding="utf8") as interact: 
    z2=interact.read()
stor={"config":z2}


#functions
def locate(file,item,no): #file is which file to check,item is parameter, no is number of parameters
    para=stor[file]
    b=para.find(item+"=")+len(item)+1
    c=0
    for i in range(0,no):
        if i==0:
            a=(para.find("|;",para.find(item+"=")))
        elif i>0:
            a=(para.find("|;",b))
        if i==no-1:
            c=para[b:a]
        b=a+2
    return c

def replacing(file,item,no,word): #file is which file to check,item is parameter, no is number of parameters,word is what is goning to replace the og

    para=stor[file]
    b=para.find(item+"=")+len(item)+1
    for i in range(0,no):
        if i==0:
            a=(para.find("|;",para.find(item+"=")))
        elif i>0:
            a=(para.find("|;",b))
        if i==no-1:
            stor[file]=stor[file][:b]+stor[file][b:a].replace(para[b:a],word)+stor[file][a:]
            if file=="config":
                with open("config.txt","w+",encoding="utf8") as config:
                    config.write(stor[file])

            if file=="interact":
                with open("interact.txt","w+",encoding="utf8") as config:
                    config.write(stor[file])


        b=a+2
    if no==-1:
        a=len(stor[file][:b])+stor[file][b:].index("|;;")
        stor[file]=stor[file][:b]+stor[file][b:a].replace(para[b:a],word)+stor[file][a:]
        if file=="config":
            
            with open("config.txt","w+",encoding="utf8") as config:
                config.write(stor[file])


    pass



#client.run(token)

textChannelID=int(locate("config","TextChannel",1))
voiceChannelID=int(locate("config","VoiceChannel",1))
token=(locate("config","Token",1))




#use ctx for commands to call with !example, button commands dont use

@bot.command(pass_context=True)
async def aaa(ctx):
    print(discord.TextChannel._get_channel)
    print("DOne")
    

@bot.command(pass_context=True)
async def join(ctx):
    print("A")

@bot.command()
async def getmsg(ctx, channel: discord.TextChannel, member: discord.Member):
    msg = discord.utils.get(await bot.history(limit=100).flatten(), author=member)
    # this gets the most recent message from a specified member in the past 100 messages
         
@bot.command(pass_context=True)
async def leave(ctx):
    global vc
    await vc.disconnect()

#@bot.command(pass_context=True)
async def joiner():
    global vc
    #voice channel
    channel1 =bot.get_channel(voiceChannelID)

    #text channel
    channel2 = bot.get_channel(textChannelID)
    
    try:
        vc= await channel1.connect()
    except:
        await channel2.send("Already connected to a voice channel.")
    
async def messageSender():
       await textChannel.send()

        
#@bot.command(pass_context=True)
async def leaver():
    global vc
    channel2 = bot.get_channel(textChannelID)

    try:
        await vc.disconnect()
    except:
        await channel2.send("name 'vc' is not defined.")
    

     
#@bot.command(pass_context=True)
async def player(file):
    global vc
    try:
        vc.play(discord.FFmpegPCMAudio('sound_files/'+file))
    except:
        pass
@bot.command(pass_context=True)
async def pauser():
    global vc
    vc.pause()
@bot.command(pass_context=True)
async def unpauser():
    global vc
    vc.resume()

    
    

                

        
        
    

@bot.command(pass_context=True)
async def search_submissions():
    global vc,stor
    while(True):
        await bot.wait_until_ready()
        with open("interact.txt","r+",encoding="utf8") as interact:
            z=interact.read()
        stor={"interact":z}
        channel1 = bot.get_channel(textChannelID)
        
        if (locate("interact","status",1)=="starting"):
             
            await channel1.send("client start")
            print("Bot Online")
            replacing("interact","status",1,"offline0")

        if ((locate("interact","status",1)=="online1")):
            bot.loop.create_task(joiner())
            print("Started connection to Discord")
            replacing("interact","status",1,"online0")
            
        
        elif ((locate("interact","status",1)=="offline1")):
            await channel1.send("leaving")
            print("Discord Disconnected")
            bot.loop.create_task(leaver())
            
            replacing("interact","status",1,"offline0")
            
            
        try:
            if vc.is_connected():
                
                replacing("interact","connected",1,"True") 
            elif vc.is_connected()!=True:
                
                replacing("interact","connected",1,"False") 
            if vc.is_playing():
                replacing("interact","playstate",1,"True")
            elif not vc.is_playing():
                replacing("interact","playstate",1,"False")

            
        except:
            pass
        if locate("interact","player",1)=="play" and locate("interact","player",4)=="1":
            if locate("interact","playstate",1)=="False":
            
                bot.loop.create_task(player(locate("interact","player",2)))
                replacing("interact","player",4,"0")
            elif locate("interact","playstate",1)=="True":
                await channel1.send("Audio already playing")
            
        if locate("interact","player",1)=="pause" and locate("interact","player",4)=="1":
            bot.loop.create_task(pauser())
            replacing("interact","player",4,"0")
        elif locate("interact","player",1)=="unpause" and locate("interact","player",4)=="1":
            bot.loop.create_task(unpauser())
            replacing("interact","player",4,"0")
            
        
        await asyncio.sleep(0.03)
        
bot.loop.create_task(search_submissions())
#bot.add_command(check)

    
    




#client.run(token)
bot.run(token)



