# Desafio
# Agora, vamos Adicionar uma funcionalidade à classe UsuarioTelefone para que possa ser verificado
# o saldo disponível em seu plano. Para essa solução, você pode criar uma classe PlanoTelefone, o seu
# método de inicialização e encapsular os atributos, 'nome' e 'saldo' dentro da classe. Adicione também
# um método 'verificar_saldo' para verificar o saldo do plano e uma  'mensagem_personalizada' para
# gerar uma mensagem personalizada.

# Condições da verificação do saldo:
# - Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
# - Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
# - Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

# Entrada
# Como entrada, será solicitado o nome, plano (Essencial, Prata, Premium) e saldo atual do cliente.

# Saída
# Mensagem personalizada de acordo o saldo do cliente.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas.
# Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	                              Saída

# João                                    Seu saldo está baixo. Recarregue e use os serviços do seu plano.
# Essencial      
# 9


# Debora                                  Seu saldo está razoável. Aproveite o uso moderado do seu plano.
# Prata
# 11


# Catarina                                Parabéns! Continue aproveitando seu plano sem preocupações.
# Premium
# 50




# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':


# TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:    
    
# TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo: 
    

# Classe UsuarioTelefone:
class UsuarioTelefone:
    def __init__(self, nome_usuario, plano_usuario):
        self.nome_usuario = nome_usuario
        self.plano_usuario = plano_usuario

     
    def verificar_saldo(self):
        saldo_usuario = usuario.plano_usuario.saldo
        if saldo_usuario < 10:
            return saldo_usuario, "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif saldo_usuario >= 50:
            return saldo_usuario, "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return saldo_usuario, "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
        

# TODO: Crie um método para verificar o saldo do usuário e gerar uma mensagem personalizada:
class PlanoTelefone:
    def __init__(self, nome_plano, saldo_inicial):
         self.nome_plano = nome_plano
         self._saldo_inicial = saldo_inicial
    
    @property
    def saldo(self):
        return self._saldo_inicial
    



# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

 # Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)