#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    lista1 = []
    lista2 = []
   
    for line in sys.stdin:
        lista1.append(line)

  
    lista2 = sorted(lista1, key=lambda x: x[2])

    for item in lista2:
        sys.stdout.write("{}".format(item))
