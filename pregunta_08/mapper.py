#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        result = line.split()
                
        sys.stdout.write("{}\t{}\n".format(result[0], result[2]))
