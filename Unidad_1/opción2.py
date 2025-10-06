from random import choice, sample

my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", "voavanga"]

print(sample(my_list, 3), end=' ')
choice1 = choice(my_list)
print(choice1)
my_list.remove(choice1)
choice1 = choice(my_list)
print(choice1)
my_list.remove(choice1)
choice1 = choice(my_list)
print(choice1)
my_list.remove(choice1)
