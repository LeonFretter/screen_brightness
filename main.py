from subprocess import Popen, PIPE, call
import sys

if len(sys.argv) != 2:
    print('usage: cmd brightess')
    exit()

brightness = sys.argv[1]

if float(brightness) < .2:
    print('Dude, dont you want to be able to read something?')
    exit()
else if float(brightness) > 1:
    print('Ahh, thats not such a good idea!')
    exit()

cmd = Popen(['xrandr', '-q'], stdout=PIPE, stderr=PIPE, stdin=PIPE)



stdout, stderr = cmd.communicate()
stdout_str = stdout.decode('utf-8')

lines = stdout_str.splitlines()


for line in lines:
    if 'connected' in line:
        words = line.split()
        connection = words[0]
        call(['xrandr', '--output', connection, '--brightness', brightness])