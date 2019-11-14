# fibonacci.py

def fib():
    fibs = [1, 2]
    val_1 = 1
    val_2 = 2
    
    for i in range(1,9):
        next_num = val_1 + val_2
        fibs.append(next_num)
        val_1 = val_2
        val_2 = next_num

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()