def eliminacao(A, b):
    """
    Realiza a eliminação de Gauss para transformar a matriz A em uma matriz triangular superior.
    - A: Matriz de coeficientes (n x n).
    - b: Vetor de constantes (tamanho n).
    - Retorna A (modificada) e b (modificado) após a eliminação de Gauss.
    """
    n = len(A)  # n é o número de linhas da matriz A, que deve ser quadrada (n x n).

    # Eliminação de Gauss: transforma A em uma matriz triangular superior.
    for k in range(n):  # k é o índice da linha atual sendo processada.
        for i in range(k + 1, n):  # i é o índice das linhas abaixo da linha k.
            
            if A[k][k] == 0:  # Verifica se o pivô (A[k][k]) é zero.
                # Se o pivô for zero, não é possível realizar a eliminação corretamente.
                # Isso significa que a matriz é singular e o sistema não tem solução única.
                raise ValueError("Matriz singular, não é possível continuar.")  # Levanta um erro caso a matriz seja singular.
            
            # Calcula o multiplicador m que será usado para zerar os elementos abaixo do pivô.
            m = A[i][k] / A[k][k]  # A[i][k] é o elemento na linha i e coluna k, A[k][k] é o pivô.
            
            # Realiza a eliminação da linha i, subtraindo um múltiplo da linha k de A[i].
            for j in range(k, n):  # j percorre as colunas a partir da coluna k até a última coluna.
                A[i][j] -= m * A[k][j]  # Atualiza a linha i da matriz A, subtraindo o múltiplo da linha k.
            
            # Atualiza o vetor b, subtraindo m vezes o valor de b[k] de b[i].
            b[i] -= m * b[k]  # Atualiza a constante associada à linha i do vetor b.

    return A, b  # Retorna a matriz A modificada e o vetor b modificado após a eliminação de Gauss.

def resolucao_sistema(A, b):
    """
    Resolve o sistema linear Ax = b utilizando substituição retroativa após a eliminação de Gauss.
    - A: Matriz triangular superior (n x n).
    - b: Vetor de constantes (tamanho n).
    - Retorna o vetor solução x.
    """
    n = len(A)  # n é o número de variáveis, ou seja, o número de linhas/colunas da matriz A.

    x = [0] * n  # Inicializa o vetor solução x com zeros. Será preenchido durante a substituição retroativa.

    # Inicia a substituição retroativa a partir da última linha.
    x[n-1] = b[n-1] / A[n-1][n-1]  # A última variável (x[n-1]) é calculada diretamente pela equação A[n-1][n-1] * x[n-1] = b[n-1].

    # Agora realiza a substituição retroativa para as variáveis anteriores, de n-2 até 0.
    for k in range(n-2, -1, -1):  # k percorre as linhas de baixo para cima, da penúltima linha até a primeira.
        s = 0  # Inicializa a soma s que acumula os termos já conhecidos da equação.

        # Soma os termos já conhecidos para a linha k.
        for j in range(k+1, n):  # j percorre as colunas à direita do pivô.
            s += A[k][j] * x[j]  # Acumula os valores já conhecidos da solução (x[j]).

        # Calcula o valor de x[k] isolando-o na equação A[k][k] * x[k] = b[k] - s.
        x[k] = (b[k] - s) / A[k][k]  # x[k] é calculado dividindo o valor restante pela diagonal de A[k][k].

    return x  # Retorna o vetor solução x.

# Exemplo:

# Define a matriz de coeficientes A do sistema linear.
A = [
    [1, 1, 0, 3],  # A primeira linha da matriz A.
    [2, 1, -1, 1],  # A segunda linha da matriz A.
    [3, -1, -1, 2],  # A terceira linha da matriz A.
    [-1, 2, 3, -1]  # A quarta linha da matriz A.
]

# Define o vetor de constantes b do sistema linear.
b = [4, 1, -3, 4]  # b contém as constantes de cada equação.

# Passo 1: Eliminação de Gauss
# A função eliminacao é chamada para transformar a matriz A em uma matriz triangular superior.
A, b = eliminacao(A, b)  # A e b são modificados pela função eliminacao.

# Passo 2: Substituição retroativa
# Agora que A é triangular superior, a função resolucao_sistema pode ser chamada para resolver o sistema.
x = resolucao_sistema(A, b)  # A solução x do sistema é calculada.

# Imprime o vetor solução x, que contém as soluções para as incógnitas do sistema.
print(x)  # Exibe a solução do sistema linear.

"""
Comentários gerais sobre o código:
===================================
1. **Eliminação de Gauss:**
   - O método de eliminação de Gauss é usado para transformar uma matriz em uma matriz triangular superior, facilitando a resolução do sistema linear por substituição retroativa.
   - Se a matriz A for singular (ou seja, tiver um pivô igual a zero), o código levanta um erro, pois o sistema não terá uma solução única ou terá infinitas soluções.

2. **Substituição retroativa:**
   - Após a eliminação de Gauss, a matriz A se torna triangular superior, o que permite resolver o sistema linear de forma eficiente.
   - A substituição retroativa é realizada de baixo para cima, começando pela última variável e calculando as variáveis anteriores.

3. **Resolução de sistemas lineares:**
   - O código resolve sistemas lineares de 4 equações com 4 incógnitas.
   - O exemplo mostrado usa uma matriz A de 4x4 e um vetor b de tamanho 4.
   - A solução é encontrada em duas etapas: eliminação de Gauss para triangularizar a matriz e substituição retroativa para encontrar as soluções das variáveis.

4. **Considerações sobre a matriz A:**
   - A matriz A deve ser quadrada (ou seja, ter o mesmo número de linhas e colunas).
   - Caso a matriz A seja singular (tiver um pivô igual a zero), o sistema não tem solução única, e o código levanta um erro.

5. **Solução final:**
   - O vetor solução x contém os valores das incógnitas do sistema linear, que são calculados após a eliminação de Gauss e a substituição retroativa.
"""
