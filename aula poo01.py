class Pessoa:
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        
    def apresentar(self):
        print("Ola meu nome é:",self.nome)
            
    def envelhecer(self,anos):
        self.idade += anos
         
                
                
    def mostrarcpf(self):
        print("este é meu cpf:",self.cpf)
                    
pessoa1 = Pessoa("mariana",20,'60234567095')
Pessoa2 = Pessoa('lauara',15,'60780536586')
    
pessoa1.apresentar()
Pessoa2.apresentar()
    