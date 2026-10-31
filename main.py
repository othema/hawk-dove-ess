import matplotlib.pyplot as plt
from src.simulation import Simulation

OUTPUT = "output.png"


def main():
    simulation = Simulation()

    n = 1000

    population_history = []
    for _ in range(n):
        population_history.append(simulation.get_species_total())
        simulation.step()
    
    plt = plot_data(population_history)
    plt.savefig(OUTPUT)

    print("Saved output to " + OUTPUT)


def plot_data(population_history):
    species = list(population_history[0].keys())
    steps = range(len(population_history))

    data = [[h[s] for h in population_history] for s in species]

    plt.figure()
    plt.stackplot(steps, data, labels=species, alpha=0.8)

    plt.xlabel("Generations")
    plt.ylabel("Total Population")
    plt.title("Population Over Time")
    plt.legend(loc="upper left")

    return plt



if __name__ == "__main__":
    main()
