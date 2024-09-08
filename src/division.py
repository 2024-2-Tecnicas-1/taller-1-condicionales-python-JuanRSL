def evaluar(dividendo, divisor):
    if divisor == 0:
        return "Error: División por cero no permitida."

    cociente = dividendo // divisor
    residuo = dividendo % divisor

    if residuo == 0:
        respuesta = "La división es exacta. \n" \
                    "Cociente: " + str(cociente) + " \n" \
                    "Residuo: " + str(residuo)
    else:
        respuesta = "La división no es exacta. \ n" \
                    "Cociente: " + str(cociente) + " \n" \
                    "Residuo: " + str(residuo)
    return respuesta
if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
