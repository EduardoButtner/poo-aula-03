import csv
import os

# Classe Pessoa com o novo atributo 'telefone'
class Pessoa:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

    def to_list(self):
        return [self.nome, self.idade, self.email, self.telefone]

# Classe CRUD
class CadastroPessoas:
    ARQUIVO = "pessoas.csv"

    def __init__(self):
        # Se não existir o arquivo, cria com o cabeçalho atualizado
        if not os.path.exists(self.ARQUIVO):
            with open(self.ARQUIVO, mode="w", newline="", encoding="utf-8") as f:
                escritor = csv.writer(f)
                escritor.writerow(["Nome", "Idade", "Email", "Telefone"])

    def adicionar(self, pessoa: Pessoa):
        with open(self.ARQUIVO, mode="a", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(pessoa.to_list())
        print("✅ Pessoa cadastrada com sucesso!")

    def listar(self):
        with open(self.ARQUIVO, mode="r", encoding="utf-8") as f:
            leitor = csv.reader(f)
            for i, linha in enumerate(leitor):
                if i == 0:
                    continue  # pula cabeçalho
                if linha:
                    print(f"Nome: {linha[0]} | Idade: {linha[1]} | Email: {linha[2]} | Telefone: {linha[3]}")

    def atualizar(self, email, novo_nome, nova_idade, novo_telefone):
        linhas = []
        atualizado = False
        with open(self.ARQUIVO, mode="r", encoding="utf-8") as f:
            leitor = csv.reader(f)
            for linha in leitor:
                if linha and linha[2] == email:
                    linha[0] = novo_nome
                    linha[1] = nova_idade
                    linha[3] = novo_telefone
                    atualizado = True
                linhas.append(linha)
        
        with open(self.ARQUIVO, mode="w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerows(linhas)
            
        if atualizado:
            print("✅ Cadastro atualizado com sucesso!")
        else:
            print("⚠️ Pessoa não encontrada.")

    def excluir(self, email):
        # Verifica primeiro se o registro existe
        encontrado = False
        linhas = []
        
        with open(self.ARQUIVO, mode="r", encoding="utf-8") as f:
            leitor = csv.reader(f)
            for linha in leitor:
                if linha and linha[2] == email:
                    encontrado = True
                linhas.append(linha)

        if not encontrado:
            print("⚠️ Pessoa não encontrada.")
            return

        # Solicitando confirmação do usuário (Requisito 1b)
        confirmacao = input(f"Tem certeza que deseja excluir a pessoa com email '{email}'? (s/n): ").strip().lower()
        if confirmacao != 's':
            print("❌ Operação de exclusão cancelada.")
            return

        # Filtrando e salvando apenas as linhas mantidas
        novas_linhas = [linha for linha in linhas if not (linha and linha[2] == email)]
        
        with open(self.ARQUIVO, mode="w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerows(novas_linhas)

        print("🗑️ Pessoa excluída com sucesso!")


def menu():
    cadastro = CadastroPessoas()

    while True:
        print("\n--- MENU ---")
        print("1 - Cadastrar Pessoa")
        print("2 - Listar Pessoas")
        print("3 - Atualizar Pessoa")
        print("4 - Excluir Pessoa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            idade = input("Idade: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            pessoa = Pessoa(nome, idade, email, telefone)
            cadastro.adicionar(pessoa)

        elif opcao == "2":
            cadastro.listar()

        elif opcao == "3":
            email = input("Digite o email da pessoa que deseja atualizar: ")
            novo_nome = input("Novo nome: ")
            nova_idade = input("Nova idade: ")
            novo_telefone = input("Novo telefone: ")
            cadastro.atualizar(email, novo_nome, nova_idade, novo_telefone)

        elif opcao == "4":
            email = input("Digite o email da pessoa que deseja excluir: ")
            cadastro.excluir(email)

        elif opcao == "5":
            print("👋 Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
