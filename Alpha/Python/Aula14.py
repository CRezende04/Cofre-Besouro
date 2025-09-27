from datetime import date

class Cliente:
    def __init__(self, id_cliente, nome, telefone, email):
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Cliente {self.id_cliente}: {self.nome}, {self.telefone}, {self.email}"


class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.disponivel = True


    def __str__(self):
        status = "Disponível" if self.disponivel else "Ocupado"
        return f"Quarto {self.numero} ({self.tipo}) - R${self.preco}/dia - {status}"


class Reserva:
    def __init__(self, cliente, quarto, check_in, check_out):
        self.cliente = cliente
        self.quarto = quarto
        self.check_in = check_in
        self.check_out = check_out
        self.ativa = True

        
    def __str__(self):
        status = "Ativa" if self.ativa else "Cancelada"
        return (f"Reserva de {self.cliente.nome} no quarto {self.quarto.numero}, "
                f"de {self.check_in} até {self.check_out} - {status}")


class GerenciadorDeReservas:
    def __init__(self):
        self.reservas = []
        self.quartos = []
        self.clientes = []


    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)


    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)


    def verificar_disponibilidade(self):
        disponiveis = [q for q in self.quartos if q.disponivel]
        if not disponiveis:
            print("Nenhum quarto disponível.")
        else:
            print("Quartos disponíveis:")
            for q in disponiveis:
                print(q)


    def criar_reserva(self, cliente, numero_quarto, check_in, check_out):
        # encontrar o quarto
        for quarto in self.quartos:
            if quarto.numero == numero_quarto and quarto.disponivel:
                reserva = Reserva(cliente, quarto, check_in, check_out)
                self.reservas.append(reserva)
                quarto.disponivel = False
                print("Reserva criada com sucesso!")
                return reserva
        print("Quarto indisponível ou não encontrado.")


    def cancelar_reserva(self, reserva):
        if reserva in self.reservas:
            reserva.ativa = False
            reserva.quarto.disponivel = True
            print("Reserva cancelada com sucesso!")
        else:
            print("Reserva não encontrada.")

        
    def listar_reservas(self):
        if not self.reservas:
            print("Nenhuma reserva encontrada.")
        else:
            for r in self.reservas:
                print(r)

    
    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for c in self.clientes:
                print(c)



if __name__ == "__main__":
    gerenciador = GerenciadorDeReservas()

    # Criando clientes
    cliente1 = Cliente(1, "Alice", "1111-1111", "alice@email.com")
    cliente2 = Cliente(2, "Bob", "2222-2222", "bob@email.com")

    gerenciador.adicionar_cliente(cliente1)
    gerenciador.adicionar_cliente(cliente2)

    # Criando quartos
    q1 = Quarto(101, "Single", 150)
    q2 = Quarto(102, "Double", 200)
    gerenciador.adicionar_quarto(q1)
    gerenciador.adicionar_quarto(q2)

    # Testando funcionalidades
    gerenciador.verificar_disponibilidade()
    reserva1 = gerenciador.criar_reserva(cliente1, 101, date(2025, 9, 26), date(2025, 9, 30))
    gerenciador.verificar_disponibilidade()
    gerenciador.listar_reservas()
    gerenciador.cancelar_reserva(reserva1)
    gerenciador.verificar_disponibilidade()
