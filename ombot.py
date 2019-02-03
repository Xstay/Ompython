import discord
from discord.ext import commands
import asyncio
import platform
import colorsys
import random
from discord.voice_client import VoiceClient
import youtube_dl
from discord.ext.commands.cooldowns import BucketType
from discord import Game, Embed, Color, Status, ChannelType


bot = commands.Bot(command_prefix='%')
bot.remove_command('help')

@bot.event
async def on_ready( ) :
	await bot.change_presence(game=discord.Game(name='in '+str(len(bot.servers))+' servers With %help'))
	print('The Bot Online')

@bot.event
async def on_message(message):
	await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    print("In our server" + member.name + " just joined")
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Welcome message')
    embed.add_field(name = '__Welcome to Our Server__',value ='**Hope you will be active here. Check Our server rules and never try to break any rules. ',inline = False)
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    await bot.send_message(member,embed=embed)
    print("Sent message to " + member.name)
    channel = discord.utils.get(bot.get_all_channels(), server__name='CASINO [GTSG]', name='👐wellcome-left👋')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check Rules and never try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
    embed.add_field(name='Your join position is', value=member.joined_at)
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    embed.set_thumbnail(url=member.avatar_url)
    await bot.send_message(channel, embed=embed)




@bot.command(pass_context = True)
async def uncle(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await bot.say("Please specify a user to wish")
    await bot.say('Its You ' + msg + ' \nhttps://colinbendell.cloudinary.com/image/upload/c_crop,f_auto,g_auto,h_350,w_400/v1512090971/Wizard-Clap-by-Markus-Magnusson.gif')
    return



@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await bot.delete_message(ctx.message)

    if not msg: await bot.say("Please specify a message to send")
    else: await bot.say(msg)
    return

@bot.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member):
    """User Avatar"""
    await bot.reply("{}".format(member.avatar_url))

@bot.command(pass_context=True, no_pm=True)
async def servericon(ctx):
    """Guild Icon"""
    await bot.reply("{}".format(ctx.message.server.icon_url))

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)

async def unbanall(ctx):
    server=ctx.message.server
    ban_list=await client.get_bans(server)
    await bot.say('Unbanning {} members'.format(len(ban_list)))
    for member in ban_list:
        await bot.unban(server,member)

@bot.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = '``Our Help Server Link`` ',value ='https://ombot.simdif.com',inline = False)
    embed.add_field(name = '%help ',value ='Explaines all the commands which are only usable by Those who has moderation permissions. Like- Manage Nicknames, Manage Messages, Kick/Ban Members,etc.',inline = False)
    embed.add_field(name = 'Bot Developer:OmGila',value ='Sorry The command has repaired.',inline = False)
    await bot.send_message(author,embed=embed)
    await bot.say('📨 Check DMs For Information')

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True) 
async def roles(context):
	"""Displays all of the roles with their ids"""
	roles = context.message.server.roles
	result = "The roles are "
	for role in roles:
		result += '``' + role.name + '``' + ": " + '``' + role.id + '``' + "\n "
	await bot.say(result)
	
@bot.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):
 
    if ctx.message.author.server_permissions.manage_messages:
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)            
       
    try:
        await bot.delete_messages(mgs)          
        await bot.say(str(number)+' messages deleted')
     
    except discord.Forbidden:
        await bot.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await bot.say('clear failed.')
        return         

@bot.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):

    if user.server_permissions.kick_members:
        await bot.say('**He is mod/admin and i am unable to kick him/her**')
        return
    
    try:
        await bot.kick(user)
        await bot.say(user.name+' was kicked. Good bye '+user.name+'!')
        await bot.delete_message(ctx.message)

    except discord.Forbidden:
        await bot.say('Permission denied.')
        return

@bot.command(pass_context = True)
@commands.has_permissions(send_messages=True)     
async def whois(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)  
@commands.has_permissions(kick_members=True)      
async def ban(ctx,user:discord.Member):

    if user.server_permissions.ban_members:
        await bot.say('**He is mod/admin and i am unable to ban him/her**')
        return

    try:
        await bot.ban(user)
        await bot.say(user.name+' was banned. Good bye '+user.name+'!')

    except discord.Forbidden:

        await bot.say('Permission denied.')
        return
    except discord.HTTPException:
        await bot.say('ban failed.')
        return		 

@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str): 
    await bot.send_message(userName, "You have been warned for: **{}**".format(message))
    await bot.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
    pass

@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True) 

@commands.cooldown(rate=5,per=86400,type=BucketType.user) 
async def access(ctx, member: discord.Member):
    role = discord.utils.get(member.server.roles, name='Access')
    await bot.add_roles(member, role)
    embed=discord.Embed(title="User Got Access!", description="**{0}** got access from **{1}**!".format(member, ctx.message.author), color=0xff00f6)
    await bot.say(embed=embed)
    await asyncio.sleep(45*60)
    await bot.remove_roles(member, role)

@bot.command(pass_context = True)
@commands.has_permissions(manage_server=True)     
async def setnick(ctx, user: discord.Member, *, nickname):
    await bot.change_nickname(user, nickname)
    await bot.delete_message(ctx.message)
    
    await bot.say('NickName Has Changed')

@bot.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     


async def unban(ctx):
    ban_list = await bot.get_bans(ctx.message.server)

    # Show banned users
    await bot.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
    	
        await bot.say('Ban list is empty.')
        return
    try:
        await client.unban(ctx.message.server, ban_list[-1])
        await bot.say('Unbanned user: `{}`'.format(ban_list[-1].name))
    except discord.Forbidden:
        await bot.say('Permission denied.')
        return
    except discord.HTTPException:
        await bot.say('unban failed.')
        return		

@bot.command()
async def ping():
	await bot.say('Hi Im OmGila Developer This BOT')
	
@bot.command(pass_context=True, aliases=['server'])
@commands.has_permissions(create_instant_invite=True)
async def membercount(ctx, *args):
    """
    Shows stats and information about current guild.
    ATTENTION: Please only use this on your own guilds or with explicit
    permissions of the guilds administrators!
    """
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="MemberCount")
    em.description =    "```\n" \
                        "Members:   %s online: (%s)\n" \
                        "  Users:   %s online: (%s)\n" \
                        "  Bots:    %s online:  (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await bot.send_message(ctx.message.channel, embed=em)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)  
@commands.has_permissions(manage_messages=True)     

async def serverinfo(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color = discord.Color((r << 16) + (g << 8) + b));
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await bot.say(embed = join);

@bot.command(pass_context = True)
async def happybirthday(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await bot.say("Please specify a user to wish")
    await bot.say('Happy birthday ' + msg + ' \nhttps://asset.holidaycardsapp.com/assets/card/b_day399-22d0564f899cecd0375ba593a891e1b9.png')
    return
	
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def friend(ctx, user:discord.Member,):
    await bot.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Friend of Owner')
    await bot.add_roles(ctx.message.mentions[0], role)
	
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def rules(ctx, *, msg = None):
    await bot.delete_message(ctx.message)
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await bot.say("Please specify a user to warn")
    else: await bot.say(msg + ', Please Read Rules again and never break any one of them again otherwise i will mute/kick/ban you next time.')
    return
    
@bot.command(pass_context=True)
async def devbot(ctx):
    embed = discord.Embed(title="Information about owner", description="Bot Name- OmBOT", color=0x00ff00)
    embed.set_footer(text="Copyright@UK Soft")
    embed.set_author(name=" Bot Owner Name- OmGila#4069,|OmGila Singh|™✓#4856,Tag<!--Back-->#MeMei,SNSW,MegumiN")
    embed.add_field(name="Site-", value="Thanks for adding our bot", inline=True)
    await bot.say(embed=embed)
	
@bot.command()
async def info():
	await bot.say('`Server CASINO [GTSG]`                             *Made-by :OmGila#4069.                                                    Asist Owner:SNSW#8494.                                       Co-Owner:MeiMei#0003 and Megumin#7624*')                                             
	
bot.run('NTM2NDA4NjA0ODExNzIyNzUz.DzBLYQ.jZsH_Fq6ITtldRyuItXMd_pkx3I')
