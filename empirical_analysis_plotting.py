import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def plot_mean():
    # creating the dataset
    data = {'10': 0.0, '100': 0.00102, '1000': 0.00892, '10000': 0.08866, '100000': 0.86912, '500000': 4.681,
            '1000000': 8.9071}
    courses = list(data.keys())
    values = list(data.values())

    # fig = plt.figure(figsize=(10, 5))
    #
    # # creating the bar plot
    # plt.bar(courses, values, color='maroon',
    #         width=0.4)
    #
    # plt.xlabel("n, Value of N")
    # plt.ylabel("t, Mean Computation Time (s)")
    # plt.title("Mean Outcomes")
    # plt.show()

def plot_best_fit():
    xdata = ['10', '100', '1000', '10000', '100000', '500000', '1000000']
    ydata = [0.0, 0.00102, 0.00892, 0.0866, 0.8691, 4.681, 8.9071]
    fit_y = [10, 200, 3000, 40000, 500000, 2849485, 6000000]

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(xdata, fit_y, color='indigo',
            width=0.4)

    plt.xlabel("n, Value of N")
    plt.ylabel("t, Mean Computation Time (s)")
    plt.title("nlog(n) Graph")
    plt.show()

# Define the Gaussian function
def gauss(x, A, B):
    y = A*np.exp(-1*B*x**2)
    return y


if __name__ == '__main__':
    plot_best_fit()
