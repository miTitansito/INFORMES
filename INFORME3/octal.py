
""" El modulo Octal debe tener las siguientes funciones:
         convertirABinario     => recibe string (cadena_octal), retorna string (cadena_binario)
         convertirADecimal     => recibe string (cadena_octal), retorna string (cadena_decimal)
         convertirAHexadecimal => recibe string (cadena_octal), retorna string (cadena_hexadecimal)"""


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

def convertirABinario(cadena_octal):
    cadena_octal=int(cadena_octal)
    bin = 0
    b = 0
    cont = 1
    deci=int(convertirADecimal(cadena_octal))
    while deci != 0:
        b = deci % 2
        deci //= 2
        bin += b * cont
        cont *= 10
    return str(bin)

#print(convertirABinario(64))

letras = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']

def convertirAHexadecimal(cadena_octal):
    cadena_octal=int(cadena_octal)
    decc=int(convertirADecimal(cadena_octal))
    print(decc)
    if(decc<=0):
        return ''
    hex = decc%16
    return  str(convertirAHexadecimal(decc//16)+letras[hex])
print(convertirAHexadecimal(1144))