#字典推导式（Dictionary comprehensions）{expr1: expr2 for k, v in d}，这个语法等价于
result={'c':'d'}
for k, v in result.items():
    result['c']='b'
print(result)

str={'c':'e' for k,v in result.items()}
print(result)