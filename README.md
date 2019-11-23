## rofi-checklist

## Objetivo

Esse script para rofi tem como propósito de ser um checklist ou seja ele é focado em tarefas que fazemos rotineiramente.

## Primeiros Passos

para simplificar o processo de instalação você pode abrir um terminal e digitar os seguintes comandos:
```$ cd ~/.local/bin/ && git clone https://github.com/Rodrigo-Barros/rofi-checklist ```

## Como funciona?

O script lê o arquivo em ~/.local/bin/rofi-checklist/tasks, para modificar o local onde suas tarefas ficam você pode 
alterar o arquivo task.py e editar o valor da variavél task_file para aonde você desejar salvar seu arquivo de 
tarefas, *** se for fazer mesmo isso apenas tenha o cuidado de não apagar a primeira linha do arquivo tasks*** dentro
de ~/.local/bin/rofi-checklist

### Como Usar

Execute o script rofi-checklist e escolha uma ação.

Aqui vai uma pequena dica se você tiver um desktop que te permita definir atalhos para executar aplicativos como o 
cinnamon tem ferramentas para isso ou mesmo o xfce definir uma combinação de teclas para chamar o rofi-checklist, e 
se me permite outra sugestão eu escolheria a combinação (tecla do windows) + t

## Funções

- Adicionar tarefa (ctrl+shift+a).
- Remover tarefa (ctrl+shift+b) e selectione a tarefa a ser removida.
- Alternar o estado da tarefa ou seja entre realizado e não realizada.
- Reseta as tarefas marcadas como concluídas a cada dia.

## Demonstração
![Preview](img/preview.gif)
