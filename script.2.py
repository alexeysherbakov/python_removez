# txt = open('test.txt', 'r+')
# txtinc = txt.read()
# for line in txtinc:
#     if line.startswith('d='):
#         repltxt = txtinc.replace('z','')
#         print('done')

with open('test.txt', 'rt') as f:
        for line in f:
            # print(line.rstrip())
            if line.startswith('<glyph') and line.endswith('/>'):
                line.replace('z','')
                f.close()
                txt = open(f, 'wt')
                txt.write(line)
                txt.close()
                f.write()