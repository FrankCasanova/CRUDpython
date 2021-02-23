
clients = 'pablo,ricardo, '

def create_client(client_name):
    global clients 

    if client_name not in clients:

        clients += client_name
        _add_comma() 
    else:
        print('Client already is in the client\'s list')    

def list_client():
    global clients
    print(clients)

def update_client(client_name,update_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name+',', update_client_name + ',')
    else:
        print('Client is not in client\'s list')    

def delete_client():
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client is not in the client\'s list.')    

def search_client(client_name):
    global clients
    clients_list = clients.split(',')

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True


def _add_comma():
    global clients
    clients += ','

def _print_welcome():
    print('WELCOME TO FRANKY SELLS')
    print('*'*50)
    print ('What would you like today?.')
    print('[C]reate client')    
    print('[U]pdate client')    
    print('[D]elete client') 
    print('[S]earch client') 

def _get_client_name():
    return input('What is the client name? ')


if __name__ == '__main__':

    _print_welcome()
    
    command = input()
    command = command.upper()

    if command == 'C':
        _get_client_name()
        create_client(_get_client_name)
        list_client()

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

    else:
        print('Invalid command')

    list_client()        
    
    