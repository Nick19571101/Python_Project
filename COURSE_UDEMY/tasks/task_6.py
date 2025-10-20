#  вивести список виконаних і не виконаних завдань
# tasks = [ "Помити посуд" , "Сходити в магазин" , "Зробити ДЗ" , "Зателефонувати комусь" ]
# done = [ False , True , False , True ]

# for i in range(len(tasks)):
#     if done[i]:
#         mark = '[x]'
#     else:
#         mark = '[]'
#     print(f'{i + 1}, {mark} {tasks[i]}')

tasks = [
    [ "Помити посуд" , False ],
    [ "Сходити в магазин" , True ],
    [ "Зробити ДЗ" , False ],
    [ "Зателефонувати комусь" , True ]
]

for i in range(len(tasks)):
    task_name = tasks[i][0]
    is_fulfil = tasks[i][1]
    if is_fulfil:
        mark = '[x]'
    else:
        mark = '[ ]'
    print(f'{i + 1}. {task_name} - {mark}')
