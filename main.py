def q1():
    ano = int(input("Primeira dose: "))
    intervalo = int(input("Intervalo: "))

    for i in range(1, 5):
        print(f"{ano + i * intervalo} ", end="")

    pass

def q2():
    def primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    while True:
        num = int(input("Número: "))
        if num == -1:
            break
        if primo(num):
            print("Primo")
        else:
            print("Não")

    pass

def q3():
    soma = 0
    doador = 0

    while True:
        doacao = float(input("valor da doação: "))
        if doacao < 0:
            break
        soma += doacao
        doador += 1

    if doador == 0:
        print("0.00")
        print("0.00")
    else:
        media = soma / doador
        print(f"{soma:.2f}")
        print(f"{media:.2f}")

        


    pass

def q4():
    dias = int(input("Quantidade de dias: "))
    km = float(input("Km total rodada: "))

    cota = dias * 100
    excedente = max(0, km - cota)
    valor = dias * 90 + excedente * 12

    print(f"{valor:.2f}")

    pass

def q5():
    escala = input("Digite a escala: ").upper()
    temp = float(input("temperatura: "))

    if escala == 'C':
        f = temp * 9/5 + 32
        k = temp + 273.15
        print(f"{f:.2f} F")
        print(f"{k:.2f} K")
    elif escala == 'F':
        c = (temp - 32) * 5/9
        k = c + 273.15
        print(f"{c:.2f} C")
        print(f"{k:.2f} K")
    elif escala == 'K':
        if temp < 0:
            print("Valor de temperatura abaixo do minimo")
        else:
            c = temp - 273.15
            f = c * 9/5 + 32
            print(f"{c:.2f} C")
            print(f"{f:.2f} F")
    else:
        print("Escala inválida")

    pass

if __name__ == "__main__":
    q1()
