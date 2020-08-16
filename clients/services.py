import json
import uuid

from clients.models import Client

class ClientService:

    def __init__(self,file_clients):
        self.file_clients=file_clients
        self.load_clients()
#        print('Se cargaron los metodos')

    def load_clients(self)   :      
        file=open(self.file_clients,'r')
        var = json.load(file)
        clients = []
        for d in var:
            name = str(d.get("name"))
            company = str(d.get("company"))
            email = str(d.get("email"))
            position = str(d.get("position"))
            uid = str(d.get("uid"))
            client = Client(name, company, email,position,uid)
            clients.append(client)
        self.clients = list(clients)    
        file.close()

    def save_clients(self):   
        file=open(self.file_clients,'w')
        file.write(json.dumps([c.to_dict() for c in self.clients]))
        file.close()

    def create_client(self,client):
            
        if client not in self.clients:
            self.clients.append(client)
        else:
            print('Client already exists')  
        self.save_clients()      
     

    def list_clients(self):
        clients=[]
        for client in self.clients:
           if client is None: 
               pass 
           else:
                clients.append(client.to_dict())
        return clients        


    def delete_client(self, deleted_client):   
        clients_aux = []
        for client in self.clients:
            if client.uid==deleted_client.uid:
                pass
            else:
                clients_aux.append(client)
        self.clients = clients_aux        
        self.save_clients()  

    def update_client(self,updated_client):
        clients_aux = []
        for client in self.clients:
            if client.uid==updated_client.uid:
                clients_aux.append(updated_client)
            else:
                clients_aux.append(client)
        self.clients = clients_aux        
        self.save_clients()    

    def from_str(x) -> str:
        assert isinstance(x, str)
        return x
     

    
    