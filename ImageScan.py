import os
import subprocess
print("Loading...")
output = subprocess.check_output("scanimage -A", shell=True)
results = output.strip().split("\n")
args = {}
command = ['scanimage']
for i, s in enumerate(results):
    results[i] = s.strip()	
for i in results:
    if i[0] == '-':
        arg = i.split(' ')
        vals = arg[1].split('|')
        print('Arg: '),
	print(arg[0])
        print('Values: '),
        print(vals)
        print('Default value: '),
        print(arg[2])
        val = ''
        while True:
            val = raw_input()
            if val == '':
                break
            elif val not in vals:
                print('Invalid')
            else:
                args[arg[0]] = val
                command.append(arg[0])
                command.append(val)
                break
name = raw_input('Filename: ')
tiffname = '/tmp/' + name + '.tiff'
command.append('--format=tiff')
command.append('>')
command.append(tiffname)
print('Scanning...')
#print(name)
#print(args)
#print(command)
os.system(' '.join(command))
os.system('convert ' + tiffname + ' ' + name + '.png')
print('Complete!')
