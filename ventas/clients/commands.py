import click





@click.group() #convierte a la función client en otro decorador
def clients():
    """
    maganes the clients lifecycles
    """
    pass



@click.command()
@click.pass_context
def create (ctx, name, company, email, position):
    """
    create a new client
    """
    pass


@click.command()
@click.pass_context
def listc(ctx):
    """
    listo all clients
    """
    pass


@click.command()
@click.pass_context
def update(ctx,client_uid):
    """
    update a client
    """
    pass

@click.command()
@click.pass_context
def delete(ctx, client_uid):
    """
    delete a client
    """
    pass

allc = clients

