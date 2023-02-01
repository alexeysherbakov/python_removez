with open('test.txt', 'r+') as txt:
    check_tags = False
    for line in txt:
        if '<glyphs' in line:
            check_tags = True
        if check_tags:
            line = line.replace('z','')
        if '/>' in line:
            check_tags = False
    txt.seek(0)
    txt.truncate()
    txt.write(line)

txt.close()
print ('File is successfully edited')

        


# with open('test.txt', 'rt') as f:
#         for line in f:
#             # print(line.rstrip())
#             if line.startswith('<glyph') and line.endswith('/>'):
#                 line.replace('z','')
#                 f.close()
#                 txt = open(f, 'wt')
#                 txt.write(line)
#                 txt.close()
#                 f.write()

            # txt_replace = txt.read().replace('z','')
            # txt.seek(0)
            # txt.truncate()
            # txt.write(txt_replace)
            # txt.close()
            # print ('File is successfully edited')