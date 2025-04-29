# creating listing method
# 4. count

people: list[str] = ['bush', 'obama' , 'obama', 'trump']
bush = people.count('obama')
print(bush)#output: 2

# 5. extend

people: list[str] = ['elon', 'jeff', 'mark']
rappers: list[str]= ['wayne', 'tupac']

people.extend(rappers)
print(people)# output: ['elon', 'jeff', 'mark', 'wayne'' ,'tupac'']

# 6. index

people: list[str] = ['drake', 'c.brown', 'beyonce']

print(people.index('c.brown'))# output: 1