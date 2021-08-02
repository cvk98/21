from random import randint

DECK = {
    6: "Шестёрка",
    7: "Семёрка",
    8: "Восьмёрка",
    9: "Девятка",
    10: "Десятка",
    3: "Дама",
    4: "Король",
    2: "Валет",
    11: "Туз"
}
# Колода
values = [[6, 7, 8, 9, 10, 2, 3, 4, 11],
          [6, 7, 8, 9, 10, 2, 3, 4, 11],
          [6, 7, 8, 9, 10, 2, 3, 4, 11],
          [6, 7, 8, 9, 10, 2, 3, 4, 11]]

# Раздача
def distribution(repeat):
    for i in range(repeat):
        c = randint(0, 3)
        s = randint(1, len(values[c])) - 1
        choice = values[c][s]
        del values[c][s]
        return choice


def bank():
    if amount < amountb < 22:
        print('Вы проиграли')
        print('У Банка - ', amountb, '. У Вас - ', amount)
    else:
        print('Поздравляю, вы победили! У вас - ', amount, ', а у Банка - ', amountb)


print("*** Первая раздача карт ***")
dist1 = distribution(1)
dist2 = distribution(1)
dist3 = distribution(1)
amount = dist1 + dist2 + dist3
print("Вам выпало - ", DECK[dist1], "+", DECK[dist2], "+", DECK[dist3], "  |   Сумма равна - ", amount)

answer = 'y'

while answer == 'y':
    if amount == 21:
        print('Вы победили!!!')
        break
    elif amount > 21:
        print('Перебор(((')
        break
    else:
        answer = input("Ещё? (y - да) - ")
        if answer == 'y':
            dist = distribution(1)
            amount += dist
            print('Вам выпало - ', dist)
            print('Сумма равна - ', amount)
        else:
            print("*** Раздача для банка ***")
            distb1 = distribution(1)
            distb2 = distribution(1)
            distb3 = distribution(1)
            amountb = distb1 + distb2 + distb3
            print("Банку выпало - ", DECK[distb1], "+", DECK[distb2], "+", DECK[distb3], "  |   Сумма равна - ",
                  amountb)
            while amountb <= 16:
                distb = distribution(1)
                amountb += distb
                print('Банк добрал ', DECK[distb])
            bank()
