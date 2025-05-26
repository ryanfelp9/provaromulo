def q1():
    ano = int(input("Primeira dose: "))
    intervalo = int(input("Intervalo: "))

    for i in range(1, 5):
        print(f" {ano + i * intervalo}", end="")

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
            print("É primo")
        else:
            print("Não é")

    pass

def q3():
   total = 0
quantidade = 0

while True:
    valor = float(int(input("Valor da doação: ")))
    if valor < 0:
        break
    total += valor
    quantidade += 1

if quantidade > 0:
    media = total / quantidade
    print(f"{total:.2f}")
    print(f"{media:.2f}")
else:
    print("Nenhuma doação realizada.")

    pass

def q4():
    dias = int(input("Quantidade de dias: "))
    km = float(input("Quilometragem total rodada: "))

    cota = dias * 100
    excedente = max(0, km - cota)
    valor = dias * 90 + excedente * 12

    print(f"Valor total a pagar: R$ {valor:.2f}")

    
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

if __name__=="__main__":
    q1()