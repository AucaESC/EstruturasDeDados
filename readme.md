# Projeto: Histórico de Navegação em um Navegador

Este projeto simula o funcionamento do histórico de navegação em um navegador web utilizando a estrutura de dados **pilha (stack)**. A pilha é ideal para esse cenário, pois segue o princípio **LIFO (Last In, First Out)**, onde a última página visitada é a primeira a ser acessada ao voltar.

---

## Funcionalidades

1. **Visitar uma página**:
   - Adiciona a página ao topo do histórico.
2. **Voltar para a página anterior**:
   - Remove a página atual do histórico e retorna à página anterior.
3. **Exibir página atual**:
   - Mostra a página que está sendo visualizada no momento.
4. **Exibir histórico completo**:
   - Mostra todas as páginas visitadas até o momento.

---

## Como Funciona

O histórico de navegação é implementado usando uma pilha. Cada nova página visitada é **empilhada**, e ao clicar em "Voltar", a última página é **desempilhada**.

### Exemplo de Funcionamento:
1. O usuário visita as páginas na seguinte ordem:
   - `página1.com`
   - `página2.com`
   - `página3.com`
2. Ao clicar em "Voltar":
   - O sistema remove `página3.com` e retorna para `página2.com`.

---

## Estrutura do Projeto

O projeto é composto por um único arquivo Python (`historico_navegacao.py`) que contém a implementação do histórico de navegação.


## Alunos

Igor de Sousa Vieira Araujo 
Pedro Henrique Moraes Amaral 
Cauã Eduardo Silva de Carvalho Mendes 
