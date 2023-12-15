from discord.ext import commands
import discord
import os

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("$"),
    intents=discord.Intents.all()
)


@bot.event
async def on_ready():
    print("Bot is Ready!")

@bot.command()
async def echo(ctx: commands.Context, *, message: str):
    await ctx.send(message)
    await ctx.message.delete()

#Gives a summary of the series
@bot.command()
async def seriessum(ctx: commands.Context):
    await ctx.send('''
    Bill Chakor is a young, wisecracking lawyer with a talent for verbal insults and roasting public figures. He relocates to take a position at the Tensen Law Firm in the city of Roxford, working under his mentor Jason. 

    While Bill harbors insecurities and struggles with self-doubt, he is forced to publicly confront and mock various villains in Insult Court battles. These include arrogant politician Newt Manson, Bill’s shady casino-running Uncle Ricchi, and sinister shopkeeper Takahashi. 

    In his personal life, Bill befriends a temperamental ex-con named Zoey who gets him involved with her connections. This includes shy spiritualist Kora who runs a mountain temple. Through these relationships and courtroom showdowns, Bill must find conviction to overcome external and internal threats.

    The central themes seem to revolve around an underdog protagonist challenging hierarchies of power and corruption through verbal wit. There is also social commentary on status, prejudice, and moral obligation. Personal demons mirror societal ones as Bill pursues redemption and purpose.
        ''')

#Lists every character in the series
@bot.command()
async def listchars(ctx: commands.Context):    
    await ctx.send('''
        Here is a list of all 28 Characters Bill Chakor:
        Bill Chakor
        Zoey Pines
        Takahashi
        Newt Manson
        Ricchi Ippatsu
        LaShawnya Williams
        Mark Johnson
        Jorges Mason
        Kora Gray
        Parris DeMarco
        Clara Tess
        Kupp Martin
        Jarred Diego
        Lord Kay
        Panzen Dgoras
        Elder Grafton
        Kris Chakor
        Emile Castro
        Ray Castro
        Lucio Del Cara
        Gordon Von Barret
        Luko Goodkid
        Jax Carter
        Jason Thorne
        Steven Carmichael
        Roy G. Biv
        Chelsey DeMarco
    ''')

#Randomly roasts the user
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def roastme(ctx: commands.Context): 
    import random

    roasts = [
    ["You tired going to the clothing store to get *software*"],
    ["You worked at a seafood department and thought you were *selfish*"],
    ["You couldnt see anyone else and thought you were the only person on earth"],
    ["You went tightroping and thought you were *online*"],
    ["You bought a spider and thought you got a *Web Developer*"],
    ["You got on a high point of elevation on earth and thought you were *above everyone else*"],
    ["You thought *iHop* was an acrobatics gym"],
    ["You put an iPhone in some crust and thought you had *Apple Pie*"],
    ["You walked around with a clock and thought you were *Time Traveling*"],
    ["You walked around with some Brisk and thought you had *T-Mobile*"],
    ["You mixed Lipton and Brisk then thought you had *AT&T*"],
    ["You tried going on a space expedition to the *Samsung Galaxy*"],
    ["You thought Dunkin Donuts was NBA Chairity program"],
    ["You read some text on a screen and thought you were *IT Literate*"],
    ["You went to Italy during the winter to get *Italian Ice*"],
    ["You tried plugging a wire into a cloud and thought you were *Cloud Computing*"],
    ["You tried to go to Dr. Pepper for a diagnosis"],
    ["You thought high school was a place where you learned how to smoke weed"],
    ["You tried climbing over the moon and thought you were working *overnight*"],
    ["You yelled out loud and thought you had *Ice Cream*"],
    ["You tried pushing a tree and thought you were *woodworking*"],
    ["You thought Taco Bell was a Mexican phone company"],
    ["You decapitated yourself to *get ahead*"],
    ["You made a container out of junk and thought you had a *trash can*"],
    ["You went to Lowe's to get high"],
    ["You went to Home Depot to buy a house"],
    ["You fried some icing and thought you had *Krispy Kreme*"],
    ["You looked in a mirror and thought you *self-reflected*"],
    ["You thought you were gonna get a speeding ticket for running on foot"],
    ["You thought Tim Cook was a famous chef"],
    ["You thought terminal cancer was a computer virus"],
    ["You thought Target was an archery range"],
    ["You thought you had to write a book in order to get *authorized access* to something"],
    ["You thought the millennium falcon was an actual bird"],
    ["You thought Pizza Hut was literally a house made of bread, cheese, and sauce"],
    ["You thought you had to write a book in order to get *authorized access* to something"],
    ["You thought Walmart was a shelf with a bunch of items for sale on it"],
    ["You tried planting a dollar tree"],
]

    random_index = random.randint(0, len(roasts)-1) 

    random_roast = roasts[random_index][0]

    await ctx.send("You're so stupid, " + random_roast)

bot.run(os.getenv("TOKEN"))