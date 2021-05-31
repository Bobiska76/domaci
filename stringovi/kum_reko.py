s = input('neki string: ').lower().split(' ')
s = ''.join(s)
if s == s[:: -1]:
    print('palindrom')
else:
    print('nije')
