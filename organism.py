import numpy as np

## Function that takes the name of organism, an array without padding, number of rotations possible for each shape and possible flips
def add_org(title, org, rot=1, flip=False):
    global Organisms
    org = np.pad(org, 1)                # Add a number of zeros around the matrix of the shape of the organism (in a sence making neighbors in order not to count other organisms) 
    padd_org = [org.astype(np.int8)]    # Convert them to int8 for sake of @njit 
    
    for i in range(rot-1):              # For number of 90 degrees rotations an organism might has (-1 so it does not count the organism itelf twice)
        org = np.rot90(org)             # Rotate 90 degrees
        padd_org.append(org)            # Add to the list of shapes
    
    if flip:                            # For number of flips (over the horizontal or vertical symmetry)  an organism might has
        org = np.flip(org, axis=0)      # Make the Flip
        padd_org.append(org)            # Make the padding like before
        for i in range(rot-1):          # For number of 90 degrees rotations the flipped organism might has
            org = np.rot90(org)         # Make the rotation
            padd_org.append(org)        # Add to the list of shapes
            
    Organisms |= {title: padd_org}      # Add all the shapes to the main dictionary

## Now we make the dictionary of the organisms using the function "add_org"  
Organisms = {}

add_org( "Block" , np.array( [ [1, 1] , [1, 1] ] ) , rot = 1 )

add_org( "Bee Hive" , np.array( [ [0,1,1,0] , [1,0,0,1] , [0,1,1,0] ] ) , rot = 2 )

add_org( "Loaf" , np.array( [ [0,1,1,0] , [1,0,0,1] , [0,1,0,1] , [0,0,1,0] , ] ) , rot = 4 )

add_org( "Boat" , np.array( [ [1,1,0] , [1,0,1] , [0,1,0] ] ) , 4 )

add_org( "Ship" , np.array( [ [1,1,0] , [1,0,1] , [0,1,1] ] ) , 2 )

add_org( "Tub" , np.array( [ [0,1,0] , [1,0,1] , [0,1,0] ] ) , 1 )

add_org( "Pond" , np.array( [ [0,1,1,0] , [1,0,0,1] , [1,0,0,1] , [0,1,1,0] ] ), 1 )

#add_org( "Long Boat" , np.array( [ [0,0,1,0] , [0,1,0,1] , [1,0,1,0] , [1,1,0,0] ] ) , 4 )

#add_org( "Ship Tie" , np.array( [ [0,0,0,0,1,1] , [0,0,0,1,0,1] , [0,0,0,1,1,0] , [0,1,1,0,0,0] , [1,0,1,0,0,0] , [1,1,0,0,0,0] ] ) , 2 )

#add_org( "Barge" , np.array( [ [0,0,1,0] , [0,1,0,1] , [1,0,1,0] , [0,1,0,0] ] ) , 2 )

add_org( "Blinker" , np.array( [ [0,0,0] , [1,1,1] , [0,0,0] ] ) , 2 )

add_org( "Eater", np.array( [ [1,1,0,0] , [1,0,1,0] , [0,0,1,0] , [0,0,1,1] ] ) , 4 , 1 )

add_org( "Hat" , np.array( [ [0,0,1,0,0] , [0,1,0,1,0] , [0,1,0,1,0] , [1,1,0,1,1] ] ) , 4 )

add_org( "Integral" , np.array( [ [0,0,0,1,1] , [0,0,1,0,1] , [0,0,1,0,0] , [1,0,1,0,0] , [1,1,0,0,0] ] ) , 2)

add_org( "Boat Tie" , np.array( [ [0,1,0,0,0,0] , [1,0,1,0,0,0] , [0,1,1,0,0,0] , [0,0,0,1,1,0] , [0,0,0,1,0,1] , [0,0,0,0,1,0] ] ) , 2)

add_org( "Loop" , np.array( [ [0,1,1,0,0] , [1,0,0,1,0] , [0,1,0,1,0] , [1,1,0,1,1] ] ) , 4 , 1 )

add_org( "Elevener" , np.array( [ [0,0,0,0,1,1] , [0,0,0,1,0,1] , [0,0,0,1,0,0] , [0,1,1,1,0,0] , [1,0,0,0,0,0] , [1,1,0,0,0,0] ] ) , 4 )

add_org( "Mirrored Table" , np.array( [ [1,1,0,1,1] , [0,1,0,1,0] , [0,1,0,1,0] , [1,1,0,1,1] ] ) , 2)

add_org( "Sesquihat" , np.array( [ [0,0,0,0,1,0,0] , [1,1,0,1,0,1,0] , [0,1,0,1,0,1,0] , [0,1,0,1,0,1,1] , [0,0,1,0,0,0,0] ] ) , 4 , 1 )

#add_org( "Fourteener" , np.array( [ [0,0,0,0,1,1,0] , [1,1,0,0,1,0,1] , [1,0,0,0,0,0,1] , [0,1,1,1,1,1,0] , [0,0,0,1,0,0,0] ] ) , 4 , 1 )

add_org( "Paperclip" , np.array( [ [0,0,1,1,0] , [0,1,0,0,1] , [0,1,0,1,1] , [1,1,0,1,0] , [1,0,0,1,0] , [0,1,1,0,0] ] ) , 4 , 1 )

add_org( "Moose Antlers" , np.array( [ [1,1,0,0,0,0,0,1,1] , [1,0,0,0,0,0,0,0,1] , [0,1,1,1,0,1,1,1,0] , [0,0,0,1,0,1,0,0,0] , [0,0,0,0,1,0,0,0,0] ] ) , 4 )

add_org( "Mirrored Cap" , np.array( [ [0,1,1,0,1,1,0] , [1,0,1,0,1,0,1] , [1,0,1,0,1,0,1] , [0,1,1,0,1,1,0] ] ) , 2 )

#add_org( "Scorpion" , np.array( [ [0,0,0,1,0,0,0] , [0,1,1,1,0,0,0] , [1,0,0,0,1,1,0] , [1,0,1,0,1,0,1] , [0,1,1,0,1,0,1] , [0,0,0,0,0,1,0] ] ) , 4 , 1 )

#add_org( "Twin Hat" , np.array( [ [0,0,1,0,0,0,1,0,0] , [0,1,0,1,0,1,0,1,0] , [0,1,0,1,0,1,0,1,0] , [1,1,0,1,0,1,0,1,1] , [0,0,0,0,1,0,0,0,0] ] ) , 4 )

#add_org( "Spiral" , np.array( [ [1,1,0,0,0,0,1] , [0,1,0,0,1,1,1] , [0,1,0,1,0,0,0] , [0,0,1,0,1,0,0] , [0,0,0,1,0,1,0] , [1,1,1,0,0,1,0] , [1,0,0,0,0,1,1] ] ) , 1 , 1 )

add_org( "Spark Coil", np.array([ [1,1,0,0,0,1,1], [1,0,1,0,1,0,1], [0,0,1,0,1,0,0], [1,0,1,0,1,0,1], [1,1,0,0,0,1,1] ]), 2 )

add_org( "Toad" , np.array( [ [0,1,1,0] , [1,0,0,0] , [0,0,0,1] , [0,1,1,0] ] ) , 2 , 1 )

add_org( "Toad2" , np.array( [ [1,0] , [1,1] , [1,1] , [0,1] ] ) , 2 , 1 )

Organisms['Toad'] = Organisms['Toad'] + Organisms['Toad2']
del Organisms['Toad2']

add_org( "Beacon" , np.array( [ [1,1,0,0] , [1,1,0,0] , [0,0,1,1] , [0,0,1,1] ] ) , 2 )

add_org( "Beacon2" , np.array( [ [1,1,0,0] , [1,0,0,0] , [0,0,0,1] , [0,0,1,1] ] ) , 2 )

Organisms['Beacon'] = Organisms['Beacon'] + Organisms['Beacon2']
del Organisms['Beacon2']

add_org( "Glider" , np.array( [ [0,1,0] , [0,0,1] , [1,1,1] ] ) , 4 , 1 )

add_org( "Glider2", np.array([ [1,0,1], [0,1,1], [0,1,0] ]), 4,1)

Organisms['Glider'] = Organisms['Glider'] + Organisms['Glider2']
del Organisms['Glider2']

add_org("Catfish", np.array( [ [0,0,1,1,1,0,0,0,1,1,1,0,0] , [0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,1,0,1,0,0,0,0,1] ,
        [1,0,0,0,0,1,0,1,0,0,0,0,1] , [1,0,0,0,0,1,0,1,0,0,0,0,1] , [0,0,1,1,1,0,0,0,1,1,1,0,0] ]) )

add_org("Catfish2",np.array( [ [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,1,0,0,0,0], [0,0,0,0,1,1,0,0,0,1,1,0,0,0,0] ,
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] , [1,1,1,0,0,1,1,0,1,1,0,0,1,1,1], [0,0,1,0,1,0,1,0,1,0,1,0,1,0,0] ,
                              [0,0,0,0,1,1,0,0,0,1,1,0,0,0,0] ] ) )

add_org( "Catfish3", np.array([ [0,0,1,1,0,0,0,0,0,1,1,0,0], [0,0,0,1,1,0,0,0,1,1,0,0,0],[1,0,0,1,0,1,0,1,0,1,0,0,1],
        [1,1,1,0,1,1,0,1,1,0,1,1,1],[0,1,0,1,0,1,0,1,0,1,0,1,0],[0,0,1,1,1,0,0,0,1,1,1,0,0] ] ) )

Organisms['Catfish'] = Organisms['Catfish'] + Organisms['Catfish2'] + Organisms['Catfish3']
del Organisms['Catfish2']
del Organisms['Catfish3']

for k in Organisms:
    Organisms[k] = [org.astype(np.int8) for org in Organisms[k]]
