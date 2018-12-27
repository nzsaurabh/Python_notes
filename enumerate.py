#! python3

game = [["a","b","c"],
        [0,0,0],
        [0,0,0],
        [0,1,"test_index"]]

game_iter = list(enumerate(game))
print(game_iter)
print("Length of enumerate object: " + str(len(game_iter)))
print(range(3))

print(game_iter[3][1])
print(game_iter[3][1].index("test_index"))
print(type(game_iter[2][1]))


#print(game_iter.index(0))

for count, row in game_iter:
    print(count,str(row))

  
