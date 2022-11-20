"""El modulo binario debe tener las siguientes funciones:
            convertirADecimal     => recibe string (cadena_binario), retorna string (cadena_decimal)
            convertirAOctal       => recibe string (cadena_binario), retorna string (cadena_octal)
            convertirAHexadecimal => recibe string (cadena_binario), retorna string (cadena_hexadecimal) """
def convertirADecimal(cadena_binario):
    cadena_binario=int(cadena_binario)
    deci = 0
    cont = 1
    while cadena_binario>0:
        b=cadena_binario%10
        cadena_binario//=10
        deci+= (b)*cont
        cont*=2
        
    return str(deci)


def convertirAOctal(cadena_binario):
    cadena_binario=int(cadena_binario)
    octal=0
    cont=1
    dec=int(convertirADecimal(cadena_binario))
    while dec!=0:
        octal+=(dec%8)*cont
        cont*=10
        dec//=8

        
    return(str(octal))



letras = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']

def convertirAHexadecimal(cadena_binario):
    cadena_binario=int(cadena_binario)
    decc=int(convertirADecimal(cadena_binario))
    if(decc<=0):
        return ''
    hex = decc%16
    return  convertirAHexadecimal(decc//16)+letras[hex]
print(convertirAHexadecimal(1011111))  