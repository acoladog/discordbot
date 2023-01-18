import discord
from discord.ext import commands
import re
from keep_alive import keep_alive

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print('目前登入身份：', bot.user)
    #channel = bot.get_channel(1000976647941533756)
    #await channel.send('我上線了')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1018082828967215115)
    await channel.send(f'歡迎 {member} 加入 dc 704 班')
    #guild = bot.get_guild(member)
            #role = guild.get_role(1015799270525378581)
          #  await member.member.add_roles(role)

@bot.event
async def on_member_leave(member):
    channel = bot.get_channel(1018082860617433129)
    await channel.send(f'喔不！{member} 離開我們了')

@bot.event
async def on_message(message):
    a = [
        'hi',
        'Hi',
        'HI',
        '嗨',
        '安安',
        '安',
        '你好',
        '呵',
        '哈',
        'ㄏㄏ',
        'hhh',
        '幹',
        '靠',
        '白癡',
        '變態',
        'ㄎㄅ',
        '單身狗',
        '同性戀',
        '智障',
        'gay',
        'ga',
        '腦殘',
        '神經',
        '神經病',
        '吃屎',
        '三小',
        '尛',
        '去死',
        'ㄍ',
        'ㄎ',
        'ㄘ',
        '操',
        '你娘',
        '靠邀',
        '靠腰',
        '靠要',
        '哈囉'
        ]
    b = [
        'hello',
        'Hello',
        'HELLO',
        '安安',
        '嗨嗨嗨',
        '安安',
        '嗨~~',
        '哈哈哈哈哈',
        'ㄏㄏ',
        '呵呵',
        '哈哈哈',
        '你要幹甚麼',
        '不要靠著我',
        '跟你聊天我才變白癡的',
        '至少我不像你變性',
        '看吧!這個沒水準的人',
        '我不像你腳踏多條船',
        '跟你學的',
        '我不像你腦殘 + 有問題',
        '跟你學的',
        '跟你學的',
        '我不像你沒腦',
        '我的神經怎了',
        '我至少有要醫',
        '那不是你在吃的東西嗎',
        '對對 無三不成禮',
        '尛 音:ㄇㄚˊ 意思:宗教、神話中指害人性命、迷惑人的惡鬼',
        '那我詛咒你 上廁所掉進馬桶',
        '你是要割甚麼',
        '你是啃什麼',
        'ㄘ什麼ㄘ 神經病阿',
        '你是要去操場阿',
        'FBI 就是他',
        '你腰酸背痛阿',
        '你腰酸背痛阿',
        '你腰酸背痛阿',
        '嗨'
        ]
    if message.author == bot.user:
        return
    c = 0
    d = 0
    for i in range(len(a)):
        y = re.compile(f".*{a[i]}.*")
        t = message.content
        r = y.findall(t)
        if r:
            c += 1
            d = i
    if c == 1:
        await message.channel.send(b[d])

    a = message.author.name
    b = message.content
    print(f'{a} : {b}')
    f = open('say.txt', 'a')
    seq = [a," : ",b]
    f.writelines(seq)
    
keep_alive()
