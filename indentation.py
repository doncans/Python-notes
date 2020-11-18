'''
l1 = [5,6,7,8,9,0,10]

#out_put = [25, 36, 49,....]

for i in l1:
	print(i**2)
'''
# x = 6
# while x > 0: 6>0
#     print("iteration %s"%x)
#     x -= 1


def sqr_val(l1):
    sqr_list = []
    for i in l1:
        sqr_list.append(i**2)
    return sqr_list

def cube(l2):
	cube_list = []
	for i in l2:
		cube_list.append(i**3)
	return cube_list

lst = [5,6,7,8]
lst1 = sqr_val(lst)
print(cube(lst1))
print(cube(sqr_val(lst)))




