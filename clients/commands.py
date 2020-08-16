import click

from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass



@clients.command()
@click.option('-n','--name', type=str,prompt=True,help ='The client name: ')
@click.option('-c','--company', type=str,prompt=True,help ='The company name: ')
@click.option('-e','--email', type=str,prompt=True,help ='The email email: ')
@click.option('-p','--position', type=str,prompt=True,help ='The position name: ')
@click.pass_context    
def create(ctx, name, company,email,position):
    """Create a new client"""
    client =Client(name, company,email,position)
    client_service=ClientService(ctx.obj['file_clients'])

    client_service.create_client(client)

@clients.command()
@click.pass_context    
def list(ctx):
    """List all clients"""
    client_service=ClientService(ctx.obj['file_clients'])
    clients  = client_service.list_clients()
    _print_clients_flow(clients)

    


@clients.command()
@click.option('-i','--id', type=str,prompt=True, help ='The id client: ')
@click.pass_context    
def update(ctx, id):
    """Update a client""" 

    client_service=ClientService(ctx.obj['file_clients'])
    clients = client_service.list_clients()
    client = [client for client in clients if client['uid']==id]
    if client:
        client=_update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Client updated')
    else:
        click.echo('Client not found')




@clients.command()
@click.option('-i','--id', type=str,prompt=True)
@click.pass_context    
def delete(ctx, id):
    """Delete a client"""    
    client_service=ClientService(ctx.obj['file_clients'])
    clients = client_service.list_clients()
    client = [client for client in clients if client['uid']==id]
    if client:
        client_service.delete_client(Client(**client[0]))

        click.echo('Client deleted')
    else:
        click.echo('Client not found')



def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value')

    client.name     = click.prompt('New Name: ',type=str,default=client.name)
    client.company  = click.prompt('New company: ',type=str,default=client.company)
    client.email    = click.prompt('New email: ',type=str,default=client.email)
    client.position = click.prompt('New position: ',type=str,default=client.position)

    return client

def _print_clients_flow(clients): 
    if not clients:
        print('Empty list')
    else:
        headers = ''
        for key in clients[0].keys():
            headers+=f'| {key.upper()} '

        print(headers)


        for client in clients:
            values = ''
            for value in client.values():
                values+=f'| {value}'
            print(values)


all = clients
   