#!/usr/local/bin/python3

words = ["cat", "window", "defenestrate"]
active_users = {}
users = {
	"user1" : "active",
	"user2" : "inactive"
}

for w in words:
	print(w, len(w))

#print("Users:", users)
#print("Active users:", active_users)

# Create new collection
for user, status in users.items():
	if status == "active":
		print("Adding", user, "to active users")
		active_users[user] = status

#print("Active users:", active_users)

# Iterate over a copy
for user, status in users.copy().items():
	if status == "inactive":
		del users[user]
		print("deleting user:", user)

#print("Users:", users)
