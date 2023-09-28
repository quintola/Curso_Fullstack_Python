# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

#Importa o json pq quero salvar a lista em um arquivo
import json

print('#' * 50)
print('To do list'.upper())
print('#' * 50)

to_do_list = []
erased_list = []
command_list = ['list', 'undo', 'remake', 'save', 'load', 'exit']

while True:
    print('')
    print('Commands: List, Undo, Remake, Save, Load, Exit')
    task = input(f'Please, inform a task or a command: ').lower()
    
    if task not in command_list:
        to_do_list.append(task)

    if task == 'list':
        print()
        print('To do list'.upper())
        print()
        for item in to_do_list:
            print(item, end=' ' '\n')

    if task == 'undo':
        if len(to_do_list) > 0:
            erased_list.append(to_do_list.pop())
        continue

    if task == 'remake':
        if len(erased_list) > 0:
            to_do_list.append(erased_list.pop())
    

    if task == 'save':
        with open('to_do_list.json', 'w', encoding='utf-8') as archive:
            json.dump(to_do_list, archive, ensure_ascii=False, indent=2,)  

    if task =='load':
        with open('to_do_list.json', 'r', encoding='utf-8') as archive:
            saved_tasks = json.load(archive)
        for i in saved_tasks:
            to_do_list.append(i)
        
    if task == 'exit':
        break

    continue




