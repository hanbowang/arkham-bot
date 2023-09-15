import discord

with open('config.json', 'r') as cfg:
  data = json.load(cfg)
  print(data)