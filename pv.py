
import json
import click
from clients import commands as client_commands

clients = '.data.json'

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['file_clients']=clients

cli.add_command(client_commands.all)
    

