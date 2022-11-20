import binario
import decimal
import hexadecimal
import octal




print('---------Conversor Numerico-------')
print("   ")
print("Recuerde que debe ingresar el numero a convertir correctamente, en su forma correcta")
print("   ")
num1=input(print("Escriba el numero que desea convetir\n1.Decimal \n 2.Octal \n 3.Hexadecimal \n 4.Binario"))
num2=input(print("Escriba el numero al que desea convetir\n1.Decimal \n 2.Octal \n 3.Hexadecimal \n 4.Binario"))
if num1==1:
    cadena_decimal=input(str('Ingrese su numero'))
    num2=input(print("Escriba el numero al que desea convetir\n1.Decimal \n 2.Octal \n 3.Hexadecimal \n 4.Binario"))
    if num2==1:
        print(cadena_decimal)
    if num2==2:
        print(convertirABinario(cadena_decimal))
    if num2==3:
        print(convertirAOctal(cadena_decimal))
    if num2==4:
        print(convertirAHexadecimal(cadena_decimal))

