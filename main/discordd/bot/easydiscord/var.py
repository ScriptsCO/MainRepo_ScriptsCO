
"""
varibles 
"""

import discord 
from discord import * 
# this is to stop import loop :/

bot = discord.Client(intents=discord.Intents.all())
"""
the main bot varible 
"""
tree = app_commands.CommandTree(bot)
"""
the command tree 
"""


customcolor = discord.Color
"""
Pick a color using from_rgb or somthing else!
"""

