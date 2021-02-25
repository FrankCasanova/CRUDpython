import click
from clients import commands as clients_commands


@click.group() #este es el punto de entrada
@click.pass_context #objeto de contexto
def cli():
    ctx.obj = {}


cli.add_command(clients_commands.allc)    