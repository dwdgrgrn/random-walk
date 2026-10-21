import numpy as np
import matplotlib.pyplot as plt

n = 1000
num_of_steps = 10

particles = [[0 for k in range(num_of_steps)] for k in range(n)]
end_positions = {k:0 for k in range(-num_of_steps, num_of_steps+1)}


rng = np.random.default_rng()

for j in range(n):
    random_steps = rng.choice([-1, 1], size=num_of_steps)
    steps = [0 for k in range(num_of_steps)]
    sum = 0
    for i in range(len(random_steps)):
        sum += random_steps[i]
        steps[i] = sum
    particles[j] = steps
    end_positions[sum] += 1

def plot_end_positions(positions):
    plt.bar(list(positions.keys()), list(positions.values()))
    plt.show()




msd = [0 for k in range(num_of_steps)]

for i in range(num_of_steps):
    x = 0
    for k in range(n):
        x += particles[k][i] ** 2
    msd[i] = x / n


t = np.arange(1, num_of_steps + 1)
gradient, intercept = np.polyfit(t, msd, 1)

def plot_msd(t, msd, gradient, intercept):
    plt.plot(t, msd, "o")
    plt.plot(t, gradient * t + intercept, label="Fitted line")
    plt.xlabel("Time step")
    plt.ylabel("Mean squared displacement")
    plt.legend()
    plt.show()



x = np.linspace(-num_of_steps, num_of_steps, 500)
normal = n * 2 * np.exp(-x**2 / (2 * num_of_steps)) / np.sqrt(2 * np.pi * num_of_steps)


def plot_comparison(positions, x, normal):
    plt.bar(list(positions.keys()), list(positions.values()), label="Simulated")
    plt.plot(x, normal, color="red", label="Normal distribution")
    plt.xlabel("Final position")
    plt.ylabel("Number of particles")
    plt.legend()
    plt.show()


#plot_end_positions(end_positions)
#plot_msd(t, msd, gradient, intercept)
plot_comparison(end_positions, x, normal)