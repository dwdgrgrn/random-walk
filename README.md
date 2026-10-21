# Random Walk Simulation

A Python simulation of particles moving by random walks in a 1D setting.

## Method
- Start with n = 1000 particles at position 0.
- Then using a predetermined number of steps, we then simulate for each particle where it will end up after that many steps.
- Random walk method uses probability p = 0.5 chance to either move in a positive direction (+1) or a negative direction (-1).
- With the calculated end position of each particle, we can then plot the number of particles in each position using `plot_end_positions()`.
- Viewing this plot, we can see a normal distribution pattern form. This becomes increasingly more evident with higher number of particles.
- The final position is a sum of independent steps, so the central limit theorem applies.
- We can also plot this directly alongside the normal distribution using the function `plot_comparison()`.

## The Mean Squared Displacement
- By calculating the MSD of the position of the particles, we can attempt to see a pattern for each step the particles take.
- Using the function `plot_msd()`, we can observe a linear positive correlation, along with its fitted line, between the step number and the mean squared displacement.
- For large n, we observe near perfect linear correlation, while small n show quite scattered results.
- This shows that the particles are diffusing and that each step is independent of the one before.
