
class task_list:
    def __init__(self,name,time,category):
        self.name=name
        self.time=time
        self.category=category
        
    def display_full_task(self):
        print("Name:",str(self.name),"\n")
        print("Time:",str(self.time),"\n")
        print("Category:",str(self.category),"\n")
    
    def get_name(self):
        return self.name

    def get_time(self):
        return self.time

    def get_catefory(self):
        return self.category

num_tasks = int(input(f'How many tasks would you like to create? \n'))
list_of_tasks = []

for x in range(0, num_tasks):
    n = input("\ninput name: \n") #Customize Questions
    t = input("input time: \n")
    c = input("input category: \n")

    task=task_list(n,t,c)

    list_of_tasks.insert(x, task.name)

print("\nList of Tasks:", list_of_tasks)

## Additional methods that don't have to do with the code when you run it as of now   
def get_tasks():
    print("The available tasks are:")
    print(task_list)

def recommend_task():
    '''
      Need to print the tasks with numbers than allow the user to select a 
      specific task by entering a number
    '''
    for x in range (0, len(task_list)):
      task_list.display_full_task(x)

