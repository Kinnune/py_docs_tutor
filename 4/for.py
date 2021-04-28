#!/usr/local/bin/python3

words = ["cat", "window", "defenestrate"]
for w in words:
    print(w, len(w))

active_users = {}
users = {
    "user1" : "active",
    "user2" : "inactive"
}
print("Users:", users)
print("Active users:", active_users)

# add active users to active_users
for user, status in users.items():
    if status == "active":
        print("Adding", user, "to active_users")
        active_users[user] = status

print("Active users:", active_users)

# copy users list for iteration and remove inactives from the original
for user_cpy, status in users.copy().items():
    if status == "inactive":
        del users[user_cpy]
        print("deleting user:", user_cpy)

print("Users:", users)
