import math

def run_quiz():
    score = 0

    print("Bem-vindo ao Quiz de Raciocínio Matemático!")
    print("Responda às perguntas sobre restrições matemáticas complexas.")
    print("---------------------------------------------------")

    # Questão 1: 
    print("\nQuestão 1: Qual a restrição para a operação (a + b) / (c - d)?")
    print("a) c deve ser igual a d")
    print("b) c deve ser diferente de d")
    print("c) a + b deve ser diferente de zero")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'b':
        print("Correto! O denominador (c - d) não pode ser zero.")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'b'.")

    # Questão 2: 
    print("\nQuestão 2: Qual a restrição para a operação ((x * y) - z)**0.5?")
    print("a) (x * y) - z deve ser um número positivo")
    print("b) (x * y) - z deve ser maior ou igual a zero")
    print("c) x * y deve ser maior que z")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'b':
        print("Correto! O radicando ((x * y) - z) não pode ser negativo.")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'b'.")

    # Questão 3:
    print("\nQuestão 3: Qual a restrição para a operação math.log(a**2 - b)?")
    print("a) a**2 - b deve ser maior que zero")
    print("b) a**2 - b deve ser diferente de zero")
    print("c) a**2 deve ser maior que b")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'a':
        print("Correto! O argumento do logaritmo (a**2 - b) deve ser estritamente positivo.")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'a'.")

    # Questão 4: 
    print("\nQuestão 4: Para a operação (m + n) / (p + q), qual a restrição para (p + q)?")
    print("a) p + q deve ser maior que zero")
    print("b) p + q deve ser diferente de zero")
    print("c) p e q devem ser números inteiros")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'b':
        print("Correto! O denominador (p + q) não pode ser zero.")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'b'.")

    # Questão 5: 
    print("\nQuestão 5: Para a operação (u - v)**0.5, qual a restrição para (u - v)?")
    print("a) u - v deve ser maior que zero")
    print("b) u - v deve ser um número par")
    print("c) u - v deve ser maior ou igual a zero")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'c':
        print("Correto! O radicando (u - v) não pode ser negativo.")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'c'.")

    # Questão 6:
    print("\nQuestão 6: Para a operação math.log(r * s), qual a restrição para (r * s)?")
    print("a) r * s deve ser maior que zero")
    print("b) r * s deve ser diferente de zero")
    print("c) r e s devem ser números reais")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'a':
        print("Correto! O argumento do logaritmo (r * s) deve ser estritamente positivo.")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'a'.")

    # Questão 7: 
    print("\nQuestão 7: Para a operação 10 / ( (e + f) - (g * h) ), qual a restrição para o denominador?")
    print("a) (e + f) - (g * h) deve ser maior que zero")
    print("b) (e + f) - (g * h) deve ser diferente de zero")
    print("c) (e + f) - (g * h) deve ser um número inteiro")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'b':
        print("Correto! O denominador não pode ser zero.")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'b'.")

    # Questão 8: 
    print("\nQuestão 8: Para a operação (x**2 - y**2)**0.5, qual a restrição para (x**2 - y**2)?")
    print("a) x**2 - y**2 deve ser maior que zero")
    print("b) x**2 - y**2 deve ser um número par")
    print("c) x**2 - y**2 deve ser maior ou igual a zero")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'c':
        print("Correto! O radicando (x**2 - y**2) não pode ser negativo.")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'c'.")

    # Questão 9: 
    print("\nQuestão 9: Para a operação math.log(abs(k - l) - m), qual a restrição para o argumento do logaritmo?")
    print("a) abs(k - l) - m deve ser maior que zero")
    print("b) abs(k - l) - m deve ser diferente de zero")
    print("c) abs(k - l) - m deve ser um número real")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'a':
        print("Correto! O argumento do logaritmo deve ser estritamente positivo.")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'a'.")

    # Questão 10: 
    print("\nQuestão 10: Para a operação (-27)**(1/3), qual a restrição para a base?")
    print("a) A base deve ser maior que zero")
    print("b) A base deve ser um número positivo")
    print("c) Não há restrição para a base")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'c':
        print("Correto! É sempre possível calcular a raiz cúbica de um número real.")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'c'.")

    print("\n---------------------------------------------------")
    print(f"Quiz finalizado! Você acertou {score} de 10 questões.")

if __name__ == "__main__":
    run_quiz()


