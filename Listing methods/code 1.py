# creating listing method
# 1.append

people: list[str] = ['bush', 'obama', 'trump']
people.append('biden')
print(people)# output: ['bush', 'obama', 'trump', 'biden']

# 2. clear

people: list[str] = ['elon', 'jeff', 'mark']
people.clear()
print(people)# output: []

# 3. copy

people: list:[str] = ['drake', 'c.brown', 'beyonce']
copy_people: list[str] = people.copy()
print(people)
print(copy_people)