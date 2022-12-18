'''
file = open('demo.txt', 'r+', encoding='utf-8')
lines = file.readlines()
lines = lines[:-1]
lines_2 = lines.write("hello!!!")

print(lines)
print(lines_2) '''

file = open('../demo.txt', 'r', encoding='utf-8')
lines = file.readlines()
lines = lines[:-1]

print(lines)