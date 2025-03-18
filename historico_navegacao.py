class HistoricoNavegacao:
    def __init__(self):
        # Pilha para armazenar o histórico de navegação
        self.historico = []
        # Variável para armazenar a página atual
        self.pagina_atual = None

    def visitar_pagina(self, pagina):
        """
        Adiciona uma nova página ao topo do histórico.
        """
        if self.pagina_atual:
            # Se houver uma página atual, empilha no histórico
            self.historico.append(self.pagina_atual)
        self.pagina_atual = pagina
        print(f"Visitando: {pagina}")

    def voltar(self):
        """
        Volta para a página anterior, removendo a página atual do histórico.
        """
        if not self.historico:
            print("Não há páginas anteriores no histórico.")
            return

        # Desempilha a última página visitada
        pagina_anterior = self.historico.pop()
        print(f"Voltando para: {pagina_anterior}")
        self.pagina_atual = pagina_anterior

    def exibir_pagina_atual(self):
        """
        Exibe a página que está sendo visualizada no momento.
        """
        if self.pagina_atual:
            print(f"Página atual: {self.pagina_atual}")
        else:
            print("Nenhuma página está sendo visualizada no momento.")

    def exibir_historico_completo(self):
        """
        Exibe todas as páginas visitadas até o momento.
        """
        if not self.historico:
            print("O histórico está vazio.")
            return

        print("Histórico completo de navegação:")
        for i, pagina in enumerate(self.historico, start=1):
            print(f"{i}. {pagina}")
        if self.pagina_atual:
            print(f"Página atual: {self.pagina_atual}")


# Função principal para simular o uso do histórico de navegação
def main():
    historico = HistoricoNavegacao()

    while True:
        print("\n--- Menu ---")
        print("1. Visitar uma página")
        print("2. Voltar para a página anterior")
        print("3. Exibir página atual")
        print("4. Exibir histórico completo")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pagina = input("Digite o nome da página a ser visitada: ")
            historico.visitar_pagina(pagina)
        elif opcao == "2":
            historico.voltar()
        elif opcao == "3":
            historico.exibir_pagina_atual()
        elif opcao == "4":
            historico.exibir_historico_completo()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executa o programa
if __name__ == "__main__":
    main()
