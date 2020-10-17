
def imprimeFitas():
    global cabecote_1
    global cabecote_2

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

    print('\n')

def q0():
    global cabecote_1
    global cabecote_2

    if fita_1[cabecote_1] == 'I':

        cabecote_1 += 1
    
        if fita_2[cabecote_2] == '\0':
            
            fita_2.insert(-1, 'I')
            cabecote_2 += 1
            q1()
            return

    return



def q1():
    global cabecote_1
    global cabecote_2


    if fita_1[cabecote_1] == 'I':
        
        cabecote_1 += 1
        q1()

        if fita_2[cabecote_2] == '\0':

            fita_2.insert(-1, 'I')
            cabecote_2 += 1
            q1()
            return


    elif fita_1[cabecote_1] == '#':

        cabecote_1 += 1

        if fita_2[cabecote_2] == '\0':

            cabecote_2 -= 1
            q2()
            return

    return

            
                

def q2():
    global cabecote_1
    global cabecote_2


    if fita_1[cabecote_1] == 'I':
        
        cabecote_1 += 1
        if fita_2[cabecote_2] == 'I':
            fita_2[cabecote_2] = '\0'

            cabecote_2 -= 1
            q3()
            return

    return


def q3():
    global cabecote_1
    global cabecote_2


    if fita_1[cabecote_1] == 'I':
        cabecote_1 += 1

        if fita_2[cabecote_2] == 'I':
            fita_2[cabecote_2] = '\0'

            cabecote_2 -= 1
            q3()
            return


    elif fita_1[cabecote_1] == '\0':
        cabecote_1 -= 1

        if fita_2[cabecote_2] == 'I':
            
            q4()
            return


    elif fita_1[cabecote_1] == 'I':
        cabecote_1 -= 1

        if fita_2[cabecote_2] == '\0':
            fita_2[cabecote_2] = 'I'

            cabecote_2 += 1
            q5()
            return


    if fita_1[cabecote_1] == '\0':
        cabecote_1 -= 1

        if fita_2[cabecote_2] == '\0':
            cabecote_2 -= 1
            q7()
            return

    return



def q4():
    global cabecote_1
    global cabecote_2

    if fita_1[cabecote_1] == 'I':
        cabecote_1 -= 1

        if fita_2[cabecote_2] == 'I':

            q4()
            return


    elif fita_1[cabecote_1] == '#':
        cabecote_1 += 1

        if fita_2[cabecote_2] == 'I':

            q2()
            return

    return

def q5():
    global cabecote_1
    global cabecote_2
    
    if fita_1[cabecote_1] == 'I':
        cabecote_1 -= 1

        if fita_2[cabecote_2] == '\0':
            fita_2[cabecote_2] = 'I'

            cabecote_2 =+ 1
            q5()
            return


    elif fita_1[cabecote_1] == '#':

        if fita_2[cabecote_2] == '\0':
            cabecote_2 += 1

            q6()
            return

    return

def q6():
    global cabecote_1
    global cabecote_2

    if fita_1[cabecote_1] == '#':

        if fita_2[cabecote_2] == 'I':
            fita_2[cabecote_2] = '\0'
            cabecote_2 += 1

            q8()
            return

    return

def q7():
    global resultado

    resultado = 'ACEITA'
    return resultado

def q8():
    global resultado

    resultado = 'ACEITA'
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

    resultado = "REJEITA"
    
    fita_1 = i
    fita_1 = list(fita_1)
    fita_1.append('\0')

    fita_2 = ['\0', '\0']

    q0()

    print(i, resultado)