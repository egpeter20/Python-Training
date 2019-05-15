# Dictionary and sets

def main1():
    phonebook = {'Chris':'555−1111', 'Katie':'555−2222', 'Joanne':'555−3333'}
    
    num_items = len(phonebook) # The number of elements of the dictionary
    print('Total items in the list is', num_items)
    
    print(phonebook)
    
    if 'Chris' in phonebook:
        print('Chris is found and deleted from the phonebook')
        del phonebook['Chris']
    
    print('The phonebook after deleting chris:',phonebook)
    
    print() # Empty line for speacing
    
    phonebook = {'Chris':'555−1111', 'Katie':'555−2222', 'Joanne':'555−3333'}
    
    # Testing get function!
    value = phonebook.get('Chris','Found')
    print(value)
    value = phonebook.get('Peter','Peter is not found')
    print(value)
    
    print() # Empty line for speacing
    
    # Testing items function!
    for key, value in phonebook.items():
        print(key, value)
    
    print() # Empty line for speacing
    print(phonebook)
    
    print() # Empty line for speacing
    # Testing the Key funcation!
    for key in phonebook.keys():
        print(key)
    
    # Testing the pop funcation!
    #value = phonebook.pop('Peter', 'Peter is not found')
    
    #print(value)
    
    print() # Empty line for speacing
    
    # Testing the popitem funcation
    #k, v = phonebook.popitem()
    
    #print(k, v)
    
    # Testing the values funcation
    test_scores = { 'Kayla' : [88, 92, 100],
                    'Luis' : [95, 74, 81],
                    'Sophie' : [72, 88, 91],
                    'Ethan' : [70, 75, 78] }
                    
    for val in test_scores.values():
        print(val)
    # End of main1()

def main2():
    myset1 = set(['one', 'two', 'three'])    
    myset1.add('Yes')
    myset1.add('No')
    myset2 = set(['Here', 'Is', 'New', 'List'])
    myset1.update(myset2)
    
    # Testting the intersection funcation
    set1 = set([1, 2, 3, 4])
    set2 = set([3, 4, 5, 6])
    set3 = set1.intersection(set2)
    
    test = set2.issubset(set1)
    print('Testing the subset method is', test)
    print()
    
    groupMe = set1.union(set2)
    
    print('My lists contains') # Printing the whole group
    for val in groupMe:
        print(val)
    
    print() # Empty line!
    
    # Testing the symetric of 2 sets
    set3 = set1.symmetric_difference(set2)
    print('The symetric difference is', set3)
    print() # Empty line
    
    print('My intersection is', set3)
    print() # Empty line
    
    # Testting the difference funcation
    set3 = set1.difference(set2)
    set3 = set1 - set2
    
    print('The Difference in my sets are ',set3)
    print() # Empty line
    
    myset13 = myset1.union(myset2)
    print('Testting my union', myset13)
    print() # Empty line
    
    # myset1.remove('is')
    # myset1.discard('one') # testting the discard funcation
    # myset1.clear()
    
    print('My set contains', myset1)
    print() # Empty line for speacing
    
    for val in myset1:
        print(val)
    print() # Empty line
    
    # Testing if funcation
    if 'Here' in myset1:
        print('Here is found')
    else:
        print('Here is not found')
    
    size = len(myset1)
    
    print() # Empty line
    print('The size of my set is', size)
    
    
# Main funcations
# Calling main1()
main1()
main2()