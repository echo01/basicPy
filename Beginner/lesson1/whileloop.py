
while input("Do you want to play game y/n:") == 'y':
    print("start game")
    x = int(input('x='))
    y = int(input('y='))
    operator = input('operator *,+,-,/')
    if operator == '+':
        print(f"x+y={x+y}")
    elif operator == '-':
        print(f"x-y={x-y}")

print("Game is end.")
