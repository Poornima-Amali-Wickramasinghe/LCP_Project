import numpy as np
from numba import njit

## function that searches for a pattern of organisms    
    
#@njit("i8(i1[:,:], i1[:,:], boolean)")                         # Used to speed up the runs
@njit
def search(world, org, periodic=True):                         # The function takes the matrix of the world, all different shapes of an organism and the border condition (whether it is periodic (open) or closed )
    count = 0                                                  # Number of the organisms
    n, m = org.shape                                           # Size of the matrix of organisms
    
    if periodic:                                               # Open Border 
        world_temp = np.vstack((world, world[:n-1, :]))        # Make an extra column since the border is open !
        worldp = np.hstack((world_temp, world_temp[:, :m-1]))  # Make an extra row on the modified world (with extra column) since the border is open !
        
    else:                                                      # Close Border
        worldp = world                                         # The same matrix will do the tick
    
    for i in range(worldp.shape[0] - n + 1):                   # Iterate through all the rows , Not hitting the corners !!
        for j in range(worldp.shape[1] - m + 1):               # Iterate through all columns ,  Not hitting the corners !!
            
            view = worldp[i:i+n, j:j+m]                        # Make same size auxilary matrixes as the organism's shapes
            
            if (view == org).all():                            # The Matching Condition for the auxilary matrixes we defined and the matrixes for the shapes
                count += 1                                     # Count
                
    return count                                               # Return the Number of shapes found in the world 
    
def show_world(world):                                                 # introducing the function "show_world"
    plt.figure(figsize=(16, 16))                                       # create figure
    plt.pcolormesh(world[::-1, :], cmap='gray')                        # Create a pseudocolor plot with a non-regular rectangular grid
    ax = plt.gca()                                                     # Get the current Axes
    ax.tick_params(left = False, right = False , labelleft = False ,
                    labelbottom = False, bottom = False)               # Remove the ticks
    ax.set_aspect('equal')                                             # Set an equal aspect ratio 
    

                                                    

## Function to use the rules of our world (game) in order to obtain the next generation phase of the world using world's currunt phase 
@njit("i1[:, :](i1[:, :], boolean)", nogil=True)
def next_gen(world, periodic):                                                                      # The function takes the matrix of the world and the border condition 
    N = len(world)                                                                                  # Size of the world
    new_world = np.zeros((N, N), np.int8)                                                           # Make a new world filled with zeros
    if periodic:                                                                                    # Open border 
        world_temp = np.vstack((world[-1:] ,world, world[:1]))                                      # Here we are trying to make neighbors for the corners of the world by adding proper number of rows and columns for "Open border" situation
        worldp = np.hstack((world_temp[:, -1:], world_temp, world_temp[:, :1]))
        
    else:                                                                                           # Closed Border
        world_temp = np.vstack((np.zeros((1, N), np.int8) ,world, np.zeros((1, N), np.int8)))       # Here we are trying to make neighbors for the corners of the world by adding proper number of rows and columns for "Open border" situation
        worldp = np.hstack((np.zeros((N+2, 1), np.int8), world_temp, np.zeros((N+2, 1), np.int8)))
        
    for i in range(1, N+1):                                                                         # Iterate through all the rows
        for j in range(1, N+1):                                                                     # Iterate through all columns

            cell = worldp[i][j]                                                                     # The Cell
            neighbours_count = worldp[i-1:i+2, j-1:j+2].sum() - cell                                # Counting the 8 neighbors

            if cell:                                                                                # An alive cell
                if neighbours_count in (2, 3):                                                      # With 2 or 3 alive neighbors
                    new_world[i-1][j-1] = 1                                                         # Remains alive

            elif (not cell) and neighbours_count == 3:                                              # A dead cell with exactly 3 alive neighbors                     
                new_world[i-1][j-1] = 1                                                             # Gets to be born
    
    return new_world                                                                                # The Next Generation
