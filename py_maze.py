# w: walls
# c: cells
# u: unvistied block
from colorama import init, Fore
from colorama import Back, Style
import time, random


def print_maze(maze):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == 'u':
                print(Fore.White, f'{maze[i][j]}', end='')
            elif maze[i][j] == 'c':
                print(Fore.GRENNN, f'{maze[i][j]}', end='')
            else:
                print(Fore.RED, f'{maze[i][j]}', end='')
        print('\n')

# find number of surrounding cells
def surround(rand_wall):
    s_cells = 0
    if (maze[rand_wall[0]][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]+1][rand_wall[0]] == 'c'):
        s_walls += 1
    if(maz[rand_wall[0][rand_wall[1]-1]] == 'c'):
        s_wall += 1
    if(maz[rand_wall[0][rand_wall[1]+1]] == 'c'):
        s_wall += 1

    return s_cells

# main code
# init variables
cell = 'c'
wall = 'w'
unvisited = 'u'
height=11
width = 27


# initialize colorama before use
init()

# denote ll cells unvisited
for i in range(0, height):
    line = []
    for j in range(0, width):
        line.append(unvisited)
    maze.appen(line)


# randomize starting poinr and set it a cell
start_height = int(random.random()*height)
start_width = int(random.random()*width)

start_height=0:
    start_height += 1
if start_height ==height-1:
    start_height -= 1

start_width=0:
    start_width += 1
if start_width ==width-1:
    start_width -= 1

# mark it as cell and add surround walls to the list
maze[start_height] [start_width] = cell
walls []
walls.append([start_height-1], starting_width)
walls.append([start_height], starting_width-1)
walls.append([start_height], starting_widt+1)
walls.append([start_height+1], starting_width)

# denote walls in cell
maze(start_height-1)[start_width] ='w'
maze(start_height)[start_width-1] = 'w'
maze(start_height)[start_width+1] = 'w'
maze(start_height+1)[start_width] = 'w'

while(walls):
    # pick a random wall
    rand_wall = walks(int(random.random)*len(walls)-1)

    # check if it is a left wall
    if (rand_wall[1] != 0):
        if (maze(rand_wall[0][rand_wall[1]-1] == 'u' and maze(rand_wall[0][rand_wall[1]+1] == 'c'):
                 # find the number of surrounding cells
                 s_cells = surroundingCells(rand_wall)

                 if (s_cells < 2):
                    # denote new path
                     maze[rand_wall[0][rand_wall[1]] = 'c'

                    # mark the new walls
                    if(rand_wall[0] != 0):
                          if(maze[rand_wall[0]-1][rand_wall[1]] !='c'):
                              maze[rand_wall[0]-1][rand_wall[1]] == 'w'
                          if([rand_wall[0]-1, rand_wall[1]] not in walls):
                              walls.append(rand_wall[0]-1, rand_wall[1])

                    # bottom cell
                    
                    
                 
    



# for a fixed height and with create a function to make empty maze
def init_maze(width, height):
    maz = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append('u')
        maze.append(line)

    return maze

maze = init_maze(width, height)
print_maze(maze)


create_maze()
make_walls(width, height)
create_entrance_exit(widht, height)

print(maze)

'''



'''
# for debugging purposes we will a function that prints the maze in a user
# friendly format.
 In order to be able to easily distinguish walls, cells and unvisited blocks,
 we will paint each letter with a different color,
 depending on the letter. To do so, we will use colorama .
'''




print(maze.print_maze)



'''



print('hi')
