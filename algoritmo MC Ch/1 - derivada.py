import sympy as sp  # Importa a biblioteca SymPy para realizar cálculos simbólicos.

# Função para exibir o menu principal com as opções de tipos de derivadas.
def menu():
    print("\nEscolha o tipo de derivada:")  # Exibe o título do menu.
    print("1. Derivada Simples")  # Opção para derivada simples.
    print("2. Regra da Cadeia")  # Opção para aplicar a regra da cadeia.
    print("3. Derivada Parcial")  # Opção para calcular derivadas parciais.
    print("0. Sair")  # Opção para sair do programa.
    return int(input("Digite sua escolha: "))  # Retorna a escolha do usuário como um inteiro.

# Função para calcular derivadas utilizando a biblioteca SymPy.
def derivada_com_sympy():
    print("\n[Usando Sympy]")  # Indica que o método SymPy será usado.
    # Define as variáveis simbólicas x, y, z que serão usadas nas expressões matemáticas.
    x, y, z = sp.symbols('x y z')

    escolha = menu()  # Chama o menu e armazena a escolha do usuário.
    if escolha == 1:  # Verifica se o usuário escolheu derivada simples.
        funcao = input("Digite a função em relação a x (ex: x**2 + 3*x): ")  # Solicita a função ao usuário.
        funcao_sympy = sp.sympify(funcao)  # Converte a string da função para uma expressão SymPy.
        print("Derivada:", sp.diff(funcao_sympy, x))  # Calcula e exibe a derivada em relação a x.

    elif escolha == 2:  # Verifica se o usuário escolheu a regra da cadeia.
        funcao = input("Digite a função externa f(x) (ex: sin(x)): ")  # Solicita a função externa.
        interna = input("Digite a função interna g(x) (ex: x**2): ")  # Solicita a função interna.
        f = sp.sympify(funcao)  # Converte a função externa para uma expressão SymPy.
        g = sp.sympify(interna)  # Converte a função interna para uma expressão SymPy.
        # Aplica a regra da cadeia: derivada de f(g(x)) = f'(g(x)) * g'(x).
        derivada = sp.diff(f, x).subs(x, g) * sp.diff(g, x)
        print("Resultado da regra da cadeia:", derivada)  # Exibe o resultado da regra da cadeia.

    elif escolha == 3:  # Verifica se o usuário escolheu derivada parcial.
        funcao = input("Digite a função multivariada (ex: x**2 + y**2 + z**2): ")  # Solicita a função multivariada.
        variavel = input("Escolha a variável para derivar (x, y ou z): ")  # Solicita a variável de derivação.
        funcao_sympy = sp.sympify(funcao)  # Converte a função para uma expressão SymPy.
        # Calcula a derivada parcial em relação à variável escolhida.
        print(f"Derivada parcial em relação a {variavel}:", sp.diff(funcao_sympy, sp.Symbol(variavel)))

    else:  # Caso o usuário insira uma opção inválida.
        print("Opção inválida.")  # Exibe uma mensagem de erro.

# Função para calcular derivadas sem o uso da biblioteca SymPy.
def derivada_sem_sympy():
    print("\n[Sem Sympy]")  # Indica que o método sem SymPy será usado.
    escolha = menu()  # Chama o menu e armazena a escolha do usuário.

    if escolha == 1:  # Verifica se o usuário escolheu derivada simples.
        # Solicita os coeficientes do polinômio, separados por espaços, e converte para uma lista de floats.
        coeficientes = list(map(float, input("Digite os coeficientes do polinômio (ordem decrescente): ").split()))
        derivada = []  # Lista para armazenar os coeficientes da derivada.
        n = len(coeficientes) - 1  # Determina o maior expoente do polinômio.
        for i, coef in enumerate(coeficientes):  # Itera sobre os coeficientes do polinômio.
            if n - i >= 1:  # Ignora o termo constante (expoente 0).
                derivada.append(coef * (n - i))  # Calcula o novo coeficiente multiplicando pelo expoente.
        print("Derivada do polinômio:", derivada)  # Exibe os coeficientes da derivada.

    elif escolha == 2:  # Verifica se o usuário escolheu a regra da cadeia.
        # Define uma função anônima para calcular f'(g(x)), solicitando o valor ao usuário.
        def f_prime(x):
            return float(input("Digite o valor de f'(g(x)): "))

        # Define uma função anônima para calcular g'(x), solicitando o valor ao usuário.
        def g_prime(x):
            return float(input("Digite o valor de g'(x): "))
        g_x = float(input("Digite o valor de g(x): "))  # Solicita o valor de g(x).
        x = float(input("Digite o valor de x: "))  # Solicita o valor de x.
        # Calcula e exibe o resultado da regra da cadeia: f'(g(x)) * g'(
