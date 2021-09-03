def main():
    #escribe tu código abajo de esta línea
    a = int(input())
    total = 0
    for i in range(a):
        b = float(input())
        total = total + b
    promedio = total / a
    print(promedio) 

if __name__=='__main__':
    main()
