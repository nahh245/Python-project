# creating listing method
# 7. insert

people: list[str] = ['bush', 'obama', 'trump']
people.insert(1, 'biden')
print(people)#output: ['bush', 'biden', 'obama', 'trump'']

# 8. pop

people: list[str] = ['elon', 'jeff', 'mark']
popped = people.pop(0)

print(popped)# output : elon
print(people)# output: ['jeff', 'mark']

# 9. remove

people: list[str] = ['drake', 'c.brown', 'beyonce']
people.remove('c.brown')
print(people)# output: ['drake', 'beyonce']
