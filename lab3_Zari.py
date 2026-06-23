# Zari W | Lab 3 | Blue

#Ticket 1

username = "lizardlover21"
print (len(username))   #13 , Yes

#Ticket 2

print (username[0]) #L
print (username[12]) #1
# It is minus 1 because the first character starts from 0.

#ticket 3

Welcome = "Welcome to loop,"
user = "@lizardlover21!"
full = Welcome + " " + user
print(full)  # Welcome to loop, @lizardlover21!

print(f"Welcome to loop, @{username}!")  # Welcome to loop, @lizardlover21!

#  Yes, both lines will look the same. 
# I personally found using concatenation easier, since I just had to type "full".

#ticket 4

 # NameError: name 'X' is not defined

caption = "LIZARDLOVER21"
print(caption) # LIZARDLOVER21 

# I think it means the string cant be changed?

#ticket 5

feed = ["Beach Day!", "June photo dump", "I love animals!"]
print (len(feed)) #3
print(feed[0]) # Beach Day!

#Ticket 6

feed.append("Movie day, watch Obsession!")
print(feed) #3, because they count starting at 0.

#Ticket 7

feed.pop(0) #Removes Beach Day!
feed = ["I love animals!", "June photo dump", "Moive day, watch Obsession!"]
print(feed)
#I used pop, which deleted a part of the list, and append, which added something to the list.

#Ticket 8

profile = {"username": "lizardlover21", "followers": "21",}
Verified = False
print(profile)
# profile [0] KeyError: 0

#It prints 21 followers, and I think profile[0] tries to print "username"?
#I think its immutable

#Ticket 9

profile = {"username": "lizardlover21", "followers": "71","bio":"Hello new followers!"}
print(profile)
# git(age) NameError:name'git' is not defined.
# It prevents your code from crashing

#Ticket 10

print(f"@{username} has 71 followers and {len(feed)} posts. Top post: {feed[0]}")
#@lizardlover21 has 71 followers and 3 posts. Top post: I love animals!
# I used print, f-string, list, dictionary, and index.