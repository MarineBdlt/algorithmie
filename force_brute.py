import timeit

ACTIONS = {
    "Action-1": [20, 5],
    "Action-12": [30, 10],
    "Action-3": [50, 15],
    "Action-4": [70, 20],
    "Action-5": [60, 17],
    "Action-6": [80, 25],
    "Action-7": [22, 7],
    "Action-8": [26, 11],
    "Action-9": [48, 13],
    "Action-10": [34, 27],
    "Action-11": [42, 17],
    "Action-12": [110, 9],
    "Action-13": [38, 23],
    "Action-14": [14, 1],
    "Action-15": [18, 3],
    "Action-16": [8, 8],
    "Action-17": [4, 12],
    "Action-18": [10, 14],
    "Action-19": [24, 21],
    "Action-20": [114, 18],
}


def tableau_gain(ACTIONS):
    """Compte les gains par actions
    Retourne un dict avec le nom de chaque action contenant son prix et son gain brut au bout de 2 ans
    """

    tableau_gain = {action: [0] * 2 for action in ACTIONS.keys()}

    for action_name, value in ACTIONS.items():
        tableau_gain[action_name][0] = value[0]
        tableau_gain[action_name][1] = value[1] * value[0] / 100
    return tableau_gain


tableau_actions = tableau_gain(ACTIONS)


def table_elements(tableau_actions):
    """Création d'une liste de tuples"""
    elements = []
    for name, val in tableau_actions.items():
        elements.append((name, val[0], val[1]))
    return elements


elements = table_elements(tableau_actions)
money = 500


def algo_force_brute_recursif(money, elems, elements_selection=[], nb_calls=0):
    """Teste toutes les combinaisons et renvoie le meilleur package d'actions"""
    if elems:
        val1, lst_val1 = algo_force_brute_recursif(money, elems[1:], elements_selection)
        val = elems[0]

        if val[1] <= money:
            val2, lst_val2 = algo_force_brute_recursif(
                money - val[1],
                elems[1:],
                elements_selection + [val],
            )
            if val1 < val2:
                return val2, lst_val2
        return val1, lst_val1

    else:
        return sum([i[2] for i in elements_selection]), elements_selection


# complexité = 0(n3)
# algo_force_brute(money, elements)

import itertools


def algo_force_brute(money, elems):
    """algorythme qui teste toutes les combinaisons et print la plus rentable"""
    all_combinations = [
        u for i in range(len(elems)) for u in itertools.combinations(elems, i)
    ]  # retourne toutes les combinaisons possibles

    all_legal_combinations = [
        comb for comb in all_combinations if sum([u[1] for u in comb]) < money
    ]  # retourne toutes les combinaisons possibles dans le budget

    combinaison_money = max(
        all_legal_combinations, key=lambda x: sum(u[2] for u in x)
    )  # retourne la combinaison la plus rentable

    money = sum(
        u[2] for u in combinaison_money
    )  # calcule le bénéfice de ladite combinaison

    return money, combinaison_money


print(algo_force_brute(500, elements))

brute_time_1 = timeit.timeit(
    "algo_force_brute_recursif(money, elements)", globals=globals(), number=1
)

print(brute_time_1)
brute_time_2 = timeit.timeit(
    "algo_force_brute(money, elements)", globals=globals(), number=1
)
print(brute_time_2)
