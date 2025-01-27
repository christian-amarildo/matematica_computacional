def gauss_jacobi(A, b, e, max_i):
    """
    Método iterativo de Gauss-Jacobi para resolver um sistema linear Ax = b.
    A: Matriz dos coeficientes (n x n).
    b: Vetor dos termos independentes (tamanho n).
    e: Precisão desejada (erro máximo aceitável).
    max_i: Número máximo de iterações permitidas.
    Retorna o vetor solução x após a convergência ou após max_i iterações.
    """
    
    n = len(b)  # n é o número de equações, que é igual ao tamanho do vetor b (também ao número de linhas de A).
    
    # Inicializando o vetor de soluções com zeros. x é a solução atual, inicializada em [0, 0, ..., 0].
    x = [0.0] * n  # x armazena a solução em cada iteração. Inicialmente, todos os valores são zero.

    # Inicializando o vetor x_novo, que armazena os novos valores calculados em cada iteração.
    x_novo = [0.0] * n  # x_novo irá armazenar a solução calculada na iteração atual.

    # Laço que executa o máximo de iterações permitidas (max_i).
    for k in range(max_i):
        
        # Laço que percorre cada equação do sistema linear.
        for i in range(n):
            soma = b[i]  # Inicia a soma com o valor b[i], que é o termo independente da equação i.

            # Laço que percorre todas as variáveis (colunas) para calcular a soma.
            for j in range(n):
                # Se a variável j não for igual à variável i, soma o valor de A[i][j] * x[j].
                if i != j:
                    soma -= A[i][j] * x[j]  # Subtrai o valor de A[i][j] multiplicado pelo valor de x[j].

            # Agora, a soma contém o valor de b[i] menos as contribuições das outras variáveis.
            # O valor de x_novo[i] é calculado dividindo a soma pela diagonal A[i][i].
            x_novo[i] = soma / A[i][i]  # Resolve a equação para a variável i (x_novo[i] é o novo valor de x[i]).

        # Calcular o erro total entre a solução anterior (x) e a nova solução (x_novo).
        e_total = 0.0  # e_total acumula o erro total, que será comparado com a precisão desejada (e).

        # Laço que percorre todas as variáveis e calcula o erro.
        for i in range(n):
            e_total += abs(x_novo[i] - x[i])  # A soma do erro absoluto de cada variável.

        # Se o erro total for menor que a precisão desejada (e), isso significa que a solução convergiu.
        if e_total < e:
            return x_novo  # Retorna a solução calculada, pois a convergência foi atingida.

        # Atualiza o vetor x com os valores calculados em x_novo para a próxima iteração.
        x = x_novo[:]  # Copia o conteúdo de x_novo para x (agora x se torna a solução atualizada).

    # Se o número máximo de iterações foi atingido e a solução não convergiu, exibe uma mensagem.
    print("Número máximo de iterações atingido:", max_i)  # Informa que o número máximo de iterações foi alcançado.

    # Retorna a solução após o número máximo de iterações.
    return x_novo  # Retorna a última aproximação encontrada, mesmo que o método não tenha convergido.

# Exemplo de uso do método de Gauss-Jacobi:

# Matriz dos coeficientes (sistema de equações lineares).
A = [[10, 2, 1],  # Primeira equação: 10x1 + 2x2 + x3 = 7
     [1, 5, 1],   # Segunda equação: x1 + 5x2 + x3 = -8
     [2, 3, 10]]  # Terceira equação: 2x1 + 3x2 + 10x3 = 6

# Vetor dos termos independentes (lado direito do sistema).
b = [7, -8, 6]  # Os valores de b correspondem aos resultados das equações: [7, -8, 6].

# Precisão desejada (erro máximo permitido entre iterações).
e = 1e-6  # A precisão desejada é 10^-6, ou seja, o erro total entre duas iterações deve ser menor que 10^-6.

# Número máximo de iterações permitidas.
max_i = 100  # O número máximo de iterações será 100. Se não houver convergência antes disso, o método será interrompido.

# Chama a função gauss_jacobi com os parâmetros definidos.
resultado = gauss_jacobi(A, b, e, max_i)  # A função retorna o vetor solução aproximada para o sistema.

# Imprime a solução calculada.
print("Solução:", resultado)  # Exibe a solução final após a execução do método de Gauss-Jacobi.

"""
Comentários gerais sobre o código:
===================================
1. **Método de Gauss-Jacobi:**
   - Gauss-Jacobi é um método iterativo para resolver sistemas de equações lineares. Ele usa as soluções da iteração anterior para calcular as soluções da iteração atual, até que a solução converja para um valor suficientemente preciso ou um número máximo de iterações seja alcançado.

2. **Fórmula de atualização:**
   - A fórmula de atualização usada no método de Gauss-Jacobi para cada variável é dada por:
     x_i^(k+1) = (b_i - somatório(A[i][j] * x_j)) / A[i][i]
   - Ou seja, a solução de uma variável depende das soluções das outras variáveis na iteração anterior.

3. **Critério de parada:**
   - O critério de parada é baseado no erro total entre a solução atual e a solução anterior. Se o erro total for menor que a precisão desejada (e), o método para e retorna a solução.

4. **Número máximo de iterações:**
   - Caso o método não converja antes de atingir o número máximo de iterações, uma mensagem é exibida e a última solução calculada é retornada. Isso garante que o método não entre em um loop infinito em casos onde a convergência não ocorre.

5. **Exemplo prático:**
   - O exemplo fornecido resolve o sistema linear Ax = b usando o método de Gauss-Jacobi, onde A é uma matriz 3x3 e b é um vetor de 3 elementos. A solução final é impressa após a convergência do método ou após o número máximo de iterações.

6. **Eficiência:**
   - O método de Gauss-Jacobi pode ser lento em sistemas grandes ou quando a matriz não é bem condicionada. Métodos como Gauss-Seidel ou LU com pivotamento podem ser mais eficientes em tais casos.
"""
