from os import system
import argparse
from datetime import date
from os import getenv

lines=-1
task_file = '%s/.local/bin/task/task' % getenv('HOME')


def do_task():
    number = int(input())
    file = open(task_file, 'r+')
    lines_of_text = file.readlines()
    mark = lines_of_text[number].split()[0]
    if mark == '+':
        lines_of_text[number] = lines_of_text[number].replace('+','-')
    elif mark == '-':
        lines_of_text[number] = lines_of_text[number].replace('-','+')
    temp_file = open('/tmp/temp_task_file','w')
    temp_file.writelines(lines_of_text)
    temp_file.close()
    system('cp /tmp/temp_task_file %s' % task_file)
    file.close()

def add_task():
    task_desc = input()
    file = open(task_file,'a')
    file.writelines('- %s\n' % task_desc)

def remove_task():
    line_removed_line = int(input())
    lines = getLines()
    del lines[line_removed_line]
    file=open('/tmp/temp_task_file','w')
    file.writelines(lines)
    file.close()
    system('cp /tmp/temp_task_file %s' % task_file)

def get_tasks():
    file=open(task_file,'r')
    global lines

    for line in file:
        lines += 1
        if line.split()[0] == '-':
            line = ('%s %s' % (lines,line.replace('-','[ ]')) )
        elif line.split()[0] == '+':
            line = ('%s %s' % (lines,line.replace('+','[X]')))
        elif line.split()[0] == 'timestamp':
            file_date = line.rstrip().split()[3].split('/')[0]
            line = 'Tarefas'
            
        #check_date(file_date)
        print(line.rstrip())
    file.close()

def check_date():
    file=open(task_file,'r')
    for line in file:
        if line.split()[0] == 'timestamp':
            file_date = line.rstrip().split()[3].split('/')[0]
    now = date.today()
    read_file_date = file_date.split('/')[0]
    if (now.day != int(read_file_date)):
        update_date()
        reset_tasks()
    else:
        update_date()
    file.close()

def update_date():
    now = date.today()
    line_index = -1
    file = open(task_file,'r')
    lines = getLines()
    temp_file = open('/tmp/temp_task_file','w')

    for line in file:
        line_index += 1
        if line.split()[0] == 'timestamp':
            lines[line_index] = 'timestamp atualizado em %s/%s/%s \n' % (now.day,now.month,now.year)
    temp_file.writelines(lines)
    temp_file.close()
    system('cp /tmp/temp_task_file /home/rodrigo/.local/bin/task/task')

def getLines():
    file = open(task_file,'r')
    return file.readlines()

def reset_tasks():
    line_index = -1
    lines = getLines()
    temp_file = open('/tmp/temp_task_file','w')
    for line in lines:
        line_index += 1
        if line.split()[0]=='+':
            lines[line_index] = line.replace('+','-')
    temp_file.writelines(lines)
    temp_file.close()
    system('cp /tmp/temp_task_file /home/rodrigo/.local/bin/task/task') 


parser = argparse.ArgumentParser()
parser.add_argument('--show-tasks',help='mostrar todas as terefas',action='store_true')
parser.add_argument('--do-task',help='faz a terefa espeficada',action='store_true')
parser.add_argument('--get-tasks',help='lista as tarefas',action='store_true')
parser.add_argument('--add-task',help='adiciona uma tarefa ao arquivo',action='store_true')
parser.add_argument('--remove-task',help='remove a tarefa do arquivo',action='store_true')
parser.add_argument('--reset-tasks',help='reseta as terefas para não feitas',action='store_true')
parser.add_argument('--check-date',help='verifica se a data informada no arquivo é diferente do dia atual',action='store_true')
args = parser.parse_args()

if args.do_task:
    do_task()
elif args.get_tasks:
    get_tasks()
elif args.add_task:
   add_task()
elif args.remove_task:
    remove_task()
elif args.reset_tasks:
    reset_tasks()
elif args.check_date:
    check_date()
