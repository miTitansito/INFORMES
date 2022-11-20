""" El modulo decimal debe tener las siguientes funciones:
            convertirABinario     => recibe string (cadena_decimal), retorna string (cadena_binario)
            convertirAOctal       => recibe string (cadena_decimal), retorna string (cadena_octal)
            convertirAHexadecimal => recibe string (cadena_decimal), retorna string (cadena_hexadecimal)"""
def convertirABinario(cadena_decimal):
    cadena_decimal=int(cadena_decimal)
    cadena_binario=0
    cont=1
    while cadena_decimal!=0:
        cadena_binario=cadena_binario+cadena_decimal%2*cont
        cadena_decimal//=2
        cont*=10
    return str(cadena_binario)

def convertirAOctal(cadena_decimal):
    cadena_decimal=int(cadena_decimal)
    cadena_octal=0
    cont=1
    while cadena_decimal!=0:
        cadena_octal+=(cadena_decimal%8)*cont
        cont*=10
        cadena_decimal//=8

        
    return(str(cadena_octal))



letras = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']

def convertirAHexadecimal(cadena_decimal):
    cadena_decimal=int(cadena_decimal)
    if(cadena_decimal<=0):
        return ''
    hex = cadena_decimal%16
    cadena_hexadecimal=convertirAHexadecimal(cadena_decimal//16)+letras[hex]
    return  str(cadena_hexadecimal)
        
print(convertirAHexadecimal('89798568985268'))
