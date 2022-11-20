import moduloDecimal
import moduloBinario
import moduloHexadecimal
import moduloOctal
print('---------Conversor Numerico-------')
print("   ")
print("""Recuerde que debe ingresar el numero a convertir correctamente, en su forma correcta\n 
Las opciones a ingresar correspone a la base de los numeros a trabajar\n
No se acpetan numeros negativos""")
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
    cadena_binario=input('Ingrese su numero moduloBinario')
    num2=input( """
"Escriba el numero de la opcion al que desea convertir su numero
8)Octal
10)Decimal
16)Hexadecimal
""")
    if num2=="10":
        print(moduloBinario.convertirADecimal(cadena_binario))
    if num2=="16":
        print(moduloBinario.convertirAHexadecimal(cadena_binario))
    if num2=="8":
        print(moduloBinario.convertirAOctal(cadena_binario))


elif numconver=="8":
    cadena_octal=input('Ingrese su numero Octal')
    num3=input( """
"Escriba el numero de la opcion al que desea convertir su numero
2)Binario
10)Decimal
16)Hexadecimal
""")
    if num3=="10":
        print(moduloOctal.convertirADecimal(cadena_octal))
    if num3=="16":
        print(moduloOctal.convertirAHexadecimal(cadena_octal))
    if num3=="2":
        print(moduloOctal.convertirABinario(cadena_octal))

elif numconver=="10":
    cadena_decimal=input('Ingrese su numero decimal')
    num4=input( """
"Escriba el numero de la opcion al que desea convertir su numero
2)Binario
8)Octal
16)Hexadecimal
""")
    if num4=="8":
        print(moduloDecimal.convertirAOctal(cadena_decimal))
    if num4=="16":
        print(moduloDecimal.convertirAHexadecimal(cadena_decimal))
    if num4=="2":
        print(moduloDecimal.convertirABinario(cadena_decimal))

elif numconver=="16":
    cadena_hexadecimal=input('Ingrese su numero decimal')
    num4=input( """
"Escriba el numero de la opcion al que desea convertir su numero
2)Binario
8)Octal
10)Decimal
""")
    if num4=="8":
        print(moduloHexadecimal.convertirAOctal(cadena_hexadecimal))
    if num4=="10":
        print(moduloHexadecimal.convertirADecimal(cadena_hexadecimal))
    if num4=="2":
        print(moduloHexadecimal.convertirABinario(cadena_hexadecimal))
