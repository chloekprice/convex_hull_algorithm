from time import time
from generate import generate_random_points
from convex_hull import compute_hull
import random
from plotting import plot_points, draw_hull, title, show_plot

if __name__ == '__main__':
    test_values = [10, 100, 1000, 10000, 100000, 500000, 1000000]

    elapsed_times = []

    for value in test_values:
        for i in range(5):
            seed = random.randint(1, 500)
            points = generate_random_points("normal", value, seed)
            plot_points(points)

            start = time()
            hull_points = compute_hull(points)
            end = time()

            elapsed_times.append(round(end - start, 4))

            draw_hull(hull_points)
            title(f'{value} normal points: {round(end - start, 4)} seconds')
            show_plot()