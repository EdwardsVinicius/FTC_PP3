
def imprimeFitas():
    global cabecote_1
    global cabecote_2
    global cabecote_3
    global cabecote_4

    print('')
    i = 0
    print("Fita_1: [", end = '')
    while fita_1[i] != '\0':
        if i == cabecote_1:
            print('>', end = '')
        print(fita_1[i], end = '')
        i+=1
    print("]")

    i = 1
    print("Fita_2: [", end = '')
    while fita_2[i] != '\0':
        if i == cabecote_2:
            print('>', end = '')
        print(fita_2[i], end = '')
        i+=1
    print("]")

    i = 1
    print("Fita_3: [", end = '')
    while fita_3[i] != '\0':
        if i == cabecote_3:
            print('>', end = '')
        print(fita_3[i], end = '')
        i+=1
    print("]")

    i = 1
    print("Fita_4: [", end = '')
    while fita_4[i] != '\0':
        if i == cabecote_4:
            print('>', end = '')
        print(fita_4[i], end = '')
        i+=1
    print("]")

    print('\n')

def q0():
    global cabecote_1
    global cabecote_2
    global cabecote_3
    global cabecote_4

    #print('q0')
    if fita_1[cabecote_1] == ' ':
        #imprimeFitas()

        cabecote_1+=1
        q0()

        return
    
    elif fita_1[cabecote_1] == 'a':
        #imprimeFitas()
        
        cabecote_1+=1

        if fita_2[cabecote_2] == '\0':
            fita_2.insert(-1, 'a')
            cabecote_2+=1
            return q0()


    elif fita_1[cabecote_1] == 'b':
        #imprimeFitas()

        cabecote_1+=1

        if fita_3[cabecote_3] == '\0':
            fita_3.insert(-1, 'b')
            cabecote_3+=1
            return q0()


    elif fita_1[cabecote_1] == 'c':
        #imprimeFitas()
        
        cabecote_1+=1

        if fita_4[cabecote_4] == '\0':
            fita_4.insert(-1, 'c')
            cabecote_4+=1
            return q0()
            


    elif fita_1[cabecote_1] == '#':
        #imprimeFitas()
        
        cabecote_1+=1

        if fita_2[cabecote_2] == '\0':
            cabecote_2-=1
            return q1()


def q1():
    global cabecote_1
    global cabecote_2
    global cabecote_3
    global cabecote_4

    #print('q1')
    #imprimeFitas()

    if fita_2[cabecote_2] == 'a':
        if fita_3[cabecote_3] == '\0':
            cabecote_3-=1

            if fita_4[cabecote_4] == '\0':
                cabecote_4-=1

                return q2()
                

def q2():
    global cabecote_1
    global cabecote_2
    global cabecote_3
    global cabecote_4

    #print('q2')
    #imprimeFitas()

    if fita_2[cabecote_2] == 'a':
        fita_2[cabecote_2] = '\0'
        cabecote_2-=1
    
        if fita_3[cabecote_3] == 'b':
            fita_3[cabecote_3] = '\0'
            cabecote_3-=1

            if fita_4[cabecote_4] == 'c':
                fita_4[cabecote_4] = '\0'
                cabecote_4-=1

                return q2()


    elif fita_2[cabecote_2] == '\0':
        if fita_3[cabecote_3] == 'b':
            fita_3[cabecote_3] = '\0'
            cabecote_3-=1

            if fita_4[cabecote_4] == 'c':
                fita_4[cabecote_4] = '\0'
                cabecote_4-=1

                return q3()


def q3():
    global cabecote_1
    global cabecote_2
    global cabecote_3
    global cabecote_4

    #print('q3')
    #imprimeFitas()

    if fita_3[cabecote_3] == 'b':
        fita_3[cabecote_3] = '\0'
        cabecote_3-=1

        if fita_4[cabecote_4] == 'c':
            fita_4[cabecote_4] = '\0'
            cabecote_4-=1

            return q3()


    elif fita_3[cabecote_3] == '\0':
        if fita_4[cabecote_4] == 'c':
            fita_4[cabecote_4] = '\0'
            cabecote_4-=1

            return q4()


def q4():
    global cabecote_1
    global cabecote_2
    global cabecote_3
    global cabecote_4

    #print('q4')
    #imprimeFitas()

    if fita_4[cabecote_4] == 'c':
        fita_4[cabecote_4] = '\0'
        cabecote_4-=1

        return q4()


    elif fita_4[cabecote_4] == '\0':
        return q5()


def q5():
    global cabecote_1
    global cabecote_2
    global cabecote_3
    global cabecote_4
    global resultado

    #print('q5')
    #imprimeFitas()

    resultado = "ACEITA"
    return resultado


#main
lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

for i in lines:
    cabecote_1 = 0
    cabecote_2 = 1
    cabecote_3 = 1
    cabecote_4 = 1

    resultado = "REJEITA"
    
    fita_1 = i
    fita_1 = list(fita_1)
    fita_1.append('\0')

    fita_2 = ['\0', '\0']
    fita_3 = ['\0', '\0']
    fita_4 = ['\0', '\0']

    q0()

    print(i, resultado)