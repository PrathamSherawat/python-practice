def value_of_card(card):
    if card == 'A':
        return int(1)
    elif card =='J' or card =='K' or card =='Q':
        return int(10)
    else:
        return int(card)


def higher_card(card_one, card_two):
    c1 = value_of_card(card_one)
    c2 = value_of_card(card_two)
    if c1 > c2:
        return card_one
    elif c1 < c2:
        return card_two
    else:
        return (card_one, card_two)

def value_of_ace(card_one, card_two):
    c1 = value_of_card(card_one)
    c2 = value_of_card(card_two)
    if 1 in [c1, c2]:
        return 1
    else:
        if (21 - (c1+c2))<10:
            return 1
        else: return 11


def is_blackjack(card_one, card_two):
    if card_one=='A' and card_two in ('K', 'J', 'Q', '10'):
        return True
    elif card_two=='A' and card_one in ('K', 'J', 'Q', '10'):
        return True
    else:
        return False



def can_split_pairs(card_one, card_two):
    c1 = value_of_card(card_one)
    c2 = value_of_card(card_two)
    if  c1 ==c2:
        return True
    else:
        return False
    


def can_double_down(card_one, card_two):
    c1 = value_of_card(card_one)
    c2 = value_of_card(card_two)
    if c1 + c2 in (9,10,11):
        return True
    return False
