def count_calls():
    global calls
    calls += 1
    return

def  string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    result = False
    for i in list_to_search:
        if i.upper() == string.upper():
            result = True
            break
    return result

calls = 0
list_ = ['Upper', 'loweR', 'isUPPER', 'ISLOwer', 'dfDfdf']
print(string_info(list_[0]))
print(string_info(list_[1]))
print(string_info(list_[2]))
print(string_info(list_[3]))
print(is_contains('uPPer', list_))
print(is_contains('loWER', ["dfdfdf",'dfghjk', 'asqwAS']))
print('Количество вызовов функций:', calls)
