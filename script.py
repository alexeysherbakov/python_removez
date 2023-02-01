p = input('Enter filename with .txt extention: ')

if not p.endswith('.txt'):
    print('The file must have a .txt extension!')
    exit()

with open(p, 'r+') as txt:
    txt_replace = txt.read().replace('z"','"')
    txt.seek(0)
    txt.truncate()
    txt.write(txt_replace)
    txt.close()
    print ('File is successfully edited')