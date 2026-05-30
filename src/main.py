import json

while True:
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"tasks": []}

    print("\n--- Список задач ---")
    if not data["tasks"]:
        print("(список пуст)")
    else:
        for index, task in enumerate(data["tasks"]):
            print(f"{index}. {task['title']} [Статус: {task['status']}]")
    print("--------------------")

    a = input("Введите: 1 - добавить задачу, 2 - выполнить, 3 - удалить, 4 - выполненные задача 0 - выход: ")
    
    if a == '1':
        task_text = input('Введите задачу: ')
        new_task = {"title": task_text, "status": "в процессе"}
        data["tasks"].append(new_task)
        
    elif a == '2':
        if not data["tasks"]:
            print("Нечего выполнять!")
            continue
        ans = input('Какую задачу хотите выполнить (Введите номер): ')
        try:
            data["tasks"][int(ans)]["status"] = "completed"
        except (ValueError, IndexError):
            print("Неверный номер задачи!")
            continue
            
    elif a == '3':
        if not data["tasks"]:
            print("Нечего удалять!")
            continue
        ans = input('Какую задачу хотите удалить (Введите номер): ')
        try:
            data["tasks"].pop(int(ans))
        except (ValueError, IndexError):
            print("Неверный номер задачи!")
            continue
            
    elif a == '0':
        print("Выход из программы.")
        break
    else:
        print("Неизвестная команда!")
        continue

    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
