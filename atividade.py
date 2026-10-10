# Classe que representa um Empréstimo individual
class Emprestimo:
    def __init__(self, valor: float, pago: bool = False):
        self.valor = valor
        self.pago = pago

    def quitar(self):
        self.pago = True


# Classe que representa um Cliente do banco
class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.emprestimos = []  # Relacionamento 1 para N (Lista de Empréstimos)

    def adicionar_emprestimo(self, emprestimo: Emprestimo):
        self.emprestimos.append(emprestimo)

    def obter_emprestimos_pendentes(self):
        return [e for e in self.emprestimos if not e.pago]

    def calcular_divida_total_pendente(self) -> float:
        return sum(e.valor for e in self.obter_emprestimos_pendentes())

    def apto_para_novo_emprestimo(self) -> bool:
        pendentes = self.obter_emprestimos_pendentes()
        divida_total = self.calcular_divida_total_pendente()

        # Regra de negócio:
        # Não pode ter 2 ou mais empréstimos pendentes E
        # A dívida total não pode ultrapassar R$ 10.000,00
        if len(pendentes) >= 2 or divida_total > 10000.00:
            return False
        return True

    def exibir_relatorio(self):
        pendentes = self.obter_emprestimos_pendentes()
        divida = self.calcular_divida_total_pendente()
        apto = self.apto_para_novo_emprestimo()

        print("=" * 50)
        print(f"Cliente: {self.nome} (CPF: {self.cpf})")
        print(f"Total de empréstimos registrados: {len(self.emprestimos)}")
        print(f"Empréstimos pendentes de quitação: {len(pendentes)}")
        print(f"Dívida total pendente: R$ {divida:.2f}")
        print(f"Status para novo empréstimo: {'✅ APTO' if apto else '❌ NÃO APTO'}")
        if not apto:
            motivos = []
            if len(pendentes) >= 2:
                motivos.append("Possui 2 ou mais empréstimos pendentes")
            if divida > 10000.00:
                motivos.append("Dívida total pendente ultrapassa R$ 10.000,00")
            print(f"Motivo(s): {', '.join(motivos)}")
        print("=" * 50)


# Exemplo de teste da aplicação
if __name__ == "__main__":
    # Criando clientes
    cliente1 = Cliente("João Silva", "111.222.333-44")
    cliente2 = Cliente("Maria Santos", "555.666.777-88")
    cliente3 = Cliente("Carlos Souza", "999.888.777-66")

    # Cliente 1: 1 empréstimo pendente de R$ 3.000,00 -> APTO
    cliente1.adicionar_emprestimo(Emprestimo(3000.00, pago=False))

    # Cliente 2: 2 empréstimos pendentes de R$ 2.000,00 -> NÃO APTO (Limite de pendências atingido)
    cliente2.adicionar_emprestimo(Emprestimo(2000.00, pago=False))
    cliente2.adicionar_emprestimo(Emprestimo(1500.00, pago=False))

    # Cliente 3: 1 empréstimo alto de R$ 12.000,00 -> NÃO APTO (Ultrapassou R$ 10.000,00)
    cliente3.adicionar_emprestimo(Emprestimo(12000.00, pago=False))

    # Exibindo os relatórios
    clientes = [cliente1, cliente2, cliente3]
    print("\n--- RELATÓRIO DE AVALIAÇÃO DE EMPRÉSTIMOS ---\n")
    for c in clientes:
        c.exibir_relatorio()
