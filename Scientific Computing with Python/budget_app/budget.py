'''
This is original code completing the "Budget App" challenge
project found at:
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app

The full project solution with unit tests are at:
https://replit.com/@samuelshoun/boilerplate-budget-app-FCCfork
'''


import numpy as np


class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amt, desc=''):
        self.ledger.append({'amount': amt, 'description': desc})


    def withdraw(self, amt, desc=''):
        if self.check_funds(amt):
            self.ledger.append({'amount': -amt, 'description': desc})
            return True
        else:
            return False


    def get_balance(self):
        bal = float()

        for i in self.ledger:
            x = i.get('amount')
            bal = bal + x

        return bal


    def check_funds(self, amt):
        return self.get_balance() >= amt


    def transfer(self, amt, category, desc=''):
        if self.check_funds(amt):
            cat = category.name
            self.ledger.append({'amount': -amt, 'description': 'Transfer to {}'.format(cat)})
            category.ledger.append({'amount': amt, 'description': 'Transfer from {}'.format(self.name)})
            return True
        else:
            return False


    def __str__(self):

        lines = []

        name_len = len(self.name)
        stars = 30 - name_len
        top_line = ''.join(['*' * int(np.floor(stars/2)), self.name, '*' * int(np.ceil(stars/2))])
        lines.append(top_line)

        total = 0
        for i in self.ledger:

            amt_str = str('%.2f' % i['amount'])[-7:]
            amt_len = len(amt_str)

            desc_len = len(i['description'][0:23])
            space_ct = 30 - amt_len - desc_len

            total = total + i['amount']

            item_line = i['description'][0:23] + ' ' * space_ct + amt_str
            lines.append(item_line)

        total_line = 'Total: ' + '%.2f' % total
        lines.append(total_line)
        return '\n'.join(lines)



def create_spend_chart(categories):

    cats = categories

    lmax = 0
    total_spend = 0
    props = {}

    for cat in cats:
        for item in cat.ledger:
            if item['amount'] < 0:
                total_spend = total_spend + item['amount']

        if lmax < len(cat.name):
            lmax = len(cat.name)

    for cat in cats:
        subt = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                subt = subt + item['amount']
        prop = int(np.floor((subt / total_spend) * 10) * 10)
        props[cat.name] = prop

    str_len = 12 + lmax


    line1 = '1' + ' ' * (str_len - 1)
    line2 = '0987654321' + ' ' * (lmax + 2)
    line3 = '00000000000' + ' ' * (lmax + 1)
    line4 = '|||||||||||' + ' ' * (lmax + 1)
    line5 = '           -' + ' ' * (lmax)

    lines = [line1, line2, line3, line4, line5]

    for cat in cats:
        barh = int(props.get(cat.name) / 10)
        lines.append(' ' * (10 - barh) + 'o' * (barh + 1) + '-' + cat.name + ' ' * (lmax - len(cat.name)))
        lines.append(' ' * 11 + '-' + ' ' * lmax)
        lines.append(' ' * 11 + '-' + ' ' * lmax)


    prt_line = ['Percentage spent by category', '\n']


    for i in range(str_len):
        for line in lines:
            prt_line.append(line[i])
        if i < str_len - 1:
            prt_line.append('\n')


    return ''.join(prt_line)


print(create_spend_chart([food, business, entertainment]))
