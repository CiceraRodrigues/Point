from model.Point import Point
def main ():
    
    while(true):
        
    x=float(input('Digite o valor de x:'))
    y=float(input('Digite o valor de y:'))
    p1 = Point (x,y)
    print (p1)
    
    x2 = float(input('Digite o valor de x:'))
    y2 = float(input('Digite o valor de y:'))
    p2 = Point (x,y)
    print (p2)
    
    p3 = p1+p2
    print ('o resultado é:',p3)
    
    parar=input('Parar s/n?')
        if(parar=="s"):
            break
    
    if __name__ == '__main__':
        main()
        