import json
import discord
print(discord.__file__)
from enum import Enum

class State(Enum):
    START = 1


class Traits(Enum):
    Agency = 1
    Detective = 2


class Skills:
    def __init__(self, willpower, intellect, combat, agility):
        self.willpower = willpower
        self.intellect = intellect
        self.combat = combat
        self.agility = agility


class Investigator:
    def __init__(self, name, skills, health, sanity, traits):
        self.name = name
        self.skills = skills
        self.health = health
        self.sanity = sanity
        self.traits = traits

    def print(self):
        return f"调查员 - 姓名: {self.name} - {'.'.join(self.traits)}"

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = State.START




intents = discord.Intents.default()
bot = discord.Bot(command_prefix='/', intents=intents)

with open('config.json', 'r', encoding="utf-8") as cfg:
    data = json.load(cfg)

TOKEN = data['token']

@bot.event
async def on_ready():
    print("Bot ready!")

@bot.slash_command
async def hello(ctx):
    await ctx.respond("Hey!")

bot.run(TOKEN)