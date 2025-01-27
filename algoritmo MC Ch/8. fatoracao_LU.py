def fatoracao_LU(A, b):
    """
    Resolve um sistema linear Ax = b utilizando a decomposição LU.
    - A: Matriz dos coeficientes (n x n).
    - b: Vetor de constantes (tamanho n).
    - Retorna o vetor solução x.
    """
    n = len(A)  # n é o número de linhas da matriz A (também o número de colunas, pois A é quadrada).

    # Verificação se a matriz A é quadrada (n x n)
    for row in A:  # Percorre todas as linhas de A.
        if len(row) != n:  # Verifica se a quantidade de colunas de cada linha é igual a n (condição para ser quadrada).
            raise ValueError("A matriz deve ser quadrada")  # Se a matriz não for quadrada, levanta um erro.

    # Inicializando as matrizes L e U com zeros.
    # L será a matriz triangular inferior (com 1s na diagonal principal).
    # U será a matriz triangular superior.
    L = [[0] * n for _ in range(n)]  # Cria uma matriz n x n com zeros para L.
    U = [[0] * n for _ in range(n)]  # Cria uma matriz n x n com zeros para U.

    # Decomposição LU: A matriz A será decomposta nas matrizes L e U, de forma que A = L * U.
    for i in range(n):  # i percorre as linhas da matriz A.
        
        # Preenche a matriz U (triangular superior).
        for j in range(i, n):  # j percorre as colunas de i até n (para manter a triangularidade superior).
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))  # Calcula o elemento U[i][j] com a fórmula da decomposição LU.
        
        # Preenche a matriz L (triangular inferior).
        for j in range(i, n):  # j percorre as linhas a partir de i até n.
            if i == j:  # Quando i == j, L[i][i] é 1 (na diagonal principal).
                L[i][i] = 1  # A diagonal de L é 1.
            else:
                # Caso contrário, calcula os elementos abaixo da diagonal de L.
                L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]  # Calcula o valor L[j][i].

    # Agora, L e U estão calculadas, e podemos resolver o sistema em duas etapas: Ly = b e Ux = y.

    # Substituição para frente: Resolver Ly = b (triangular inferior).
    y = [0] * n  # Inicializa o vetor y com zeros. Esse vetor armazena as soluções intermediárias.
    for i in range(n):  # i percorre as linhas de 0 até n-1.
        # Calcula o valor de y[i] somando os valores de L[i][j] * y[j] para j < i.
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))  # Calcula a solução de Ly = b para y[i].

    # Substituição para trás: Resolver Ux = y (triangular superior).
    x = [0] * n  # Inicializa o vetor solução x com zeros.
    for i in range(n - 1, -1, -1):  # i percorre as linhas de n-1 até 0 (de baixo para cima).
        if U[i][i] == 0:  # Verifica se o elemento diagonal de U[i][i] é zero (não pode dividir por zero).
            raise ValueError("Sistema não tem solução única (divisão por zero detectada).")  # Levanta um erro caso U[i][i] seja zero.

        # Calcula o valor de x[i] somando os valores de U[i][j] * x[j] para j > i e subtraindo de y[i].
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]  # Calcula a solução para x[i].

    return x  # Retorna o vetor solução x.

# Exemplo:

# Definição da matriz de coeficientes A (2x2).
A = [
    [4, 3],  # Primeira linha da matriz A.
    [6, 3]   # Segunda linha da matriz A.
]

# Definição do vetor b de constantes (tamanho 2).
b = [10, 12]  # O vetor b contém os valores do lado direito das equações.

# Chama a função fatoracao_LU para resolver o sistema linear Ax = b.
x = fatoracao_LU(A, b)  # x será o vetor solução calculado pela decomposição LU.

# Exibe a solução do sistema linear.
print("Solução:", x)  # Imprime o vetor solução x.

"""
Comentários gerais sobre o código:
===================================
1. **Verificação da matriz quadrada:**
   - A função começa verificando se a matriz A é quadrada (mesmo número de linhas e colunas). Caso contrário, um erro é levantado, pois a decomposição LU só pode ser feita em matrizes quadradas.

2. **Decomposição LU:**
   - A decomposição LU consiste em decompor a matriz A em duas matrizes: L (triangular inferior) e U (triangular superior). A matriz A é representada como A = L * U.
   - A matriz L tem 1s na diagonal principal, enquanto a matriz U tem todos os elementos acima (e na diagonal) da linha principal.

3. **Substituição para frente:**
   - Após calcular L e U, a solução do sistema linear é realizada em duas etapas. Primeiro, resolve-se Ly = b usando a substituição para frente. A matriz L é triangular inferior, o que permite resolver as equações da parte superior para baixo.

4. **Substituição para trás:**
   - Em seguida, resolve-se Ux = y usando a substituição para trás. A matriz U é triangular superior, o que permite resolver as equações da parte inferior para cima.

5. **Verificação de divisão por zero:**
   - Durante o cálculo de U e na substituição retroativa, é verificado se algum elemento diagonal de U é zero. Se for, o código levanta um erro, pois o sistema não terá uma solução única (será indeterminado ou terá infinita solução).

6. **Solução final:**
   - O vetor x contém a solução do sistema linear Ax = b, que é obtido após a decomposição LU de A e as substituições para frente e para trás.

"""
