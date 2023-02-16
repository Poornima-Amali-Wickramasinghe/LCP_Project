import numpy as np

def make_world(custom_world,width=600,height=1100,pixel=10):
    if type(custom_world) == str:
        fig = {'black': np.zeros((height//pixel, width//pixel), np.int8),
               'default': np.random.randint(0, 2, (height//pixel, width//pixel), np.int8),
               'block':np.array([[0,0,0,0,0],[0,0,1,0,0],[0,1,0,1,0],[0,1,0,1,0],[0,0,1,0,0],[0,0,0,0,0]]),
               'glider': np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,1,1,1,0],[0,0,0,0,0]]),
               'gospergun': np.array([ [0,0,0,0,0,0,0],
                                       [0,1,1,1,0,1,0],
                                       [0,1,0,0,0,0,0],
                                       [0,0,0,0,1,1,0],
                                       [0,0,1,1,0,1,0],
                                       [0,1,0,1,0,1,0],
                                       [0,0,0,0,0,0,0],]),
               'replicator': np.array([ [0,0,0,0,0,0,0],
                                        [0,0,0,1,1,1,0],
                                        [0,0,1,0,0,1,0],
                                        [0,1,0,0,0,1,0],
                                        [0,1,0,0,1,0,0],
                                        [0,1,1,1,0,0,0],
                                        [0,0,0,0,0,0,0],]),
              }
        if custom_world == 'option':
            print('World option:')
            for key in fig:
                print(key)
            return
        fig = fig[custom_world]

    else:
        fig = np.array([custom_world])
    return fig
