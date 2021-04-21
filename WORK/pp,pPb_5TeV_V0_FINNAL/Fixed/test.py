x = 3
y = 1


f = open("test.txt", "w")
f.write('New line ' + str(x) + ' +- ' + str(y) + '\n')
f.close()

x = 4
y = 2
f = open("test.txt", "a")
f.write('New line ' + str(x) + ' +- ' + str(y) + '\n')
f.close()
