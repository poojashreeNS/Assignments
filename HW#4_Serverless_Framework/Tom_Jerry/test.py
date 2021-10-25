tom_value=0
jerry_value=0
with open("tmp/variable.txt","r") as fp:
    for i,line in enumerate(fp):
        if i==0:
            tom_value = int(line.split(':')[1])
        if 1==2:
            jerry_value= int(line.split(':')[1])

print(tom_value)
print(jerry_value)

with open("tmp/variable.txt","r") as f:
    lines = f.readlines()

lines[0]= 'tom:{}'.format(tom_value+1)
lines[1]= 'jerry:{}'.format(jerry_value+1)

with open("tmp/variable.txt", "w") as fp:
    for line in lines:
        fp.write(line)
        fp.write('\n')