def newton_raphson(x0, e1, e2):
    """
    Implementa o método de Newton-Raphson para encontrar a raiz de uma função.
    - x0: Chute inicial para a raiz.
    - e1: Precisão desejada para o valor da função, ou seja, |f(x)| < e1.
    - e2: Precisão desejada para a diferença entre iterações consecutivas, ou seja, |x1 - x0| < e2.
    """

    # Verifica se o chute inicial já é uma solução suficientemente boa
    if abs(f(x0)) < e1:
        # Se o valor absoluto de f(x0) for menor que e1, x0 já é considerado uma boa aproximação para a raiz.
        return x0  # Retorna o chute inicial como a raiz encontrada.
    
    k = 0  # Inicializa o contador de iterações como 0, indicando que o processo está começando.
    
    # Início do loop principal do método de Newton-Raphson.
    while True:
        # Verifica se a derivada da função em x0 é igual a zero.
        # Isso é importante porque dividir por zero causaria um erro.
        if df(x0) == 0:
            # Caso a derivada seja zero, o método falha porque não pode calcular o próximo ponto.
            raise ValueError("A derivada é zero em x = {:.6f}. Método falhou.".format(x0))
        
        # Calcula o próximo valor de x usando a fórmula de Newton-Raphson:
        # x1 = x0 - f(x0) / df(x0).
        # Essa fórmula ajusta x0 com base no valor da função e na inclinação (derivada).
        x1 = x0 - f(x0) / df(x0)
        
        # Critério de parada 1: verifica se o valor de f(x1) é suficientemente pequeno.
        # Isso indica que x1 está próximo o suficiente da raiz verdadeira.
        if abs(f(x1)) < e1:
            return x1  # Retorna x1 como a raiz encontrada.

        # Critério de parada 2: verifica se a diferença entre x1 e x0 é menor que e2.
        # Isso indica que as iterações não estão mais mudando significativamente.
        if abs(x1 - x0) < e2:
            return x1  # Retorna x1 como a raiz encontrada.

        # Atualiza o valor de x0 para a próxima iteração, continuando o processo.
        x0 = x1

        # Incrementa o contador de iterações para acompanhar o progresso do método.
        k += 1
    

# Define a função f(x) cuja raiz será buscada.
def f(x):
    # A função é f(x) = x^2 - 2, ou seja, busca-se a raiz quadrada de 2.
    return x**2 - 2

# Define a derivada da função f(x).
def df(x):
    # A derivada de f(x) = x^2 - 2 é df(x) = 2x.
    return 2*x

# Define os critérios de precisão:
# e1: Precisão desejada para o valor da função.
# e2: Precisão desejada para a diferença entre iterações consecutivas.
e1, e2 = 1e-6, 1e-6  # Define as precisões como 10^-6.

# Define o chute inicial para a raiz.
x0 = 1  # Começa o processo com x0 = 1, que é uma estimativa inicial.

# Chama a função newton_raphson para encontrar a raiz da função f(x) com as precisões e o chute inicial definidos.
print(newton_raphson(x0, e1, e2))  # Imprime a raiz aproximada encontrada pelo método.

"""
Comentários gerais sobre o método:
==================================
1. **Funcionamento do método de Newton-Raphson:**
   - É um método iterativo para encontrar raízes de uma função f(x) a partir de um chute inicial x0.
   - A fórmula x1 = x0 - f(x0) / df(x0) utiliza a derivada para linearizar a função e ajustar o valor de x0.

2. **Convergência:**
   - O método converge rapidamente quando o chute inicial está próximo da raiz e a função é suficientemente bem comportada (suave e derivável).
   - No entanto, pode falhar se a derivada for zero ou se o chute inicial estiver longe da raiz.

3. **Critérios de parada:**
   - O método interrompe as iterações quando:
     a) |f(x1)| < e1: o valor da função é suficientemente próximo de zero (indicando que x1 é uma raiz).
     b) |x1 - x0| < e2: a diferença entre as iterações consecutivas é muito pequena (indicando que as iterações estabilizaram).

4. **Exemplo:**
   - A função f(x) = x^2 - 2 tem raízes em ±√2.
   - O chute inicial x0 = 1 converge para a raiz √2 ≈ 1.414213562.

5. **Cuidados:**
   - Verificar se a derivada é zero é crucial para evitar divisões por zero.
   - Se o método não convergir, pode ser necessário escolher um novo chute inicial ou usar um método alternativo.

"""
