saldo_global = 1000
monto = 0
valor_retirar = 0

def consultar_saldo(saldo_global):
    print("Su saldo es: ", saldo_global)
    return saldo_global

def depositar(saldo_global, monto):
    monto = int(input("Ingrese el valor a depositar: "))
    if monto <=  0: 
        print("El valor ingresado debe ser mayor a cero")
    else: 
        saldo_global = saldo_global + monto
        print("Deposito correcto, su nuevo saldo es: ", saldo_global)
        return saldo_global

def retirar(saldo_global, valor_retirar):
    valor_retirar = int(input("Ingrese el valor a retirar: "))
    if valor_retirar <= 0:
            print("Error. cantidad invalida")
    elif valor_retirar > saldo_global:
        print("Saldo insuficiente")
    elif valor_retirar > 0:
        saldo_global = saldo_global - valor_retirar
        print("El retiro fue exitoso, su nuevo saldo es de: ", saldo_global)
        return saldo_global
opcion = str("a")
while opcion != 0:
    print("""------MENÚ------
    a. Consultar saldo
    b. Depositar dinero
    c. Retirar dinero
    d. Salir""")
    opcion = str(input("Seleccione una opción: "))
    if opcion == str("a"):
        saldo_global = consultar_saldo(saldo_global)
        input("Presione enter para continuar")
    elif opcion == str("b"):
        saldo_global = depositar(saldo_global, monto)
        input("Presione enter para continuar")
    elif opcion == str("c"):
        saldo_global = retirar(saldo_global, valor_retirar)
        input("Presione enter para continuar")
    elif opcion == str("d"):
        break
print("Gracias por usar el cajero.")

    


