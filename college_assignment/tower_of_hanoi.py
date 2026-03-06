def tower_of_hanoi(n, fr, des, to):
    
    if(n == 1):
        print(f"{fr} to {des}")
        return
    tower_of_hanoi(n - 1, fr, to, des)
    print(f"{fr} to {des}")
    tower_of_hanoi(n - 1, to, des, fr)

tower_of_hanoi(3, 'A', 'B', 'C')
