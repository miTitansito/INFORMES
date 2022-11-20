"""El modulo binario debe tener las siguientes funciones:
            convertirADecimal     => recibe string (cadena_binario), retorna string (c)
            convertirAOctal       => recibe string (cadena_binario), retorna string (cadena_octal)
            convertirAHexadecimal => recibe string (cadena_binario), retorna string (cadena_hexadecimal) """
def convertirADecimal(cadena_binario):
    cadena_binario=int(cadena_binario)
    cadena_decimal = 0
    cont = 1
    while cadena_binario>0:
        b=cadena_binario%10
        cadena_binario//=10
        cadena_decimal+= (b)*cont
        cont*=2
        
    return str(cadena_decimal)

letras = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']

def convertirAHexadecimal(cadena_binario):
    decimal = int(cadena_binario, 2)
    b = int(decimal)
    cadena_hexadecimal = format(b,'0x')
    return cadena_hexadecimal

def convertirAOctal(cadena_binario):
    cadena_binario=int(cadena_binario)
    cadena_octal=0
    cont=1
    dec=int(convertirADecimal(cadena_binario))
    while dec!=0:
        cadena_octal+=(dec%8)*cont
        cont*=10
        dec//=8

        
    return(str(cadena_octal))




        
#print(convertirAHexadecimal('89798568985268'))
print(convertirAHexadecimal("10001010111111111111"))
# print(convertirADecimal(10001010111111111111))
print(convertirAOctal("10001010111111111111"))