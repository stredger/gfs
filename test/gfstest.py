
import sys
sys.path.append('..')

import gfs

fs = gfs.SwiftFS('http://localhost:8080/auth/v1.0', 'savant', 'savant', 'savant')

# f = fs.open('helo.txt', True)

# if not f:
#     sys.exit()
# print f.readlines()
# f.write('helo mang')
# #print f.getvalue()
# #f.seek(0)
# #print f.readlines()
# f.close()

# f = fs.open('helo.txt')
# print f.readlines()
# f.close()
# print fs.localfiles

fs.move( 'ello.txt', 'helo.txt')
