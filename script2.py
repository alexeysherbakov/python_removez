p = input('Enter filename with .txt extention: ')

if not p.endswith('.txt'):
    print('The file must have a .txt extension!')
    exit()

with open(p, 'r') as txt:
    lines = txt.readlines()

check_tags = False
new_lines = []
for line in lines:
    if 'd=' in line:
        check_tags = True
    if check_tags:
        line = line.replace('z','')
    if '/>' in line:
        check_tags = False
    new_lines.append(line)

with open(p, 'w') as txt:
    txt.writelines(new_lines)

print ('File has been successfully edited')