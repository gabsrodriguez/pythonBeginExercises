def number_of_bottles():
    for n in range(99,-1,-1):
        if n > 0: 
            print(n, "bottles of milk on the wall,", n, "bottles of milk.")
            print("take one down and pass it around,", n-1, "bottles of milk on the wall.")
        else: 
            print("no more bottles of milk on the wall, no more bottles of milk.")
            print("go to the store, buy some more, 99 bottles of milk on the wall.")

number_of_bottles()