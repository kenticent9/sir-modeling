import numpy as np
from scipy.integrate import odeint


def get_valid_input():
    N = 500
    R0 = 0
    I0 = 1
    S0 = N - I0 - R0  # Для наочності обчислення S0
    print("""Будь ласка, введіть коефіцієнти контакту та одужання через пробіл 
(наприклад, 0.001 0.1).""")
    userinp = input("> ")
    a, b = [float(i) for i in userinp.split()]
    t = np.linspace(0, 100, 100)
    return N, R0, I0, S0, a, b, t


def system(y, t, N, a, b):
    S, I, R = y
    dSdt = -a*S*I
    dIdt = a*S*I - b*I
    dRdt = b*I
    return dSdt, dIdt, dRdt


def generate_data():
    N, R0, I0, S0, a, b, t = get_valid_input()
    y0 = S0, I0, R0
    data = odeint(system, y0, t, args=(N, a, b))
    S, I, R = data.T
    with open('sir_modeling/data/data.csv', 'w', encoding='UTF-8') as f:
        f.write("Час t,Вразливі,Заражені,Одужали\n")
        for ti in zip(t, S, I, R):
            f.write(f"{','.join(str(d) for d in ti)}\n")


if __name__ == '__main__':
    generate_data()
