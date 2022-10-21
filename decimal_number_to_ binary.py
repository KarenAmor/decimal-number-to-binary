
def convert_decimal_binary(numero):
    binary = []
    while(numero >= 1):
        if numero%2== 0:
            binary.append(0)
            numero//=2
        elif numero%2!=0:
            numero//=2
            binary.append(1)
    return(binary[::-1])


def run():
    numero = int(input('Enter an integer: '))
    binary = convert_decimal_binary(numero)
    print(f'{binary} is the binary number of {numero}')

if __name__ == '__main__':
    run()