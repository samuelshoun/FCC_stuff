def arithmetic_arranger(problems, showsols=True):

    x = problems

    if len(x) > 5:
        print('Error: Too many problems.')
        return None

    for i in x:
        if i.split()[1] == '+':
            continue
        elif i.split()[1] == '-':
            continue
        else:
            print("Error: Operator must be '+' or '-'.")
            return None

    for i in x:
        if not i.split()[0].isdigit():
            print("Error: Numbers must only contain digits.")
            return None
        elif not i.split()[2].isdigit():
            print("Error: Numbers must only contain digits.")
            return None

        elif len(i.split()[0]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return None
        elif len(i.split()[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return None

    toprow = []
    botrow = []
    uline = []
    sols = []

    for i in x:

        prob = i

        prob_w = 3

        for j in prob.split():
            if len(j) + 2 > prob_w:
                prob_w = len(j) + 2

        topel = i.split()[0]
        op = i.split()[1]
        botel = i.split()[2]

        toprow.append(' ' * (prob_w - len(topel)))
        toprow.append(topel)
        if i != x[-1]:
            toprow.append(' ' * 4)


        botrow.append(op)
        botrow.append(' ' * (prob_w - len(botel) - 1))
        botrow.append(botel)
        if i != x[-1]:
            botrow.append(' ' * 4)

        uline.append('-' * prob_w)
        uline.append(' ' * 4)

        if op == '+':
            sol = int(topel) + int(botel)
        elif op == '-':
            sol = int(topel) - int(botel)
        else:
            print('error')
            break

        sol = str(sol)

        sols.append(' ' * (prob_w - len(sol)))
        sols.append(sol)
        if i != x[-1]:
            sols.append(' ' * 4)

    toprow = ''.join(toprow)
    botrow = ''.join(botrow)
    uline = ''.join(uline)
    sols = ''.join(sols)

    if showsols == True:
        out = '\n'.join([toprow, botrow, uline, sols])
    else:
        out = '\n'.join([toprow, botrow, uline])

    print(out)
