# Tetration

Plots graph of tetration of <sup>x</sup>b against x

Variable intake
 - base b
 - range of x
  
# Tetration_multiple

Same as Tetration but for multiple graphs

Variable intake
 - numpy array of bases 
 - range of x
  
# Jumper

<details>
  <summary>Using the Monte Carlo method, Plots the distribution of a jumper landing on a given position from the left in the following scenaio:</summary>

  - Start with a point, construct 2 lines out of it to form 2 more points on an upper level
  - For the next level repeat the process for both points but such that the new point to the right of the original left point is connected to the left of the original right point
  - Repeat for n levels, where adjacent points conenct to the same point higher up
  - Now place a jumper token at your original point (layer 0)
  - The token jumps n times, each time jumping to a higher level where it has a probability of moving left of p
  - For a modified version, the jumper has an equal probability of jumping left or right on the first jump only
  - The distribution modeled is the probability that the jumper lands on a particular point from the left 
</details>

Variable intake
 - Number of simulations 
 - Number of jumps
 - Probability of moving left when jumping
 - Use modified rules?

# plotDictVlaues

From a dictionary of the form {key:[x,y], ...}, plots all the points x,y
Ignores key entirely
