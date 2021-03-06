import random
import sys
import numpy as np

class mapGeneration():
    
    def __init__(self, rows, columns, filename):
        self.rows = int(rows)#input("Enter the number of self.rows: ")
        self.columns = int(columns)#input("Enter the number of self.columns: ")
        self.filename = filename#input('filename: ')
        self.f = open("{}".format(filename), "w+")
        self.playerpos = (self.columns/2, self.rows/2)

        self.map_arr = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                        'E', '.', 'E', '.', 'E', '.', 'E', 'E', 'E', 'E', '.', '.', '.',
                        '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                        '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                        '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                        '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                        '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                        '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                        '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                        '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                        '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                        '1', '1', '.', '.', '1', '.', '.', 'E', '.', 'E', '1', '.', '.',
                        '1',  '.', '.',  '1', '.',  '.', '1',  '.', ]

    def generate(self):
        i = 0
        map = []
        while i in range(0,self.rows):
            #if i == 0:
            #    for k in range(0, self.columns):
            #        f.write("1")
            if i == self.rows -1:
                for l in range(0, self.columns):
                    self.f.write("1")
            else:
                for j in range(0, self.columns):
                    check = (i,j)
                    if j == 0:
                        self.f.write("1")
                    elif j == self.columns-1:
                        self.f.write("1")
                    elif check == self.playerpos:
                        self.f.write('P')
                    else:
                        x = random.randint(0,len(self.map_arr)-1)
                        self.f.write(self.map_arr[x])
            i += 1
            #print(i, self.rows)
            self.f.write("\n")

m = mapGeneration(input('rows '), input('columns '), 'mapexample.txt')
m.generate()
#noise = np.random.normal(1,1,10)
#sys.stdout.write(str(noise))