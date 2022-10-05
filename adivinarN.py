import random
import os

#limpiar consola
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

c = 10
x = random.randint(1,c)

a=[]
clearConsole()
while True:
    try:
        a.append( int (input (f"ingresa un número entre 1 y {c}. Adiviná cual elegí yo \nLa probabilidad de acertar es del {round(1/c*100,2)}%\n")))
        print (x)
        if 1<=a[-1]<=c:
            break
        else:
            a=[]
            clearConsole()
            print("El número que elegiste no cumple con las condiciones")
    except:
        print(f"uhhh! El número debe ser entero y estar entre 1 y {c}")

while True:
    if x == a[-1]:
        print ("Felicitaciones! adivinaste!")
        break
    elif a[-1] % 1 != 0:
        print ("tu numero tiene que ser entero")
    else:
        while True:
            try:
                if a[-1] in a[:-1]:
                    clearConsole()
                    print ("tenes que elegir uno que no hayas usado")
                    a=a[:-1]
                    break
                a_lista= str(a)[1:-1]
                if len(a)==1:
                    a_lista= f"vez con el número {a_lista}"
                else:
                    a_lista= f"veces con los números {a_lista}"
                clearConsole()
                print (f"intentá otra vez!\nYa probaste {len(a)} {a_lista}")
                a.append( int (input (f"ingresa un número entre 1 y {c}. Adiviná cual elegí yo \nLa probabilidad de acertar es del {round(1/(c-len(a))*100,2)}%\n")))
                break
            except:
                print(f"uhhh! El número debe ser entero y estar entre 1 y {c}")