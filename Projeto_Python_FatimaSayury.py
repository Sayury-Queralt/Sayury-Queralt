import math

#Loop enquanto quiser realizar operações
while True:
    #input da operação
    print("Escolha a operação (opções: * - multiplicar; / - dividir; exp - exponencial; r - raiz quadrada, c - cosseno ; s - seno)")
    op = input("Digite a opção da operação desejada (*, /, exp, , r, c ou s): ")
    #Repetir caso o input seja incorreto
    while op not in ["*", "/", "exp", "r", "c", "s"]:
        print("Operação não identificada")
        print("Digite: * para multiplicar; / para dividir; exp para exponencial; c para cosseno; s para seno)")
        op = input("Digite a opção da operação desejada (*, /, exp, , r, c ou s): ")
    #Operação de Multiplicação
    if op == "*":
        x = int(input("Insira o primeiro valor: "))
        y = int(input("Insira o segundo valor: "))
        result = x*y
        Resultado = f"Resultado: {x} * {y} = {result}"
        print(Resultado)
    #Operação de Divisão
    elif op == "/":
        x = int(input("Insira o primeiro valor: "))
        y = int(input("Insira o segundo valor: "))
        while y == 0:
            print("O divisor não pode ser 0")
            y = int(input("Insira o segundo valor: "))
        result = x/y
        Resultado = Resultado = f"Resultado: {x} / {y} = {result:.4f}"
        print(Resultado)
    #Operação de Exponencial
    elif op == "exp":
        x = int(input("Insira a base: "))
        y = int(input("Insira o expoente: "))
        result = x**y
        Resultado = f"Resultado: {x} exp {y} = {result}"
        print(Resultado)
    #Operação de Raiz quadrada
    elif op == "r":
        x = int(input("Insira o valor: "))
        result = math.sqrt(x)
        Resultado = f"Resultado: raiz quadrada de {x} = {result:.4f}"
        print(Resultado)
    #Operação de Cosseno
    elif op == "c":
        angulo_graus = float(input("Digite o ângulo em graus: "))
        angulo_radianos = math.radians(angulo_graus)
        result = math.cos(angulo_radianos)
        Resultado = f"Resultado: cosseno({angulo_graus}°) = {result:.4f}"
        print(Resultado)
    #Operação de Seno
    else:
        angulo_graus = float(input("Digite o ângulo em graus: "))
        angulo_radianos = math.radians(angulo_graus)
        result = math.sin(angulo_radianos)
        Resultado = f"Resultado: seno({angulo_graus}°) = {result:.4f}"
        print(Resultado)
    continuar = input("Deseja fazer outra operação? (s/n): ")
    #Verificar se deseja realizar outra operação. Repetir até ter uma opção correta. 
    while continuar not in ["s", "n"]:
        print("Erro")
        continuar = input("Deseja fazer outra operação? (Digite s ou n): ")
    #Encerrar while principal/Fim do código.
    if continuar == "n":
        break
print("Obrigada ^^")
print("Execução finalizada!")