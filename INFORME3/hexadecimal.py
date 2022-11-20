def convertirADecimal(cadena_octal):
    cadena_octal=int(cadena_octal)
    decimal = 0
    cont = 1
    while (cadena_octal):
        a = cadena_octal % 10
        cadena_octal = int(cadena_octal / 10)
        decimal += a * cont
        cont*=8
    return str(decimal)

print(convertirADecimal("64"))