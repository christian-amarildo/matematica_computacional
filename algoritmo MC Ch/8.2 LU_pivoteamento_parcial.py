def lu_decomposition_with_pivoting(A, b):
    """
    Resolve um sistema linear Ax = b utilizando a decomposição LU com pivotamento parcial.
    - A: Matriz dos coeficientes (n x n).
    - b: Vetor de constantes (tamanho n).
    - Retorna o vetor solução x.
    """
    
    n = len(A)  # n é o número de linhas da matriz A (também o número de colunas, pois A é quadrada).

    # Inicialização do vetor de permutação p (representa a troca de linhas durante o pivotamento).
    p = list(range(n))  # p é uma lista que armazena os índices das linhas de A após o pivotamento.

    # Decomposição LU com pivotamento parcial (soma da matriz L e U).
    for k in range(n - 1):  # k percorre as colunas de 0 até n-2 (para cada passo da decomposição).
        
        # Encontrar o pivô, ou seja, o maior valor absoluto na coluna atual.
        pv = abs(A[k][k])  # Inicializa pv com o valor absoluto do elemento A[k][k].
        r = k  # Inicializa r como o índice da linha k.
        
        for i in range(k + 1, n):  # Percorre as linhas abaixo de k para encontrar o pivô.
            if abs(A[i][k]) > pv:  # Se o valor absoluto de A[i][k] for maior que o pivô atual.
                pv = abs(A[i][k])  # Atualiza o pivô com o novo valor.
                r = i  # Atualiza o índice da linha do pivô.

        if pv == 0:  # Se o pivô encontrado é zero, significa que a matriz A é singular.
            raise ValueError("A matriz A é singular.")  # Levanta um erro informando que a matriz não tem solução.

        # Troca as linhas k e r, tanto na matriz A quanto no vetor de permutação p.
        if r != k:  # Se o pivô não está na posição k, as linhas devem ser trocadas.
            p[k], p[r] = p[r], p[k]  # Troca as posições de k e r no vetor p.
            A[k], A[r] = A[r], A[k]  # Troca as linhas k e r na matriz A.

        # Atualização da matriz A: calcula os multiplicadores m e atualiza os valores abaixo do pivô.
        for i in range(k + 1, n):  # Percorre as linhas abaixo de k (de k+1 até n-1).
            m = A[i][k] / A[k][k]  # Calcula o multiplicador m, que é o valor A[i][k] dividido pelo pivô A[k][k].
            A[i][k] = m  # Armazena o valor de m na matriz A.
            for j in range(k + 1, n):  # Percorre as colunas à direita do pivô para atualizar os valores de A.
                A[i][j] -= m * A[k][j]  # Subtrai m * A[k][j] de A[i][j], o que faz A ficar triangular superior.

    # Substituição de Pb: Agora que A foi decomposta, é preciso atualizar o vetor b.
    c = [0] * n  # Inicializa o vetor c com zeros, que será a versão modificada de b após o pivotamento.
    for i in range(n):  # Para cada linha da matriz A.
        r = p[i]  # r recebe o índice da linha permutada do vetor p.
        c[i] = b[r]  # Atualiza c[i] com o valor de b[r], trocando os elementos conforme o vetor de permutação p.

    # Substituição direta Ly = c: Resolve o sistema triangular inferior Ly = c.
    y = [0] * n  # Inicializa o vetor y com zeros. Este vetor vai armazenar a solução intermediária.
    for i in range(n):  # Para cada linha de L (e y).
        soma = 0  # Variável que acumula a soma de L[i][j] * y[j] para j < i.
        for j in range(i):  # Percorre as colunas à esquerda de i (todas as colunas de L até a diagonal).
            soma += A[i][j] * y[j]  # Soma os termos L[i][j] * y[j].
        y[i] = c[i] - soma  # Atualiza y[i] subtraindo soma de c[i].

    # Substituição retroativa Ux = y: Resolve o sistema triangular superior Ux = y.
    x = [0] * n  # Inicializa o vetor x com zeros. Este vetor será a solução final.
    for i in range(n - 1, -1, -1):  # i percorre de n-1 até 0 (de baixo para cima, devido à estrutura triangular superior de U).
        soma = 0  # Variável que acumula a soma de U[i][j] * x[j] para j > i.
        for j in range(i + 1, n):  # Percorre as colunas à direita de i (todas as colunas de U após a diagonal).
            soma += A[i][j] * x[j]  # Soma os termos U[i][j] * x[j].
        x[i] = (y[i] - soma) / A[i][i]  # Atualiza x[i] dividindo a diferença y[i] - soma por A[i][i].

    return x  # Retorna o vetor solução x, que é a solução do sistema Ax = b.

# Exemplo de uso:

# Matriz de coeficientes A (3x3).
A = [
    [2, -1, -2],  # Primeira linha da matriz A.
    [-4, 6, 3],   # Segunda linha da matriz A.
    [-4, -2, 8]   # Terceira linha da matriz A.
]

# Vetor b de constantes (tamanho 3).
b = [1, 2, 3]  # O vetor b contém os valores do lado direito das equações.

# Chama a função de decomposição LU com pivotamento para resolver o sistema linear.
x = lu_decomposition_with_pivoting(A, b)  # x será o vetor solução calculado pela decomposição LU com pivotamento.

# Exibe a solução do sistema linear.
print("Solução:", x)  # Imprime o vetor solução x.

"""
Comentários gerais sobre o código:
===================================
1. **Pivotamento parcial:**
   - O método de decomposição LU com pivotamento tem como objetivo evitar a divisão por números pequenos ou zero, o que pode causar instabilidade numérica. Isso é feito trocando as linhas da matriz A de modo que o maior valor absoluto seja usado como pivô em cada etapa.

2. **Decomposição LU:**
   - A decomposição LU é uma técnica em que a matriz A é decomposta em uma matriz triangular inferior L e uma matriz triangular superior U, tal que A = L * U. O algoritmo também realiza pivotamento para garantir estabilidade numérica.

3. **Substituição direta e retroativa:**
   - Após decompor A em L e U, o sistema linear Ax = b é resolvido em duas etapas: a substituição direta (Ly = c) e a substituição retroativa (Ux = y), que são necessárias devido à estrutura triangular de L e U.

4. **Vetor de permutação:**
   - O vetor de permutação p armazena a ordem das linhas da matriz A após o pivotamento. Isso é necessário para garantir que o vetor b também seja reorganizado corretamente.

5. **Solução final:**
   - O vetor x obtido no final contém a solução do sistema linear, e é retornado pela função.
"""
