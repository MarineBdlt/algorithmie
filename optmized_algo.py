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

# structuration des données # création de dictionnaires


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


def algo_optimized(money, elems):
    matrice = [
        [0 for x in range(money + 1)] for x in range(len(elems) + 1)
    ]  # creation d'une matrice avec elems * money

    for i in range(1, len(elems) + 1):  # parcourt les elements
        for m in range(1, money + 1):  # parcourt l à 501 (argent)
            if elems[i - 1][1] <= m:
                matrice[i][m] = max(
                    elems[i - 1][2]
                    + matrice[i - 1][
                        m - elems[i - 1][1]
                    ],  # on ajoute le nouvel elem et on prends le max gain entre cette solution et celle optimisée de la ligne d'avant
                    matrice[i - 1][m],
                )
            else:
                matrice[i][m] = matrice[i - 1][m]

    m = money
    n = len(elements)
    elements_selection = []

    while m >= 0 and n >= 0:  # tant qu'il reste de l'argent et des actions
        e = elements[n - 1]  # on select le dernier element
        if (
            matrice[n][m] == matrice[n - 1][m - e[1]] + e[2]
        ):  # si le gain est égal à celui de la matrice d'avant + gain de l'elem alors on le selectionne ?
            elements_selection.append(e)
            m -= e[1]

        n -= 1
    return matrice[-1][-1], elements_selection


print(algo_optimized(500, elements))

O2_times_array = {}


optimized_time = timeit.timeit(
    "algo_optimized(money, elements)", globals=globals(), number=1
)

print(optimized_time)
