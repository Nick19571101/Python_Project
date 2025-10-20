import subprocess
action_prompt = """Що маємо робити?:>>>\n
Виберіть свій варіант:\n
1 - працюємо.
2 - відпочиваємо,
3 - граємо
"""
action =int(input(action_prompt))
if action <= 0 | action > 3:
    print("Некоректний вибір!")
elif action == 1:
    print("Ви вибрали працювати!")
    subprocess.Popen('start https:\\udemy.com', shell=True)
elif action == 2:
    print("Ви вибрали відпочивати!")
    subprocess.Popen('start https:\\youtube.com', shell=True)
else:
    print("Ви вибрали пограти!")
    subprocess.Popen('start https:\\google.com', shell=True)


# print(f"ваш вибір: {action}")
