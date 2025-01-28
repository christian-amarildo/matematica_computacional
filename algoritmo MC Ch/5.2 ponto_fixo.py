# -*- coding: utf-8 -*-
"""
Calculadora de Raízes pelo Método de Ponto Fixo
==============================================

Este programa encontra a raiz de uma função contínua utilizando o Método de Ponto Fixo.

Funcionalidades:
1. Definição interativa da função g(x).
2. Entrada do ponto inicial x0.
3. Definição do critério de precisão.
4. Exibição detalhada de cada iteração do método.
5. Retorno da raiz aproximada com a precisão especificada.

Autor: ChatGPT
Data: 2025-01-27
"""

import math  # Importa o módulo math para funções matemáticas adicionais, se necessário

def f(x):
    """
    Define a função f(x) cuja raiz será buscada.

    Retorna:
        float: Valor de f(x)

    Nota:
        - Modifique esta função conforme necessário para buscar a raiz de diferentes funções.
        - Por exemplo, para f(x) = x^3 - 9x + 3, defina como abaixo.
    """
    return x**3 - 9*x + 3  # Exemplo de função. Modifique conforme necessário.

def ponto_fixo(g, x0, erro, max_iter=1000):
    """
    Implementa o Método de Ponto Fixo para encontrar a raiz de uma função f(x).

    Parâmetros:
        g (function): Função g(x) utilizada na iteração, tal que x = g(x).
        x0 (float): Ponto inicial para iniciar as iterações.
        erro (float): Critério de parada baseado na diferença entre iterações consecutivas.
        max_iter (int): Número máximo de iterações para evitar loops infinitos.

    Retorna:
        float: Raiz aproximada de f(x) no ponto fixo.
    
    Levanta:
        ValueError: Se o método não converge dentro do número máximo de iterações.
    """
    i = 0  # Inicializa o contador de iterações
    x = x0  # Define o ponto inicial
    
    print("\nIniciando o Método de Ponto Fixo...")
    print(f"Ponto inicial: x0 = {x0}")
    print(f"Critério de parada (erro): {erro}")
    print(f"Máximo de iterações: {max_iter}\n")
    
    while i < max_iter:
        x_novo = g(x)  # Calcula o próximo ponto usando a função g(x)
        diff = abs(x_novo - x)  # Calcula a diferença entre x_novo e x atual
        
        # Exibe os detalhes da iteração atual
        print(f"Iteração {i}: x = {x:.10f}, g(x) = {x_novo:.10f}, |g(x) - x| = {diff:.10f}")
        
        # Verifica se a diferença está dentro da precisão desejada
        if diff < erro:
            print("\nCritério de parada atendido.")
            print(f"Raiz aproximada: {x_novo:.10f}\n")
            return x_novo  # Retorna a raiz encontrada
        
        x = x_novo  # Atualiza o valor de x para a próxima iteração
        i += 1  # Incrementa o contador de iterações
    
    # Se o método não convergir dentro do número máximo de iterações, levanta um erro
    raise ValueError("O método de ponto fixo não convergiu dentro do número máximo de iterações.")

def main():
    """
    Função principal que controla o fluxo do programa.

    Executa as seguintes etapas:
    1. Exibe uma mensagem de boas-vindas.
    2. Solicita ao usuário a definição da função g(x).
    3. Solicita ao usuário o ponto inicial x0.
    4. Solicita ao usuário o critério de precisão.
    5. Executa o Método de Ponto Fixo para encontrar a raiz.
    6. Exibe o resultado final.
    7. Termina o programa.
    """
    # Exibe uma mensagem de boas-vindas e informações iniciais
    print("===========================================")
    print("      CALCULADORA DE RAÍZES - PONTO FIXO")
    print("===========================================\n")
    
    # Informa ao usuário sobre a função definida
    print("Por favor, defina a função g(x) utilizada no Método de Ponto Fixo.")
    print("A função g(x) deve estar isolada em x, ou seja, na forma x = g(x).")
    print("Exemplos:")
    print("1. Para f(x) = x^3 - 9x + 3, uma possível g(x) é g(x) = (9x - 3)^(1/3)")
    print("2. Para f(x) = x * log10(x) - 1, uma possível g(x) é g(x) = x - 1.3*(x * log10(x) - 1)\n")
    
    # Solicita ao usuário a escolha da função g(x)
    # Neste exemplo, vamos manter algumas funções pré-definidas para facilitar
    print("Escolha uma das funções g(x) pré-definidas:")
    print("[1] g(x) = (9*x - 3) ** (1/3)")
    print("[2] g(x) = (5*math.exp(-x))**2")
    print("[3] g(x) = 10 ** (1/x)")
    print("[4] g(x) = x - 1.3*(x * math.log10(x) - 1)")
    print("[5] Definir uma função personalizada")
    
    while True:
        try:
            escolha = int(input("\nDigite o número correspondente à sua escolha: "))
            if escolha not in [1, 2, 3, 4, 5]:
                print("Opção inválida. Por favor, escolha um número entre 1 e 5.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    # Define a função g(x) com base na escolha do usuário
    if escolha == 1:
        # g(x) = (9*x - 3) ** (1/3)
        g = lambda x: (9*x - 3) ** (1/3)
        print("\nFunção g(x) definida como: g(x) = (9*x - 3) ** (1/3)")
    elif escolha == 2:
        # g(x) = (5*math.exp(-x))**2
        g = lambda x: (5*math.exp(-x))**2
        print("\nFunção g(x) definida como: g(x) = (5*math.exp(-x))**2")
    elif escolha == 3:
        # g(x) = 10 ** (1/x)
        g = lambda x: 10 ** (1/x)
        print("\nFunção g(x) definida como: g(x) = 10 ** (1/x)")
    elif escolha == 4:
        # g(x) = x - 1.3*(x * math.log10(x) - 1)
        g = lambda x: x - 1.3*(x * math.log10(x) - 1)
        print("\nFunção g(x) definida como: g(x) = x - 1.3*(x * math.log10(x) - 1)")
    else:
        # Permite ao usuário definir uma função personalizada
        print("\nVocê escolheu definir uma função personalizada.")
        print("Por favor, insira a expressão de g(x) usando Python.")
        print("Use 'x' como a variável.")
        print("Exemplo: (9*x - 3) ** (1/3)")
        func_str = input("Digite a expressão de g(x): ")
        try:
            # Define a função g(x) a partir da expressão fornecida
            # Usa eval em um ambiente seguro com apenas o módulo math disponível
            g = lambda x: eval(func_str, {"math": math, "x": x, "e": math.e})
            # Testa a função com um valor inicial para garantir que está correta
            teste = g(1)
            print(f"\nFunção g(x) definida como: g(x) = {func_str}")
        except Exception as e:
            print(f"\nErro ao definir a função g(x): {e}")
            print("Por favor, verifique a expressão e tente novamente.")
            return  # Encerra o programa em caso de erro na definição da função
    
    # Solicita ao usuário o ponto inicial x0
    while True:
        try:
            x0 = float(input("\nDigite o ponto inicial (x0) para iniciar as iterações: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    
    # Solicita ao usuário a precisão desejada
    while True:
        try:
            erro = float(input("Digite a precisão desejada para a convergência (exemplo: 1e-6): "))
            if erro <= 0:
                print("A precisão deve ser um número positivo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    
    # Executa o Método de Ponto Fixo para encontrar a raiz
    try:
        raiz = ponto_fixo(g, x0, erro)
        print(f"Resultado: A raiz aproximada de f(x) pelo Método de Ponto Fixo é: {raiz:.10f}")
    except ValueError as ve:
        # Trata erros levantados pelo método de ponto fixo, como falta de convergência
        print(f"\nErro: {ve}")
    
    # Exibe uma mensagem de encerramento
    print("===========================================")
    print("       FIM DA CALCULADORA DE RAÍZES")
    print("===========================================\n")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
