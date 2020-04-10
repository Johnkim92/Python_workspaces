f = open('c:/Users/USER/AppData/Local/Programs/Python_workspaces/classes/sel_list.txt', 'wt')
f.write('삼성전자\n')
f.write('하이닉스\n')
f.close()




f = open('c:/Users/USER/AppData/Local/Programs/Python_workspaces/classes/sel_list.txt', 'rt')
lines = f.readlines()

for line in lines:
    print(line, end='')

