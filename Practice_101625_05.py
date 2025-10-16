fo = open("myPythonTxt01.txt", "w")
print(fo.mode)
fo.write("text entered from python @101625-0754pm\n")
fo.write("text entered from python @101625-0756pm\n")
my_content = ["alpha\n", "bravo\n", "charlie\n"]
fo.writelines(my_content)

my_fruits = ["apple", "banana", "cherry"]
for fruit in my_fruits:
    fo.writelines(fruit+"\n")

fo = open("myPythonTxt01.txt")
print(fo.read())
print(fo.mode)

fo.close