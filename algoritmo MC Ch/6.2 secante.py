import math  # Importa a biblioteca matemática para usar funções como a exponencial (math.e) e o cosseno (math.cos).

def secante(x0, x1, e1, e2):
    """
    Implementa o método da Secante para encontrar a raiz de uma função.
    - x0, x1: Chutes iniciais para as raízes (dois pontos diferentes para iniciar o método).
    - e1: Precisão desejada para o valor da função, ou seja, |f(x2)| < e1.
    - e2: Precisão desejada para a diferença entre iterações consecutivas, ou seja, |x2 - x1| < e2.
    """
    
    # Verifica se o valor de f(x0) já está suficientemente perto de zero (raiz).
    # Se f(x0) for menor que e1, então x0 é uma boa aproximação da raiz.
    if abs(f(x0)) < e1:
        return x0  # Se f(x0) estiver suficientemente perto de zero, retorna x0 como a raiz encontrada.
    
    # Verifica se o valor de x1 já está suficientemente perto de zero ou se a diferença entre x1 e x0 é pequena o suficiente.
    # Isso evita continuar o processo caso já tenhamos uma boa aproximação da raiz.
    if abs(x1) < e1 or abs(x1 - x0) < e2:
        return x1  # Se x1 já for uma boa aproximação (|f(x1)| < e1 ou |x1 - x0| < e2), retorna x1 como a raiz.

    k = 1  # Inicializa o contador de iterações. Isso será usado para monitorar o número de iterações realizadas.

    # Início do loop principal do método da secante, que vai continuar até que a precisão desejada seja alcançada.
    while True:
        # Calcula o novo ponto x2 usando a fórmula da secante:
        # x2 = x1 - f(x1)/(f(x1) - f(x0)) * (x1 - x0)
        # Essa fórmula ajusta x1 com base na inclinação da secante entre (x0, f(x0)) e (x1, f(x1)).
        x2 = x1 - (f(x1) / (f(x1) - f(x0))) * (x1 - x0)

        # Critério de parada 1: Se o valor de f(x2) for menor que e1 (a função está suficientemente próxima de zero),
        # ou se a diferença entre x2 e x1 for menor que e2 (as iterações estão estabilizando).
        if abs(f(x2)) < e1 or abs(x2 - x1) < e2:
            return x2  # Se qualquer critério de parada for atendido, retorna x2 como a raiz encontrada.
        
        # Atualiza os valores de x0 e x1 para as próximas iterações.
        # x0 se torna x1 e x1 se torna x2.
        x0 = x1
        x1 = x2

        # Incrementa o contador de iterações, mostrando o progresso do método.
        k += 1


# Define a função f(x) cuja raiz será buscada usando o método da secante.
def f(x):
    # A função é f(x) = e^(-x^2) - cos(x), uma função que combina a exponencial negativa e o cosseno.
    return math.e**(-x**2) - math.cos(x)  # Retorna o valor de f(x).

# Define as precisões desejadas:
e1, e2 = 1e-6, 1e-6  # Define as precisões e1 (para a função) e e2 (para a diferença entre iterações consecutivas).

# Chutes iniciais para as raízes, ou seja, os valores de x0 e x1.
x0 = 1.2  # Chute inicial x0 = 1.2, uma estimativa inicial da raiz.
x1 = 2.2  # Chute inicial x1 = 2.2, outra estimativa para começar o processo.

# Chama a função secante para encontrar a raiz da função f(x) com os chutes iniciais e as precisões especificadas.
print(secante(x0, x1, e1, e2))  # Imprime a raiz encontrada pelo método da secante.

"""
Comentários gerais sobre o código:
===================================
1. **Funcionamento do método da secante:**
   - O método da secante é um método iterativo para encontrar raízes de uma função, que é similar ao método de Newton-Raphson, mas não requer o cálculo da derivada.
   - O método utiliza dois chutes iniciais, x0 e x1, e gera novas aproximações x2 usando a fórmula da secante.

2. **Critérios de parada:**
   - O loop principal do método para quando:
     a) |f(x2)| < e1: a função está suficientemente próxima de zero, indicando que x2 é uma boa aproximação da raiz.
     b) |x2 - x1| < e2: a diferença entre as iterações consecutivas é muito pequena, indicando que o processo convergiu.

3. **Convergência do método:**
   - O método da secante geralmente converge rapidamente se os chutes iniciais estão próximos da raiz, mas pode falhar se os chutes iniciais estiverem muito distantes ou se a função tiver comportamento irregular.

4. **Exemplo da função f(x):**
   - A função f(x) = e^(-x^2) - cos(x) tem raízes onde o valor da função é igual a zero.
   - O método da secante será usado para encontrar essas raízes em torno dos chutes iniciais x0 = 1.2 e x1 = 2.2.

5. **Cuidados:**
   - A convergência do método depende da escolha dos chutes iniciais. Se os chutes estiverem muito distantes ou se a função tiver múltiplas raízes, o método pode não convergir ou convergir para a raiz errada.
   - É importante garantir que os valores de f(x0) e f(x1) não sejam ambos muito próximos de zero antes de iniciar o processo, pois isso pode levar a erros numéricos.

"""
