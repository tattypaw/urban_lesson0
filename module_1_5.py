immutable_var = ("Peter", 22, "физмат", True, [5,4,5,3],"Mikle", 21, "физмат", False, [2,4,5,3])
print("Кортеж (изменять нельзя): ",immutable_var)

#immutable_var[0] = "Mary"

# попытка изменить имя вызывает ошибку, т.к. не поддерживает обращение по элементам -

#Traceback (most recent call last):
#  File "C:\Users\mvideo\Desktop\Urban\lesson1\pythonProject1\module_1_5.py", line 3, in <module>
#    immutable_var[0] = "Mary"
#TypeError: 'tuple' object does not support item assignment

mutable_list = ["Peter", 22, "физмат", True, [5,4,5,3],"Mikle", 21, "физмат", False, [2,4,5,3]]
print("Список: ", mutable_list)
mutable_list[0] = "Mary"
print("Измененный список: ",mutable_list)