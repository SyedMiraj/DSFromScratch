# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 20:59:24 2018

@author: Shahriar Miraj
"""
from collections import Counter

# Find the key connectors are among the data scientist

users = [
            {"id" : 0, "name" : 'Miraj'},
            {"id" : 1, "name" : 'Kamal'},
            {"id" : 2, "name" : 'Abi'},
            {"id" : 3, "name" : 'Reja'},
            {"id" : 4, "name" : 'Shahin'},
            {"id" : 5, "name" : 'Shihab'},
            {"id" : 6, "name" : 'koushik'},
            {"id" : 7, "name" : 'Masud'},
            {"id" : 8, "name" : 'Reja'},
            {"id" : 9, "name" : 'Tama'}
        ]

friendship = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), 
              (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friend"] = []
    
for i, j in friendship:
    users[i]["friend"].append(users[j])
    users[j]["friend"].append(users[i])
    
# find number of friend of each user

def number_of_friend(user):
    return len(user["friend"])

total_connection = (sum(number_of_friend(user) 
                             for user in users ))
'''
for user in users:
    print(user["name"] + " has " + str(len(user['friend'])) + " friends. They are ")
    for friend in user['friend']:
        print(friend['name'] + ", " )
'''

num_friend_by_id = [(user['id'], number_of_friend(user)) for user in users ]

# suggest a user that might know another user

def friend_of_friend_by_id(user):
    return [fof['id'] 
                for friend in user['friend']
                for fof in friend['friend']]
    
def not_the_same(user, other_user):
    return user != other_user

def not_friends(user, other_user):
    return all(not_the_same(friend, other_user) for friend in user['friend'])

def friend_of_friend_ids(user):
    return Counter(fof['id']
                   for friend in user['friend']
                   for fof in friend['friend']
                   if not_the_same(user, fof) and 
                   not_friends(user, fof))
    
print(not_friends(users[1], users[5]))

#print(friend_of_friend_ids(users[3]))
    

