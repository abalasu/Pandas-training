import numpy as np
i = 0
outfile = open('d:/pythondata/stu_pass_fail.csv', "wt")
while i<3000:
    x = np.random.randint(11)
    y = np.random.randint(6)
    z = np.random.randint(2)
    print(x, y, z)
    a = str(x) + "," + str(y) + "," + str(z)
    outfile.writelines(a)
    i += 1

