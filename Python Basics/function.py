## Functions
# def data(x,y):
#     print(x+' Lahir th ' + y)

# data('adi','1990')
# data('Budi','1991')
# data('Caca','1992')
# data('Dedi','1993')

# def total(x,y):
#     z = x + y
#     return z

# print(total(4,5))
# # print(z)

# def kali(x) :
#     if( x < 2 ) :
#         return 1
#     else :
#         return(x * tiga())

# def tiga() :
#     return 3

# print(kali(5))

# def kali(angka1 = 5, angka2 = 2) :
#     return angka1 * angka2

# print(kali(angka2=3))

## List
# principe = ['Horner', 'Steiner', 'Binotto', 'Abiteboul', 'Williams','Wolff', 'Brown']

# print(principal[0:4])
# for man in principal :
#     print(man)

# principe[1] = 'Briatore'
# print(principe)

# principe.append('briatore')
# print(principe)
# principe.pop()
# print(principe)

# listTest = [1, 'hi', ['hello', 2, True, [0 , 1]]]

# print(listTest[1])
# print(listTest[:2])
# print(listTest[2])
# print(listTest[2][2])
# print(listTest[2][1:])
# print(listTest[2][3][0])

# x =[40, 100, 1, 5, 25, 10]

# for i in x:
#     if ( i > i+1):
#         x=x[0:]
#         x.append(i)
#     # return x
# print(x)

# exp_list = [ i for i in range(10) if i < 9 and i % 2]
# exp_list2 = [i if i < 5 and i % 2 else i*2 for i in range(10)]
# print(exp_list)

buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga', 'Pir']
buah_2 = [i[:2] if len(i) > 4 else i.replace(i, 'Buah Lain') for i in buah]
print(buah_2)

print(enumerate(buah))
for i, j in enumerate(buah):
    print(i)
    print(j)