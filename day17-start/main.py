# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class User:

    def __init__(self, user_id, username):
        # print("new user begging create")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "ake")

user_1.follow(user_2)
print(f"{user_1.username} has followers = {user_1.followers}")
print(f"{user_1.username} has following = {user_1.following}")

print(f"{user_2.username} has followers = {user_2.followers}")
print(f"{user_2.username} has following = {user_2.following}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
