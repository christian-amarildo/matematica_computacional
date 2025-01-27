# Define a função de cálculo por bissecção
def bisseccao(a, b, e):
    """
    Método da bisseção para encontrar uma raiz de uma função f(x) em um intervalo [a, b].
    - a: limite inferior do intervalo.
    - b: limite superior do intervalo.
    - e: precisão desejada para o cálculo (critério de parada).
    """

    # Verifica se o intervalo é válido aplicando a regra do sinal:
    # Se f(a) * f(b) >= 0, então não há raiz garantida no intervalo [a, b].
    if f(a) * f(b) >= 0:
        raise ValueError("Nesse intervalo não existe raíz")  # Levanta um erro caso a regra não seja atendida.

    i = 1  # Inicializa o contador de iterações com o valor 1 (primeira iteração).
    ai = a  # Define o limite inferior inicial (a).
    bi = b  # Define o limite superior inicial (b).

    # Exibe os valores iniciais do intervalo [a, b].
    print("Valores iniciais: a =", ai, "b =", bi)

    # Enquanto a diferença entre os limites do intervalo [bi - ai] for maior que a precisão e:
    while abs(bi - ai) > e:
        # Calcula o ponto médio do intervalo [ai, bi].
        xi = (ai + bi) / 2

        # Verifica em qual subintervalo [ai, xi] ou [xi, bi] está a raiz,
        # com base no critério do sinal f(ai) * f(xi).
        if f(ai) * f(xi) < 0:
            bi = xi  # Se o sinal mudar em [ai, xi], redefine o limite superior bi como xi.
        else:
            ai = xi  # Caso contrário, redefine o limite inferior ai como xi.

        # Exibe o estado atual da iteração, incluindo os valores atualizados de ai, bi e xi.
        print(f"Iteração {i}: a{i} = {ai}, b{i} = {bi}, x{i} = {xi}")

        i += 1  # Incrementa o contador de iterações.

    # Retorna o ponto médio do intervalo final [ai, bi] como a raiz aproximada.
    return (ai + bi) / 2

# Define a função f(x) cuja raiz será buscada.
def f(x):
    # A função é definida como f(x) = x^3 - 3x - 1.
    # Essa função possui uma raiz real que será encontrada pelo método da bisseção.
    return x**3 - 3*x - 1

# Define o intervalo inicial [a, b] em que a raiz será buscada.
a = -1  # Limite inferior do intervalo.
b = 0   # Limite superior do intervalo.

# Define a precisão desejada para o cálculo (critério de parada).
e = 0.15  # Precisão aceita para o intervalo final.

# Chama a função `bisseccao` para encontrar a raiz e imprime o resultado.
print(bisseccao(a, b, e))  # Exibe a raiz aproximada encontrada pelo método.

"""
Comentário sobre o funcionamento geral:
=======================================
1. **Condições do intervalo inicial:**
   - O método exige que f(a) * f(b) < 0, o que indica que há uma mudança de sinal em [a, b].
   - Essa mudança de sinal garante a existência de pelo menos uma raiz no intervalo.

2. **Divisão do intervalo:**
   - A cada iteração, o intervalo [a, b] é dividido ao meio.
   - A parte do intervalo em que a raiz não pode estar é descartada, reduzindo a área de busca pela metade.

3. **Critério de parada:**
   - O método para quando o tamanho do intervalo (|b - a|) é menor ou igual à precisão especificada (e).

4. **Eficiência:**
   - O método é eficiente para funções contínuas e garante convergência, desde que a condição inicial f(a) * f(b) < 0 seja satisfeita.

5. **Iteração manual:**
   - Em cada passo, o método verifica em qual subintervalo a raiz está localizada e redefine os limites a e b.

6. **Saída:**
   - A função retorna o valor médio do último intervalo como a raiz aproximada.
"""
