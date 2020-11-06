def print_tasks():
    print("The available tasks are:")
    for t in list_of_tasks:
         print(display_full_task(t))
        
'''
for x in range(0, num_tasks):
    n = input("\ninput name: \n") #Customize Questions
    t = input("input time: \n")
    c = input("input category: \n")

    task=task_list(n,t,c)

    list_of_tasks.insert(x, task.name)

print("\nList of Tasks:", list_of_tasks)
'''
## Additional methods that don't have to do with the code when you run it as of now

def recommend_task():
    '''
      Need to print the tasks with numbers than allow the user to select a
      specific task by entering a number
    '''
    for x in range (0, len(task_list)):
      task_list.display_full_task(x)
