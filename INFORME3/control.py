import decimal
import binario
import hexadecimal
import octal
print('---------Conversor Numerico-------')
print("   ")
print("""Recuerde que debe ingresar el numero a convertir correctamente, en su forma correcta\n 
Las opciones a ingresar correspone a la base de los numeros a trabajar""")
print("   ")



base = ["2", "8", "10", "16"]
numconver = input( """
"Escriba el numero de la opcion que desea convetir
2)Binario
8)Octal
10)Decimal
16)Hexadecimal
""")
if  numconver not in base:
    print("La opcion que ingresaste no es correcta, por favor vuelve a ingresar la opcion")
    numconver = input( """
"Escriba el numero de la opcion que desea convertir
2)Binario
8)Octal
10)Decimal
16)Hexadecimal
""")
else:
    ""
if numconver=="2":
    cadena_binario=input('Ingrese su numero binario')
    num2=input( """
"Escriba el numero de la opcion al que desea convertir su numero
8)Octal
10)Decimal
16)Hexadecimal
""")
    if num2=="10":
        print(binario.convertirADecimal(cadena_binario))
    if num2=="16":
        print(binario.convertirAHexadecimal(cadena_binario))
    if num2=="8":
        print(binario.convertirAOctal(cadena_binario))


elif numconver=="8":
    cadena_octal=input('Ingrese su numero Octal')
    num3=input( """
"Escriba el numero de la opcion al que desea convertir su numero
2)Binario
10)Decimal
16)Hexadecimal
""")
    if num3=="10":
        print(octal.convertirADecimal(cadena_octal))
    if num3=="16":
        print(octal.convertirAHexadecimal(cadena_octal))
    if num3=="2":
        print(octal.convertirABinario(cadena_octal))


