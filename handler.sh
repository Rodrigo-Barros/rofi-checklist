#!/bin/sh
SCRIPT_EXEC_PATH="$HOME/.local/bin/task"

function get_action(){
  error=$?
  if [[ $error -eq  10 ]];then
    add_task
  elif [[ $error -eq 11 ]]; then
    remove_task
  elif [[ $erro -eq 0 ]];then
    task_number=$(echo $task_number | awk '{print $1}')
    echo $task_number | python $SCRIPT_EXEC_PATH/task.py --do-task 
  fi
}

function add_task() {
  rofi -dmenu -p "Nova Tarefa" | python $SCRIPT_EXEC_PATH/task.py --add-task
  main_menu
  get_action
}

function remove_task() {
   task_number=$(python $SCRIPT_EXEC_PATH/task.py --get-tasks | rofi -dmenu -p "Remover tarefa " -mesg "$msg" -kb-custom-1 "Ctrl+A" -kb-custom-2 "Ctrl+R" -kb-custom-3 "Alt-Tab")
  task_number=$(echo $task_number | awk '{print $1}')  
  echo $task_number | python $SCRIPT_EXEC_PATH/task.py --remove-task
  main_menu
  get_action
}

function main_menu(){
  task_number=$(python $SCRIPT_EXEC_PATH/task.py --get-tasks | rofi -dmenu -p "TODO " -mesg "$msg" -kb-custom-1 "Ctrl+A" -kb-custom-2 "Ctrl+R" -kb-custom-3 "Alt-Tab")
}
msg="Bem vindo ao seu checklist para adicionar uma nova tarefas aperte 'Ctrl+Shift+a, para remover uma tarefa aperte Ctrl+Shift+r', e para voltar para esse menu aperte 'Alt+Tab'"
python $SCRIPT_EXEC_PATH/task.py --check-date
main_menu
get_action
