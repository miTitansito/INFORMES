""" El modulo decimal debe tener las siguientes funciones:
            convertirABinario     => recibe string (cadena_decimal), retorna string (cadena_binario)
            convertirAOctal       => recibe string (cadena_decimal), retorna string (cadena_octal)
            convertirAHexadecimal => recibe string (cadena_decimal), retorna string (cadena_hexadecimal)"""
def convertirABinario(cadena_decimal):
    bin=0
    cont=1
    while cadena_decimal!=0:
        bin=bin+cadena_decimal%2*cont
        cadena_decimal//=2
        cont*=10
    return str(bin)

def convertirAOctal(cadena_decimal):
    octal=0
    cont=1
    while cadena_decimal!=0:
        octal+=(cadena_decimal%8)*cont
        cont*=10
        cadena_decimal//=8

        
    return(str(octal))
def convertirAHexadecimal(cadena_decimal):
    hex=0
    cont=1
    while cadena_decimal!=0:
        hex+=(cadena_decimal%)
print(convertirAOctal(33))

print(type(convertirABinario(645)))