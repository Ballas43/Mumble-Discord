import discord
import pymumble_py3 as pymumble


from discord.ext.commands import Bot

bot = Bot("!")

token = 'ODUzMjY1MjUyNzMyNTAyMDI2.YMS3MQ.jrEEz0wiQJMbUJq5AHi2oNe52QA'

mumble = pymumble.Mumble("192.168.100.40", "Superuser", port=64738, password="kutakkutimsampebodo.-")

userID = 0
msgID = 0

cameraCHID = 1
cgCHID = 4

@bot.event
async def on_ready():
    print('Bot Ready')
    channel = bot.get_channel(853323633308336208)
    await channel.purge(limit=5)

    embed = discord.Embed(title="Mumble Channel Selection (Current: None)", description="React to choose server that mumble will connect to: ", color=discord.Color.blue())

    embed.add_field(name="Camera 📷", value="Speak to cameraman", inline=False)
    embed.add_field(name="Live CG 🖥️", value="Speak to Visual Graphics Operator", inline=False)

    msg = await channel.send(embed=embed)
    await msg.add_reaction("📷")
    await msg.add_reaction("🖥️")

    global msgID
    msgID = msg.id

    find_user('Discord')

@bot.event
async def camera_ch():
    channel = bot.get_channel(853323633308336208)
    await channel.purge(limit=5)

    embed = discord.Embed(title="Mumble Channel Selection (Current: Camera)", description="React to choose server that mumble will connect to: ", color=discord.Color.blue())

    embed.add_field(name="Camera 📷", value="Speak to Cameraman", inline=False)
    embed.add_field(name="Live CG 🖥️", value="Speak to Visual Graphics Operator", inline=False)

    msg = await channel.send(embed=embed)
    await msg.add_reaction("📷")
    await msg.add_reaction("🖥️")

    global msgID
    msgID = msg.id

@bot.event
async def cg_ch():
    channel = bot.get_channel(853323633308336208)
    await channel.purge(limit=5)

    embed = discord.Embed(title="Mumble Channel Selection (Current: Live CG)", description="React to choose server that mumble will connect to: ", color=discord.Color.blue())

    embed.add_field(name="Camera 📷", value="Speak to cameraman", inline=False)
    embed.add_field(name="Live CG 🖥️", value="Speak to Visual Graphics Operator", inline=False)

    msg = await channel.send(embed=embed)
    await msg.add_reaction("📷")
    await msg.add_reaction("🖥️")

    global msgID
    msgID = msg.id


@bot.event
async def on_raw_reaction_add(payload):
    if msgID == payload.message_id and payload.user_id != 853265252732502026:
        emoji = payload.emoji.name

        channel = bot.get_channel(payload.channel_id)
        message = message = await channel.fetch_message(msgID)
        user = await bot.fetch_user(payload.user_id)   

        if emoji == "📷":
            print("Camera")
            mumble.channels[cameraCHID].move_in(session=userID)
            await camera_ch()
        elif emoji == "🖥️":
            print("Live CG")
            mumble.channels[cgCHID].move_in(session=userID)
            await cg_ch()
        
        

def find_user(name):
    dicts = mumble.channels.find_by_name("Shalom AVL Ministry").get_users()
    res = next(item for item in dicts if item["name"] == name)
    
    global userID
    userID = res['session']

mumble.start()

bot.run(token)