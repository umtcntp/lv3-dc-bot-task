import discord
from discord.ext import commands
from bot_token import token
from database import create_table, add_task_to_db, list_tasks, delete_task_from_db, mark_task_complete

create_table()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents = intents)


@bot.event
async def on_ready():
    print(f'Login as {bot.user} ')

@bot.command()
async def add_task(ctx, *,description):
    add_task_to_db(description)
    await ctx.send(f'The task with a description of "{description}" has been added to the database.')

@bot.command()
async def delete_task(ctx, task_id:int):
    result = delete_task_from_db(task_id)
    if result:
        await ctx.send(f'The task with ID {task_id} has been deleted successfully.')
    else:
        await ctx.send(f'No task found with ID {task_id}.')

@bot.command()
async def show_tasks(ctx):
    tasks = list_tasks()
    if not tasks:
        await ctx.send("No tasks found.")
    else:
        task_list = "\n".join([f"ID: {task[0]} | Task: {task[1]} | Complete: {task[2]}" for task in tasks])
        await ctx.send(f"Tasks:\n{task_list}")

@bot.command()
async def complete_task(ctx, task_id:int):
    result = mark_task_complete(task_id)
    if result:
        await ctx.send(f'The task with ID {task_id} has been marked as complete.')
    else:
        await ctx.send(f'No task found with ID {task_id} to mark as complete.')


bot.run(token)