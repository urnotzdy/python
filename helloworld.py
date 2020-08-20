
#使用小写作为变量名
message='msg1'
print(message)

message='msg2'
print(message)


#修改大小写
#title使每个单词的变量名为大写
#upper
#lower
name='eric'
message='Hello '+name.title()+', would you like to learn some Python today?'
print(message)

print(name.lower())
print(name.upper())
print(name.title())


name='Albert Einstein once said,"A person who never made a mistake never tried anything new."'
print(name)

#使用+合并字符串
famous_person='Albert Einstein'
name=famous_person+' once said,"A person who never made a mistake never tried anything new."'
print(name)

#制表符对齐\t
#换行符\n
name=' kong bai '
print(name)
print('\t'+name.lstrip())
print(name.rstrip())
print ('\n\t'+name.strip())
#strip lstrip rstrip删除空白


print(1*2+3)

print(3*4)
#浮点数的小数点不确定
#str将非字符串转成字符串
print("hello,it's "+str(5.0/3))
