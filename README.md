# Random Walk Simulation

A Python simulation of particles moving by random walks in a 1D setting.

## Method
- Start with n = 1000 particles at position 0
- Then using a predetermined number of steps, we then simulate for each particle where it will end up after that many steps.
- Random walk method uses probability p = 0.5 chance to either move in a positive direction (+1) or a negative direction (-1)
- With the calculated end position of each particle, we can then plot the amount of particles in each position using `plot_end_positions()`
