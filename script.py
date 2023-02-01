import os.path
import os
from pathlib import Path
# from pathlib import Path

# filepath = input(f'Would you like to change the path {os.getcwd()}? Y/N:\t')
# if filepath == 'Y':
#     new_filepath = input('Enter the new path:\n')
#     pnew = Path(new_filepath)
#     print(os.getcwd())
#     print(pnew)
#     txtpath = input('path for files: ')
#     p = (txtpath)
# elif filepath == 'N':
#     print('Keeping the current path...')
# else:
#     print('Select either Y or N')
#     exit()

txtpath = input('Enter filename with .txt extention: ')
p = (txtpath)
# print (os.path.splitext(p)[1])

if os.path.exists(p) == False:
    # p + 'txt'
    print('File does not exist, or you forgot to add the .txt extention...')
elif p.endswith( '.txt' ):
    txt = open(p, 'r+')
    txtinc = txt.read()
    repltxt = txtinc.replace('z"','"')
    txt.close()
    txt = open(p, 'wt')
    txt.write(repltxt)
    txt.close()
    print ('File is successfully edited')
# else:
#     print('Sorry, seems like you forgot to add the .txt extention...')
#     return (txtpath)

#r+	Для чтения и записи.