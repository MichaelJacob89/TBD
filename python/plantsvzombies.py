def plants_and_zombies(lawn,zombies):
    lawn = [
        '2       ',
        '  S     ',
        '21  S   ',
        '13      ',
        '2 3     '
    ]
    zombies = [[0,4,28],[1,1,6],[2,0,10],[2,4,15],[3,2,16],[3,3,13]]
    blank = []
    for i in lawn:
        for j in i:
            blank.append(j)
    



plants_and_zombies(1,2)