def evaluar(num_victorias_a, num_victorias_b):
    if (num_victorias_a == 7 and (num_victorias_b == 5 or num_victorias_b == 6)) or \
       (num_victorias_b == 7 and (num_victorias_a == 5 or num_victorias_a == 6)):
        if num_victorias_a > num_victorias_b:
            return "Ganó A"
        else:
            return "Ganó B"
    if num_victorias_a == 6 and num_victorias_b <= 4:
        return "Ganó A"
    if num_victorias_b == 6 and num_victorias_a <= 4:
        return "Ganó B"
    if num_victorias_a <= 6 and num_victorias_b <= 6:
        return "Aún no termina"

    return "Inválido"

if __name__ == '__main__':
    print("Los juegos ganados por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganados por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)

