import uuid



class Client:
    def __init__(self,name,company,email,position,uid=None) -> None:
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4() #esto nos garantiza que los ID son únicos.

    def to_dict(self):
        return vars(self)    #nos permite acceder a la representación de nuestro objeto en forma de diccionario

    @staticmethod #metodo estatico, es un metodo que se puede ejecutar sin necesidad de una instancia de clase.
    def schema():
        return['name','company', 'email','position', 'uid']



