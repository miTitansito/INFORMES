import decimal
import binario
import hexadecimal
import octal
print('---------Conversor Numerico-------')
print("   ")
print("Recuerde que debe ingresar el numero a convertir correctamente, en su forma correcta")
print("   ")

num1=input("Escriba el numero que desea convetir\n1.Decimal \n 2.Octal \n 3.Hexadecimal \n 4.Binario")
cadena_decimal=input(str('Ingrese su numero'))
num2=input("Escriba el numero al que desea convetir\n1.Decimal \n 2.Octal \n 3.Hexadecimal \n 4.Binario")
if num1==1:
    if num2==1:
        print("nudfivn",cadena_decimal)
    if num2==2:
        print("2",decimal.convertirABinario(cadena_decimal))
    if num2==3:
        print(decimal.convertirAOctal(cadena_decimal))
    if num2==4:
        print(decimal.convertirAHexadecimal(cadena_decimal))

