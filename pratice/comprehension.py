# normal way to create the list 


aadi_books = []

for items in range(10):
    aadi_books.append(items)

print(aadi_books)


# create list using comprehensiopn

aadi_books =[item for item in range(10) if item%2==0]
print(aadi_books)

## create a dictinory using python comprehension



aadi_dict= {i:f"item{i}" for i in range(10)if i%2==0}
print(aadi_dict)



##create a sets using comprehension

aadi_sets={dress for dress in["dress1","dress2","dress1","dress2","dress1","dress2","dress1","dress2"]}

print(aadi_sets)


# create a Generator using comprehension


aad_generator = (item for item in range(50) if item%2 ==0)
# print(aad_generator.__next__())
for item in aad_generator:
    print(item)
