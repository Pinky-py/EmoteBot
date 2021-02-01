import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='e!', case_insensitive=True)

@bot.event
async def on_ready():
    print(bot.user.name+' activated')

@bot.command(aliases=['trigger'], description='UNLEASH THE EVIL', usage='[user(opt.)]')
async def triggered(ctx, member:discord.Member = None):
    if not member:
        member = ctx.author
    import requests
    try:
        name = ctx.author.name if not ctx.author.nick else ctx.author.nick
    except:
        name = ctx.author.name
    ava = ''
    for line in str(member.avatar_url).split('.')[:-1]:
        ava += line+'.'
    ava = ava+'png?size=1024'
    emb = discord.Embed(title='',
    description='',
    colour=discord.Colour.gold()
    )
    emb.set_footer(
        text=f'Специально для {name}', icon_url=ctx.author.avatar_url)

    'https://some-random-api.ml/canvas/triggered?avatar='+ava

    r = requests.get('https://some-random-api.ml/canvas/triggered?avatar='+ava, allow_redirects=True)
    open(f'triggered{ctx.author.id}.gif', 'wb').write(r.content)

    with open(f'triggered{ctx.author.id}.gif','rb') as f:
        file = discord.File(f)

    await ctx.send(embed=emb, file=file)

    from os import remove
    remove(f'triggered{ctx.author.id}.gif')

@bot.command(aliases=['waste'], description='Mission failed, we\'ll get \'em next time!', usage='[user(opt.)]')
async def wasted(ctx, member:discord.Member = None):
    if not member:
        member = ctx.author

    try:
        name = ctx.author.name if not ctx.author.nick else ctx.author.nick
    except:
        name = ctx.author.name
    ava = ''
    for line in str(member.avatar_url).split('.')[:-1]:
        ava += line+'.'
    ava = ava+'png?size=1024'
    emb = discord.Embed(title='',
    description='',
    colour=discord.Colour.gold()
    )
    emb.set_image(url='https://some-random-api.ml/canvas/wasted?avatar='+ava)
    emb.set_footer(
        text=f'Специально для {name}', icon_url=ctx.author.avatar_url)

    await ctx.send(embed=emb)

@bot.command(aliases=['patting'], description='**Pat me** OwO', usage='[user(opt.)]')
async def pat(ctx, member:discord.Member = None):
    import requests
    if not member:
        member = ctx.author

    rsp = requests.get('https://some-random-api.ml/animu/pat')
    emb = discord.Embed(title='',
    description=f'**{ctx.author.mention} pats {member.mention if member != ctx.author else "themselves"}**',
    colour=discord.Colour.gold()
    )
    emb.set_image(url=rsp.json()['link'])

    await ctx.send(embed=emb)

@bot.command(aliases=['winking'], description='Winks to someone ;)', usage='[user(opt.)]')
async def wink(ctx, member:discord.Member = None):
    import requests
    if not member:
        member = ctx.author

    rsp = requests.get('https://some-random-api.ml/animu/wink')
    emb = discord.Embed(title='',
    description=f'**{ctx.author.mention} winks to {member.mention if member != ctx.author else "themselves"}**',
    colour=discord.Colour.gold()
    )
    emb.set_image(url=rsp.json()['link'])

    await ctx.send(embed=emb)

@bot.command(aliases=['hugging'], description='Hugs someone :D', usage='[user(opt.)]')
async def hug(ctx, member:discord.Member = None):
    import requests
    if not member:
        member = ctx.author

    rsp = requests.get('https://some-random-api.ml/animu/hug')
    emb = discord.Embed(title='',
    description=f'**{ctx.author.mention} hugs {member.mention if member != ctx.author else "themselves"}**',
    colour=discord.Colour.gold()
    )
    emb.set_image(url=rsp.json()['link'])

    await ctx.send(embed=emb)

@bot.command(aliases=['wtf'], description='Show everyone your cringe', usage='Empty')
async def facepalm(ctx):
    import requests
    from random import choice

    sentence = choice([
        'is dead inside',
        'loses hope in humanity',
        'hits themselves with a chair',
        'is cringing'
    ])
    rsp = requests.get('https://some-random-api.ml/animu/face-palm')
    emb = discord.Embed(title='',
    description=f'**{ctx.author.mention} {sentence}**',
    colour=discord.Colour.gold()
    )
    emb.set_image(url=rsp.json()['link'])

    await ctx.send(embed=emb)

token = open('../emotebot.txt','r').read()
bot.run(token)
