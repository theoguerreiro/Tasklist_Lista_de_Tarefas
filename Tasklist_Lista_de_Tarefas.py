# Funções

# adicionar uma task para lista
def addtask(tasklist,task):
    tasklist.append(task)
    return tasklist

# deletar uma task da lista - os itens na lista são int, logo o valor na string deve ser subtraído para compensar o 0
def deletetask(tasklist,task):
    tasklist.pop((task - 1))
    return tasklist

# Código em inglês
def menu_eng():
    running = True
    tasklist = list()

    print("\nWelcome to your task list!")

    # Aqui foi feito um loop para a lista de tarefas
    while running:
        print("\n===== MENU =====\n" \
        "1 - Input new task\n" \
        "2 - Show list\n" \
        "3 - Delete task\n" \
        "4 - Exit")
        print('-' * 30)
        option = input('Type the number of your option: ')
    
        # Adição da tarefa usando a função
        if option == "1":
            task = input('Input a new task: ')
            tasklist = addtask(tasklist,task)
            print('--> Task added.')
            print('-' * 30)
    
        # Uso da função para mostrar itens da lista
        elif option == "2":
            print("\n"f"{'   '* 2}TASK LIST")
            showlist(tasklist)
        
        # Remoção de tarefa com condições caso o input for inválido (verificando se a resposta é numerica e transformando número strg em int)
        elif option == "3":
            task = input('Type the number of the task to remove: ')
            if not task.isnumeric():
                print("[!] Invalid number.")
            elif int(task) > len(tasklist):
                print("[!] Invalid number.")
            elif int(task) <= 0:
                print("[!] Invalid number.")
            else:
                task = int(task)
                deletetask(tasklist, task)
                print("--> Task removed.")
                print('-' * 30)

        # Fim do loop
        elif option == "4":
            running = False

        else:
            print("[!] Invalid option.")

# Código em português
def menu_pt():
    running = True
    tasklist = list()

    print("\nBem-vinde a sua lista de tarefas!")

    # Loop para a lista de tarefas
    while running:
        print("\n===== MENU =====\n" \
        "1 - Adicionar tarefa\n" \
        "2 - Mostrar lista\n" \
        "3 - Remover tarefa\n" \
        "4 - Sair")
        print('-' * 30)
        option = input('Digite o número de sua opção: ')

        # Adição de tarefa
        if option == "1":
            task = input('Adicione a tarefa: ')
            tasklist = addtask(tasklist,task)
            print('--> Tarefa adicionada.')
            print('-' * 30)

        # Amostra da lista
        elif option == "2":
            print("\n"f"{'   '* 2}LISTA DE TAREFAS")
            showlist(tasklist)

        # Remoção de tarefa com condições
        elif option == "3":
            task = input('Digite o número da tarefa que deseja remover: ')
            if not task.isnumeric():
                print("[!] Número inválido.")
            elif int(task) > len(tasklist):
                print("[!] Número inválido.")
            elif int(task) <= 0:
                print("[!] Número inválido.")
            else:
                task = int(task)
                deletetask(tasklist, task)
                print("--> Tarefa removida.")
                print('-' * 30)

        # Fim do loop
        elif option == "4":
            running = False

        else:
            print("[!] Opção inválida.")

# mostrar a lista em ordem numérica (int)
def showlist(tasklist):
    n = 1
    print("-" * 50)
    for task in tasklist:
        print(f"{n} - {task}")
        n += 1
    print("-" * 50)

#### Programa começa com a variável Start ####
Start = True

while Start == True: 
    print("\n=== Language - Idioma ===\n" \
    "1 - English\n" \
    "2 - Português")
    print('-' * 30)
    idiom = input("Type a number - Digite o número: ")

    # Ao escolher o idioma, coloquei uma repetição definida para rodar a função da lista de tarefas
    if idiom == "1":
        for n in range(1):
            menu_eng()
        Start = False
    elif idiom == "2":
        for n in range(1):
            menu_pt()
        Start = False
    else:
        print("[!] Invalid option. Opção inválida. [!]\n")
    