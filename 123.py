import re

# Словарь с атомными массами элементов
atomic_masses = {
    'H': 1.008,
    'He': 4.0026,
    'Li': 6.94,
    'Be': 9.0122,
    'B': 10.81,
    'C': 12.011,
    'N': 14.007,
    'O': 15.999,
    'F': 18.998,
    'Ne': 20.180,
    'Na': 22.990,
    'Mg': 24.305,
    'Al': 26.982,
    'Si': 28.085,
    'P': 30.974,
    'S': 32.06,
    'Cl': 35.45,
    'Ar': 39.948,
    'K': 39.098,
    'Ca': 40.078,
    'Sc': 44.956,
    'Ti': 47.867,
    'V': 50.941,
    'Cr': 51.996,
    'Mn': 54.938,
    'Fe': 55.845,
    'Co': 58.933,
    'Ni': 58.693,
    'Cu': 63.546,
    'Zn': 65.38,
    'Ga': 69.723,
    'Ge': 72.630,
    'As': 74.922,
    'Se': 78.971,
    'Br': 79.904,
    'Kr': 83.798,
    'Rb': 85.468,
    'Sr': 87.62,
    'Y': 88.906,
    'Zr': 91.224,
    'Nb': 92.906,
    'Mo': 95.95,
    'Tc': 98,
    'Ru': 101.07,
    'Rh': 102.905,
    'Pd': 106.42,
    'Ag': 107.868,
    'Cd': 112.414,
    'In': 114.818,
    'Sn': 118.710,
    'Sb': 121.760,
    'Te': 127.60,
    'I': 126.904,
    'Xe': 131.293,
    'Cs': 132.905,
    'Ba': 137.327,
    'La': 138.904,
    'Ce': 140.116,
    'Pr': 140.907,
    'Nd': 144.242,
    'Pm': 145,
    'Sm': 150.36,
    'Eu': 151.964,
    'Gd': 157.25,
    'Tb': 158.925,
    'Dy': 162.500,
    'Ho': 164.930,
    'Er': 167.259,
    'Tm': 168.934,
    'Yb': 173.04,
    'Lu': 174.966,
    'Hf': 178.49,
    'Ta': 180.947,
    'W': 183.84,
    'Re': 186.207,
    'Os': 190.23,
    'Ir': 192.217,
    'Pt': 195.084,
    'Au': 196.967,
    'Hg': 200.592,
    'Tl': 204.38,
    'Pb': 207.2,
    'Bi': 208.980,
    'Po': 209,
    'At': 210,
    'Rn': 222,
    'Fr': 223,
    'Ra': 226,
    'Ac': 227,
    'Th': 232.038,
    'Pa': 231.035,
    'U': 238.028,
    'Np': 237,
    'Pu': 244,
    'Am': 243,
    'Cm': 247,
    'Bk': 247,
    'Cf': 251,
    'Es': 252,
    'Fm': 257,
    'Md': 258,
    'No': 259,
    'Lr': 262,
    'Rf': 267,
    'Db': 270,
    'Sg': 271,
    'Bh': 270,
    'Hs': 277,
    'Mt': 276,
    'Ds': 281,
    'Rg': 282,
    'Cn': 285,
    'Nh': 286
}
    # Добавьте другие элементы по мере необходимости


def calculate_molar_mass(formula):
    # Регулярное выражение для разбора формулы
    pattern = r'([A-Z][a-z]?)(\d*)'
    total_mass = 0.0

    for element, count in re.findall(pattern, formula):
        count = int(count) if count else 1  # Если количество не указано, то 1
        if element in atomic_masses:
            total_mass += atomic_masses[element] * count
        else:
            raise ValueError(f"Элемент {element} не найден в таблице.")

    return total_mass

# Пример использования
if __name__ == "__main__":
    formula = input("Введите химическую формулу: ")
    try:
        molar_mass = calculate_molar_mass(formula)
        print(f"Молярная масса {formula} составляет {molar_mass:.2f} г/моль.")
    except ValueError as e:
        print(e)