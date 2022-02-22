"""
EDGAR RODRIGUEZ HERNANDEZ

INSTRUCCIONES:
    1-Debe de generar un numero aleatorio de 4 digitos.
    2.Adivinar ese numero ingresando un numero de 4 digitos:
        Si alguno de los digitos coincidie con algun digito del numero aleatorio aun que no este en la posicion correcta imprimir "-";
        o
        Si algun digito del numero ingresado coincide con algun digito del numero aleatorio y ademas coincide con la misma posicion imprimir "*";
"""
import random
#Genera un numero Ramdon de 4 digitos
def generadorN():
    numeroG = list(str(random.randint(1000, 9999)))    
    return numeroG

#Valida que el numero ingresado sea de 4 digitos
def validacion(nIngresa):
    try:
        int(nIngresa)
        if(int(nIngresa)>=1000 and int(nIngresa)<=9999):
            return True
        else:        
            print("¡¡ERROR!! El numero debe ser de 4 digitos")
    except ValueError:
        return False

# Compara ambas listas y en base a la posicion de los numeros imprime "*" o "-"
def encuentra(nAleatorio,nIngresado):
    resultado=["","","",""]
    # print(int(len(nIngresado)))
    for i in range (int(len(nIngresado))):
        # print("nIngresado "+ nIngresado[i])
        # print("nAleatorio "+ nAleatorio[i])
        if (nIngresado[i]==nAleatorio[i]):
            resultado[i]="*"
        elif(nIngresado[i] in nAleatorio):
            resultado[i]="-"
    print(resultado)

def main():
    aleatorio=generadorN()
#Imprime valor generado
    print(aleatorio)
    print("///////// Bienvenido a este programa///////////")
    print('     -Ingresa un numero de 4 digitos')
    print("     -Para salir presiona 'q'")
    Terminar = False
    while not Terminar:
        leer = input("> ")
        if leer.lower() == 'q':
            return
        if(validacion(leer)):
            encuentra(aleatorio, list(leer))
            # print("El numero es correcto")
            # print(list(leer))
            # print(aleatorio)
if __name__=="__main__":
	main()