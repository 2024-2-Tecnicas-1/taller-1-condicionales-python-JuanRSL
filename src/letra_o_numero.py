def evaluar(caracter):
    ascii_val = ord(caracter)
    if 65 <= ascii_val <= 90:
        return "Es letra mayúscula"
    elif 97 <= ascii_val <= 122:
        return "Es letra minúscula"
    elif 48 <= ascii_val <= 57:
        return "Es número"
    else:
        return "No es letra ni número"

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
    
    if len(caracter) != 1:
        print("Por favor ingresa un solo carácter.")
    else:
        respuesta = evaluar(caracter)
        print(respuesta)


