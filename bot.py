import discord 
import requests
from countryinfo import CountryInfo as ci
from datetime import datetime
import numpy as np
import praw
from discord.ext import commands
NUM_VIDS_TO_FIND = 100
PAGE_SEED = 2#int(np.random.uniform(2,5))

# ! is taken from the Rythm bot. Use "." instead
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("bot_botesen is live!")


# ---------- Geografi ---------- #
@client.command(pass_context = True)
async def size(ctx,*countries):
    try:
        if len(countries) == 0:
            e = "Øy, du må ha minst 1 land! Med mindre du er ute etter kukstørrelsen til Ole, kan røpe at den er 50cm+ :O"
            await ctx.send(e)
        elif len(countries) == 1:
            if countries[0] == "ole" or  countries[0] == "Ole":
                await ctx.send("Oles schlong er ganske huge, bicepsen derimot... ")                
            else:
                try:
                    c_obj = ci(countries[0])
                    a = c_obj.area()
                    send = str(countries[0]) + " er " + str(a) + " kvadratkilometer."
                    await ctx.send(send)
                except Exception as e:
                    send = "Dette er kleint, men jeg tviler på at " + str(countries[0])+ " er et land"
                    await ctx.send(send)                   
        else:
            data = {}
            areas = []
            for country in countries:
                try:
                    c_obj = ci(country)
                    a = c_obj.area()
                    areas.append(a)
                    data[country] = a
                except Exception as e:
                    send = "Dette er kleint, men jeg tviler på at " + str(country)+ " er et land"
                    await ctx.send(send)   
            areas.sort()
            pos = 1
            for a in reversed(areas):
                for co, ar in data.items():
                    if ar == a:
                        send = str(pos) + ": " + str(co) + " (" + str(a) +" m^2)"
                        await ctx.send(send)
                        break
                pos += 1
         
            
                
    except Exception as e:
        await ctx.send("Dette er ganske kleint ja... ")
        await ctx.send(e)

# ---------- Officepug ---------- #
@client.command(pass_context = True)
async def office(ctx):
    now = datetime.now()
    
    now_str = str(now)
    now_date = now_str.split(" ")[0]
    now_yr = now_date.split("-")[0]
    now_mnt = now_date.split("-")[1]
    now_day = now_date.split("-")[2]

    now_clock = now_str.split(" ")[1]
    
    if int(now_clock[0]) != 0:
        now_day = int(now_day) + 1
    if int(now_clock[0]) == 0 and int(now_clock[1]) > 4:
        now_day = int(now_day) + 1   
    
    office = datetime(int(now_yr),int(now_mnt),int(now_day),4,30)
    diff = office - now
    send = "Office pøggen begynner om " + print_time(diff) + ". Hold ut!"
    await ctx.send(send)

# ---------- Philippe ---------- #
@client.command(pass_contexct = True)
async def philippe(ctx):
    await ctx.send("er den eeeeekleste homsen!")

@client.command(pass_contexct = True)
async def Philippe(ctx):
    await ctx.send("er den eeeeekleste homsen!")

@client.command(pass_context = True)
async def hjelp(ctx):
    try:
        send = "Velkommen til bot_botesen, din nye bestevenn. Jeg støtter følgende kommandoer: \n \nBruk .runk for en random juicy video fra pornhub." + \
            "\nBruk .pornostjerne for en random juicy babe fra pornhubs topplister! \n" + "Bruk .office for å finne ut hvor lenge det er til office pøggen! \n" + \
            "Bruk .size for å finne og sammenlikne størrelsen til verdens land! \nBruk .meme for en random spicyyy megmeg! \nDessuten finnes det mange juicy easter eggs ;)"

        await ctx.send(send)
    except Exception as e:
        await ctx.send("Sry, ingen hjelp å få her! LMAO")

@client.command(pass_context = True)
async def utovernavle(ctx):
    try:
        await ctx.send("https://www.facebook.com/markus.ivarsen.1")
    except Exception as e:
        await ctx.send("Æææææsjsjj")

@client.command(pass_context = True)
async def ole(ctx):
    try:
        await ctx.send("https://www.tiktok.com/@aslak.smith/video/6824851962882821382?_d=secCgsIARCbDRgBIAMoARI%2BCjzv57sjM5loJDA2MWv3ccYiQVSvv5%2FZ8QkBdGB%2F54s3Bj1DBmO6lA%2BEGSx7uAbffvVpuWb6wFoneSyfFXgaAA%3D%3D&language=en&preview_pb=0&sec_user_id=MS4wLjABAAAAAPxKU_d1g1ds9i3qpJyKRxQdBdNVmdOV_HMdLEtPpLTMnax-1Xr2z0N5A6qyry2M&share_item_id=6824851962882821382&share_link_id=ABDD89CD-8905-4D1B-8692-BD394589D633&timestamp=1599469091&tt_from=messenger&u_code=dblgafh26h3jfi&user_id=6814224647434830853&utm_campaign=client_share&utm_medium=ios&utm_source=messenger&source=h5_m")
    except Exception as e:
        await ctx.send("Leter du etter et omvendt kinderegg?")

@client.command(pass_context = True)
async def pubg(ctx):
    await ctx.send("https://www.fretex.no/")
@client.command(pass_context = True)
async def nextgentel(ctx):
    await ctx.send("https://en.wikipedia.org/wiki/Shit")
@client.command(pass_context = True)
async def csgo(ctx):
    await ctx.send("Det var headshot på min skjerm!!!")
@client.command(pass_context = True)
async def pcen_til_ole(ctx):
    await ctx.send("Denne memen er desverre død. Jeg gråter jeg også :(")
@client.command(pass_context = True)
async def pcentilole(ctx):
    await ctx.send("Denne memen er desverre død. Jeg gråter jeg også :(")
@client.command(pass_context = True)
async def fretex(ctx):
    await ctx.send("https://www.pubg.com/en-us/")

@client.command(pass_context = True)
async def markus(ctx):
    await ctx.send("https://images-ext-2.discordapp.net/external/jBMWiZnZnKfKZFrsMidxSK5OZD2eKkWeO_G1KItllEM/https/i.redd.it/lf3k1avcq3m51.gif?width=526&height=677")

# ----------- meme --------# 
@client.command(pass_context = True)
async def meme(ctx,subreddit=""):
    reddit = praw.Reddit(client_id='sy4Rm_fIuZNJVw',
                     client_secret='tQ4CGmQdYouxurloxCTD03mfCFQ',
                     user_agent='bot_botesen_devscript')

    if subreddit == "":
        subname = "dankmemes"
    else:
        subname = subreddit
    memes_submissions = reddit.subreddit(subname).hot()
    post_to_pick = int(np.random.uniform(1,100))
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

def validate_arguments(*args):
    if len(args) == 0:
        print("jobber")
        e = "Øy, du må ha minst 1 land! Med mindre du er ute etter kukstørrelsen til Ole, kan røpe at den er 50cm+ :O"
        return False, e
     
def is_country(country):
    pass

def print_time(t):
    h = str(t).split(":")[0]
    m = str(t).split(":")[1]
    s = str(t).split(":")[2]
    return h + " timer, " + m + " minutter og " + s + " sekunder"


client.run("NzUxOTc1MTMyMjM0NTE0NDgy.X1Q5ag.jJKxrZwdPnAtOJapKjWZXbEIZUw")