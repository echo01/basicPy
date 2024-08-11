import random

list1 = ["Midoriya","Todoroki","Uraraka","Bakugo","Asui"]

# แบบที่1
# print(f"Hero name : {list1[0]}")
# print(f"Hero name : {list1[1]}")
# print(f"Hero name : {list1[2]}")
# print(f"Hero name : {list1[3]}")
# print(f"Hero name : {list1[4]}")
#แบบที่2
# for nd in range(0,5):
#     print(f"Hero name : {list1[nd]}")
#แบบที่-
# for n in list1:
#     print(f"Hero name : {n}")


hero_dic1={
    "name":"Midoriya",
    "height": 166,
    "age":16,
    "power":5000
}
hero_dic2={
    "name":"Todoroki",
    "height": 176,
    "age":16,
    "power":4900
}
hero_dic3={
    "name":"Uraraka",
    "height": 156,
    "age":16,
    "power":3000
}
hero_dic4={
    "name":"Bakugo",
    "height": 172,
    "age":17,
    "power":4800
}
hero_dic5={
    "name":"Asui",
    "height": 150,
    "age":16,
    "power":2500
}

#แบบที่1
# print(f"Hero name : {hero_dic1}")
# print(f"Hero name : {hero_dic2}")
# print(f"Hero name : {hero_dic3}")
# print(f"Hero name : {hero_dic4}")
# print(f"Hero name : {hero_dic5}")

list2=[hero_dic1,hero_dic2,hero_dic3,hero_dic4,hero_dic5]
# แบบที่2
# for n in range(5):
#     print(f"Hero name : {list2[n]['name']}")
#แบบที่3
# for n in list2:
#     print(f"Hero name : {n['name']}")

def game():
    use_choose = input("Do you want to play gamey? (y/n)")
    if use_choose == 'y':
        use_hero = random.choice(list2)
        print(f"your hero is : {use_hero['name']}")
        pc_hero = random.choice(list2)
        print(f"PC hero is : {pc_hero['name']}")
        if use_hero['power'] > pc_hero['power']:
            print("You WIN..")
        elif use_hero['power'] < pc_hero['power']:
            print("You lose..")
        else:
            print("Draw..")
        return (True)
    else:
        print("bye bye")
        return(False)



is_finish =True
# while is_finish:
#     use_choose = input("Do you want to play gamey? (y/n)")
#     if use_choose == 'y':
#         use_hero = random.choice(list2)
#         print(f"your hero is : {use_hero['name']}")
#         pc_hero = random.choice(list2)
#         print(f"PC hero is : {pc_hero['name']}")
#         if use_hero['power'] > pc_hero['power']:
#             print("You WIN..")
#         elif use_hero['power'] < pc_hero['power']:
#             print("You lose..")
#         else:
#             print("Draw..")
#     else:
#         is_finish = False
#         print("bye bye")

while is_finish :
    is_finish = game()
print("end program")
