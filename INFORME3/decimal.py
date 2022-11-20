""" El modulo decimal debe tener las siguientes funciones:
            convertirABinario     => recibe string (cadena_decimal), retorna string (cadena_binario)
            convertirAOctal       => recibe string (cadena_decimal), retorna string (cadena_octal)
            convertirAHexadecimal => recibe string (cadena_decimal), retorna string (cadena_hexadecimal)"""
def convertirABinario(cadena_decimal):
    cadena_decimal=int(cadena_decimal)
    bin=0
    cont=1
    while cadena_decimal!=0:
        bin=bin+cadena_decimal%2*cont
        cadena_decimal//=2
        cont*=10
    return str(bin)

def convertirAOctal(cadena_decimal):
    cadena_decimal=int(cadena_decimal)
    octal=0
    cont=1
    while cadena_decimal!=0:
        octal+=(cadena_decimal%8)*cont
        cont*=10
        cadena_decimal//=8

        
    return(str(octal))



letras = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']

def convertirAHexadecimal(cadena_decimal):
    cadena_decimal=int(cadena_decimal)
    if(cadena_decimal<=0):
        return ''
    hex = cadena_decimal%16
    return  str(convertirAHexadecimal(cadena_decimal//16)+letras[hex])
        
print(convertirAHexadecimal('78'))