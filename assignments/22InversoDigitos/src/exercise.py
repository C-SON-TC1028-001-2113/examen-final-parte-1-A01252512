def invDigitos(n):
    inverso = 0
    ultimo = 0

    if n<0:
        negativo = True
        n = n * -1
    while n >= 10:
      ultimo = n%10     #se obtiene el residuo de n/10 (el último dígito del número)
      n = n // 10       #se obtiene la división entera de n / 10 (el resto de los dígitos)
      inverso = inverso * 10 + ultimo   #se multiplica el inverso * 10 para poder añadirle el último dígito
    
    inverso = inverso * 10 + n #cuando n es menor a 10 (o sea de un sólo dígito, se suma por última vez al inverso * 10)
    if negativo:
        inverso = inverso*-1
    return inverso

def main():
    num = int(input("Enter a number: "))
    #escribe tu código abajo de esta línea
    if num >= 1000000:
        print('Too long')
    else:
        print(invDigitos(num))


if __name__=='__main__':
    main()
