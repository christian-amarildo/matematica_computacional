from math import e  # Importa a constante matemática 'e' (base do logaritmo natural) do módulo math.

# Define a função que implementa o método da posição falsa
def posicao_falsa(a, b, e1, e2):
    """
    Método da posição falsa para encontrar a raiz de uma função f(x) no intervalo [a, b].
    - a: Limite inferior do intervalo inicial.
    - b: Limite superior do intervalo inicial.
    - e1: Critério de parada baseado na largura do intervalo.
    - e2: Critério de parada baseado na proximidade de f(x) de 0.
    """

    # Regra do sinal: verifica se existe raiz no intervalo [a, b].
    # Para garantir isso, f(a) * f(b) deve ser menor que 0 (mudança de sinal).
    if f(a) * f(b) >= 0:
        raise ValueError("Nesse intervalo não existe raíz")  # Levanta um erro caso a condição não seja atendida.

    k = 1  # Inicializa o contador de iterações, começando pela iteração 1.

    # Exibe os valores iniciais do intervalo [a, b] para referência.
    print(f"Valores iniciais: a = {a}, b = {b}")

    # Verifica se o intervalo inicial já é suficientemente pequeno para atender à precisão e1.
    if abs(b - a) < e1:
        # Se o valor de f(a) for suficientemente próximo de 0, retorna a como a raiz.
        if abs(f(a)) < e2:
            return a
        # Se o valor de f(b) for suficientemente próximo de 0, retorna b como a raiz.
        elif abs(f(b)) < e2:
            return b
        # Caso contrário, retorna o ponto médio do intervalo como aproximação da raiz.
        else:
            return (a + b) / 2

    # Loop infinito para executar o método da posição falsa até atingir os critérios de parada.
    while True:
        # Calcula o ponto de posição falsa usando a fórmula específica do método.
        # Esse ponto é uma aproximação da raiz com base na linearização da função no intervalo.
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))

        # Verifica se o valor de f(x) é suficientemente pequeno, com base no critério e2.
        # Isso indica que x é uma boa aproximação da raiz.
        if abs(f(x)) < e2:
            return x  # Retorna x como a raiz encontrada.

        # Atualiza os limites do intervalo [a, b] com base no sinal de f(x).
        # Se f(a) * f(x) > 0, significa que a raiz está no intervalo [x, b].
        if f(a) * f(x) > 0:
            a = x  # Atualiza o limite inferior a para x.
        else:
            b = x  # Caso contrário, atualiza o limite superior b para x.

        # Exibe o estado atual da iteração, incluindo os novos valores de a, b e o índice da iteração.
        print(f"Iteração {k}: a{k} = {a}, b{k} = {b}")

        # Verifica o critério de parada baseado na largura do intervalo [b - a].
        # Se a largura do intervalo for menor que e1, considera que a raiz foi encontrada.
        if abs(b - a) < e1:
            return x  # Retorna x como a raiz aproximada.

        k += 1  # Incrementa o contador de iterações.

# Define a função f(x) cuja raiz será buscada.
def f(x):
    # A função é definida como f(x) = e^(-2x) - x^2.
    # Esta é uma função contínua e diferenciável, adequada para o método da posição falsa.
    return e**(-2*x) - x**2

# Define os limites do intervalo inicial [a, b].
a = 0  # Limite inferior do intervalo.
b = 2  # Limite superior do intervalo.

# Define os critérios de parada:
# e1: Precisão em relação à largura do intervalo [a, b].
# e2: Precisão em relação ao valor absoluto de f(x).
e1 = 1e-6  # Tolerância para a largura do intervalo.
e2 = 1e-6  # Tolerância para a proximidade de f(x) de 0.

# Chama a função `posicao_falsa` para encontrar a raiz e imprime o resultado.
print("Resultado:", posicao_falsa(a, b, e1, e2))  # Exibe a raiz aproximada encontrada pelo método.

"""
Comentários gerais sobre o método:
==================================
1. **Regra do sinal:**
   - A condição f(a) * f(b) < 0 garante que a função muda de sinal no intervalo [a, b].
   - Essa mudança de sinal indica a presença de pelo menos uma raiz nesse intervalo, assumindo que a função é contínua.

2. **Método da posição falsa:**
   - Este método utiliza uma aproximação linear para encontrar a raiz em um intervalo.
   - A fórmula do ponto de posição falsa calcula a interseção da reta que conecta os pontos (a, f(a)) e (b, f(b)) com o eixo x.

3. **Critérios de parada:**
   - O cálculo é interrompido quando:
     a) O valor de |f(x)| é menor que e2 (a raiz foi encontrada com precisão suficiente).
     b) A largura do intervalo |b - a| é menor que e1 (o intervalo é suficientemente pequeno).

4. **Eficiência:**
   - O método é eficiente para funções contínuas e pode convergir rapidamente se o intervalo inicial for escolhido adequadamente.

5. **Exemplo da função f(x):**
   - A função f(x) = e^(-2x) - x^2 possui uma raiz real no intervalo [0, 2].
   - O método da posição falsa encontra essa raiz aproximada com base nos critérios de parada definidos.

"""
