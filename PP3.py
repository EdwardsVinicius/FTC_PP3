
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

def resultadoMod():
    i = 1
    while fita_2[i] != '\0':
        print(fita_2[i], end = '')
        i+=1

def q0():
    global cabecote_1
    global cabecote_2

    if fita_1[cabecote_1] == 'I' and fita_2[cabecote_2] == '\0':
        cabecote_1 += 1
            
        fita_2.insert(-1, 'I')
        cabecote_2 += 1
        q1()
        return

    return



def q1():
    global cabecote_1
    global cabecote_2

    if fita_1[cabecote_1] == 'I' and fita_2[cabecote_2] == '\0':
        cabecote_1 += 1

        fita_2.insert(-1, 'I')
        cabecote_2 += 1
        q1()
        return


    elif fita_1[cabecote_1] == '#' and fita_2[cabecote_2] == '\0':
        cabecote_1 += 1

        cabecote_2 -= 1
        q2()
        return

    return

            
                

def q2():
    global cabecote_1
    global cabecote_2

    if fita_1[cabecote_1] == 'I' and fita_2[cabecote_2] == 'I':
        cabecote_1 += 1

        fita_2[cabecote_2] = '\0'
        cabecote_2 -= 1
        q3()
        return

    return


def q3():
    global cabecote_1
    global cabecote_2

    if fita_1[cabecote_1] == 'I' and fita_2[cabecote_2] == 'I':
        cabecote_1 += 1

        fita_2[cabecote_2] = '\0'
        cabecote_2 -= 1
        q3()
        return


    elif fita_1[cabecote_1] == '\0' and fita_2[cabecote_2] == 'I':
        cabecote_1 -= 1
        q4()
        return


    elif fita_1[cabecote_1] == 'I' and fita_2[cabecote_2] == '\0':
        cabecote_1 -= 1

        fita_2[cabecote_2] = 'I'
        cabecote_2 += 1
        q5()
        return


    elif fita_1[cabecote_1] == '\0' and fita_2[cabecote_2] == '\0':
        cabecote_1 -= 1

        cabecote_2 -= 1
        q7()
        return

    return



def q4():
    global cabecote_1
    global cabecote_2

    if fita_1[cabecote_1] == 'I' and fita_2[cabecote_2] == 'I':
        cabecote_1 -= 1
        q4()
        return


    elif fita_1[cabecote_1] == '#' and fita_2[cabecote_2] == 'I':
        cabecote_1 += 1
        q2()
        return

    return

def q5():
    global cabecote_1
    global cabecote_2
    
    if fita_1[cabecote_1] == 'I' and fita_2[cabecote_2] == '\0':
        cabecote_1 -= 1

        fita_2[cabecote_2] = 'I'
        cabecote_2 += 1
        q5()
        return


    elif fita_1[cabecote_1] == '#' and fita_2[cabecote_2] == '\0':
        cabecote_2 -= 1
        q6()
        return

    return

def q6():
    global cabecote_1
    global cabecote_2

    if fita_1[cabecote_1] == '#' and fita_2[cabecote_2] == 'I':
        #fita_2[cabecote_2] = '\0'
        cabecote_2 += 1
        q8()
        return

    return

def q7():
    global resultado

    resultado = "ACEITA"
    return resultado

def q8():
    global resultado

    resultado = "ACEITA"
    return resultado 

#main
while True:
    try:
        line = input()
    except EOFError:
        break

cabecote_1 = 0
cabecote_2 = 1

resultado = "REJEITA"
    
fita_1 = line
fita_1 = list(fita_1)
fita_1.append('\0')

fita_2 = ['\0', '\0']

q0()

if resultado == "ACEITA":
    print(line, end='=')
    resultadoMod()
    print('', resultado)
else:
    print(line, resultado)