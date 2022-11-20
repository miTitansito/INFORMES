"""El modulo Hexadecimal debe tener las siguientes funciones:
            convertirABinario => recibe string (cadena_hexadecimal), retorna string (cadena_binario)
            convertirADecimal => recibe string (cadena_hexadecimal), retorna string (cadena_decimal)
            convertirAOctal   => recibe string (cadena_hexadecimal), retorna string (cadena_Octal)"""

def convertirADecimal(cadena_hexadecimal):
    cadena_decimal = int(cadena_hexadecimal, 16)
    return cadena_decimal

def convertirABinario(cadena_hexadecimal):
    decimal = int(cadena_hexadecimal, 16)
    a = int(decimal)
    cadena_binario = format(a, '0b')
    return cadena_binario

def convertirAOctal(cadena_hexadecimal):
    decimal= int(cadena_hexadecimal, 16)
    b = int(decimal)
    cadena_Octal = format(b,'0o')
    return cadena_Octal

    