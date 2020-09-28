import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("bot ready")

@client.command()
async def hi(ctx):
    await ctx.send("hi")
@client.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  
        member = ctx.message.author  
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)
 async def ban(ctx, member : discord.Member, reason=None):
    """Bans a user"""
    if reason == None:
        await ctx.send(f"Woah {ctx.author.mention}, Make sure you provide a reason!")
    else:
        messageok = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(messageok)
        await member.ban(reason=reason)
 client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!clear'):
        tmp = await client.send_message(message.channel, 'Clearing messages...')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)
@commands.command(pass_context = True)
    async def poll(self, ctx, question, *options: str):
        author = ctx.message.author
        server = ctx.message.server

        if not author.server_permissions.manage_messages: return await self.bot.say(DISCORD_SERVER_ERROR_MSG)

        if len(options) <= 1:
            await self.bot.say("```Error! A poll must have more than one option.```")
            return
        if len(options) > 2:
            await self.bot.say("```Error! Poll can have no more than two options.```")
            return

        if len(options) == 2 and options[0] == "yes" and options[1] == "no":
            reactions = ['👍', '👎']
        else:
            reactions = ['👍', '👎']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)

        embed = discord.Embed(title = question, color = 3553599, description = ''.join(description))

        react_message = await self.bot.say(embed = embed)

        for reaction in reactions[:len(options)]:
            await self.bot.add_reaction(react_message, reaction)

        embed.set_footer(text='Poll ID: {}'.format(react_message.id))

        await self.bot.edit_message(react_message, embed=embed)
server = ctx.message.server
roles = [x.name for x in server.role_hierarchy]
role_length = len(roles)

if role_length > 50: 
    roles = roles[:50]
    roles.append('>>>> [50/%s] Roles'%len(roles))

roles = ', '.join(roles);
channelz = len(server.channels);
time = str(server.created_at); time = time.split(' '); time= time[0];

join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', colour = 0xFFFF);
join.set_thumbnail(url = server.icon_url);
join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
join.add_field(name = '__ID__', value = str(server.id))
join.add_field(name = '__Member Count__', value = str(server.member_count));
join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
join.set_footer(text ='Created: %s'%time);

return await bot.say(embed = join);

@client.run("token")
