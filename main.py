size = 9
grid = [
    ['*'] *size for i in range(size)
]

print('Enter coordinates space separated.')
a = list(map(int,input('Start cords: ').split()))
b = list(map(int,input('End cords: ').split()))

a[0] -= 1
a[1] -= 1
b[0] -= 1
b[1] -= 1
a[0],a[1] = a[1],a[0]
b[0],b[1] = b[1],b[0]

visited = [[False] *size for i in range(size)]

queue = [a[:]+[[]]]
#print(queue)
while len(queue) > 0:
    y,x,path = queue.pop(0)[:]
    path = path[:]
    #print([y,x],b)
    if x<0 or y<0 or x>size-1 or y>size-1:
        pass
    elif visited[y][x]:
        pass
    elif [y,x] == b:
        #print(path)
        break
    else:
        visited[y][x] = True
        path.append([y,x])

        queue.append([y+1,x,path])
        queue.append([y-1,x,path])
        queue.append([y,x+1,path])
        queue.append([y,x-1,path])

print(path)
for y,x in path:
    grid[y][x] = 'G'
grid[b[0]][b[1]] = 'G'

for i in range(size):
    for j in range(size):
        if i!=0 and grid[i-1][j] == 'G' and grid[i][j] != 'G':
            grid[i][j] = 'R'
        elif j!=0 and grid[i][j-1] == 'G' and grid[i][j] != 'G':
            grid[i][j] = 'R'
        elif i != size-1 and grid[i+1][j] == 'G' and grid[i][j] != 'G':
            grid[i][j] = 'R'
        elif j != size-1 and grid[i][j+1] == 'G' and grid[i][j] != 'G':
            grid[i][j] = 'R'
grid[b[0]][b[1]] = 'D'

print('G: green parallel, red perpendicular')
print('R: red both ways')
print('*: unchanged')
print('  '+' '.join(list(map(str,range(1,size+1)))))
for i in range(size):
    print(f'{i+1} '+' '.join(grid[i]))
