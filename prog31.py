import sys
import math
import prog26

print('prog 26 loader:',prog26.__loader__)
print('prog 26 name:',prog26.__name__)
print('sys loader:',sys.__loader__)
print('sys name:',sys.__name__)
print('math spec:',math.__spec__)
print('prog 26 a:',prog26.a)
print('prog 26 show():',prog26.show())
print(__name__) # it prints the name of the current module