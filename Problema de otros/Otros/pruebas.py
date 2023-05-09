import numpy as np

arr = ['hola', 'mundo']  # np.full(3, 4)
print(arr)
x = ' '.join(arr)
print(x)
f = 4
try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except NameError:
    print("Variable x is not defined")
except:
    print("Something went wrong when writing to the file")
finally:
    print(f)
arr = sorted(arr, key=len, reverse=True)
print(arr)
new_arr = np.array([4, 5, 6])
x = [new_arr < 5]
print(x)
new_arr = new_arr[new_arr < 5]
print(new_arr)


def cuadrado(arg):
    return arg % 4


list = [3, 4, 5]
print(sorted(list, key=cuadrado))
# %%
arr = [3, 4, 5]
dir(arr)
# arr.count
arr.index(5)
arr.reverse()
arr
arr.sort
arr.remove(5)
arr
arr.insert
arr.insert(0, 5)
arr
arr.insert(6, 7)
arr
arr.pop
arr.pop(0)
arr
arr.count
arr.count(7)
arr.clear
arr.clear()
arr
arr.remove
arr = [4, 5, 6, 8]
arr.remove(5)
arr


# %%
str = 'Hello world'
dir(str)
str.zfill(10)

# %%
dic = {
    'saludo': 'hola',
    'nombre': 'Leydi'
}
dic = [5, 4, 6]
for index, value in enumerate(dic):
    print(index, value)
