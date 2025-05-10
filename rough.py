""" lis=[1,2,3]
my_str ="hi mohit"
myint=123

print(type(lis))
print(type(my_str))
print(type(myint))

lis.clear()
print(lis)
 """
""" 
a ="x"
b ="y"

print(a+b) """

 
#from oops_proj import chatbook
"""
obj = chatbook() """
""" # function vs method belows

lst =[1,2,3]

#function0

a1=len(lst)
print(a1)

# method  """
""" from oops_proj import chatbook
user1 = chatbook()
print(user1._chatbook__name) """

""" from oops_proj import chatbook
user1 = chatbook()
print(user1.id)

user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)
 """
# getter and setter 
""" print(user1.get_name())
user1.set_name("mohit bele")
print(user1.get_name()) """


from oops_proj import chatbook
user1 = chatbook()
print(user1.id)

chatbook.set_id(10)

user2 = chatbook()
print(user2.id)
