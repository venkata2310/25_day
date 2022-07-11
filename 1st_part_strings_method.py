'''String Methods'''
# 1 capitalize
# a='python'
# print(a.capitalize()) #Python

# 2 casefold
# b= 'PYTHON'
# print(b.casefold()) #python
# c= 'PyTHOn'
# print(c.casefold()) #python

# 3 center
# a='hello world'
# print(a.center(30)) #         hello world

#4 count
# x='hola, i know you, hola even i know you!'
# print(x.count('hola')) #2

#5 encode
# z='hello my self råm'
# print(z.encode()) #b'hello my self r\xc3\xa5m

#6 endswith
# a='hi, welcome to codingworld.com'
# print(a.endswith('.'))#false
# print(a.endswith('com'))#true

#7 expandtabs
# a='he\te\to\ti'
# print(a.expandtabs(2))#he e o i

#8 find
# a='my name is ram'
# print(a.find('e')) #6

#9 format
# a="I have a budget this month of {price} Rupee."
# print(a.format(price=10000))#I have a budget this month of 10000 Rupee.

#10 format_map
# a='Rajesh has an amount of{1000} Dollars in his bank account.'
# print(a.format_map())

#11 index
# x='Hi, welcome to coding classes'
# print(x.index('coding')) #15

#12 isalnum
# x='Iwenttoclasses365Days'
# print(x.isalnum()) #true

#13 isalpha
# z='Microsoft'
# print(z.isalpha()) #true

#14 isdecimal
# v= '38989'
# # print(v.isdecimal()) #true
# z='348378.843984'
# print(z.isdecimal()) #false

#15 isdigits
# a= '728376'
# print(a.isdigit()) #true

#16 isidentifier
# x='8gdgdjj'
# print(x.isidentifier()) #false

# y='hdjfddiksd'
# print(y.isidentifier()) #true


#17 islower
# z='visualcode'
# print(z.islower()) #true

#18 isnumeric
# s='387339837437324373'
# print(s.isnumeric()) #true

# s='387339837.437324373'
# print(s.isnumeric())#false


#19 isprintable
# w='*%4334544$#4##$%$#$#$%$%'
# print(w.isprintable())

#20 isspace
# x='my name is raj'
# print(x.isspace()) #false

# z='      '
# print(z.isspace()) #true
