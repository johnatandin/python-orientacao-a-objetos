# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    # Método para fazer uma chamada telefônica
    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)
        if self.plano.verificar_saldo() >= custo:
            self.plano.deduzir_saldo(custo)
            return f"Chamada para {destinatario} realizada com sucesso. Saldo restante: ${self.plano.verificar_saldo():.2f}"
        else:
            return "Saldo insuficiente para realizar a chamada."

# Classe Plano, ela representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    # Método para verificar o saldo atual
    def verificar_saldo(self):
        return self.saldo

    # Método para calcular o custo de uma chamada supondo o custo de $0.10 por minuto
    def custo_chamada(self, duracao):
        return duracao * 0.10

    # Método para deduzir o valor do saldo do plano
    def deduzir_saldo(self, valor):
        self.saldo -= valor

# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

# Recebendo as informações do usuário:
nome = input("Nome do usuário: ")
numero = input("Número do telefone: ")
saldo_inicial = float(input("Saldo inicial: "))

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input("Destinatário da chamada: ")
duracao = int(input("Duração da chamada (minutos): "))

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
