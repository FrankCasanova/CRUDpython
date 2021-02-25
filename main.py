import csv
import os


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']



clients = []






def _initialize_clientes_from_storage():
    
    with open(CLIENT_TABLE, mode='r') as f:

        reader = csv.DictReader(f,fieldnames=CLIENT_SCHEMA)

        [clients.append(row) for row in reader]


def _save_clients_to_storage():

    tmp_table_name = f'{CLIENT_TABLE}.tmp'
    
    with open(tmp_table_name, mode='w') as f:

        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)
        

def create_client(client):
    global clients 

    if client not in clients:
        clients.append(client)
        
    else:
        print('Client already is in the client\'s list')    

def list_client():
    global clients
    
    [print(f'{idx} | {client["name"]} | {client["company"]} | {client["email"]} | {client["position"]}') for idx,client in enumerate(clients)]

def update_client(client_name,update_client_name):
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = update_client_name
    else:
        print('Client is not in client\'s list')    

def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break 

def search_client(client_name):
    global clients
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('WELCOME TO FRANKY SELLS')
    print('*'*50)
    print ('What would you like today?.')
    print('[C]reate client')    
    print('[U]pdate client')    
    print('[D]elete client') 
    print('[S]earch client')
    print('[L]ist client')


def _get_client_field(field_name):
    field = None
    while not field:
        field= input(f'What is the client {field_name}')

    return field    

def _get_client_name():
    return input('What is the client name? ')


if __name__ == '__main__':

    _initialize_clientes_from_storage()
    _print_welcome()
    
    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('enamil'),
            'position': _get_client_field('position'),
            }
        create_client(client)

    elif command == 'D':
        client_name = _get_client_name()
        delete_client()

    elif command == 'U':
        client_name =_get_client_name()
        update_client_name = input('What is the updated client name? ')
        update_client(client_name=client_name, update_client_name=update_client_name)

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print(f'the client: {client_name} is not in our client\'s list')    
    elif command == 'L':
        list_client()
    else:
        print('Invalid command')
     
    
    _save_clients_to_storage()