import task_list
#Uncoded
def run_dashboard():
    print_hello() #visually pleasing entry message
    get_action()

def print_hello():
  print("""
===================================================================
                            Welcome to

       __      __ ___  __  __  ___  _____  _   _  ___  __   __
       \ \    / /|_ _||  \/  |/ __||_   _|| | | ||   \ \ \ / /
        \ \/\/ /  | | | |\/| |\__ \  | |  | |_| || |) | \   / 
         \_/\_/  |___||_|  |_||___/  |_|   \___/ |___/   |_|  


===================================================================
""")

def get_action():

  need = raw_input (u"\u001b[38;5;105m" + "Hello, do you want to add a new task to your list? Answer 'yes' or 'no' \n" + u"\u001b[0m") 
  
  # If user doesn't answer in the format of [yes, y, no, n], then this method forces the user to enter an appropriate answer and select a task
  if need.lower() in ['n', 'no']: # if no new tasks are added, the study process will begin
    print(u"\u001b[38;5;105m" + "\nFantastic, lets get started!\n" + u"\u001b[0m")
    greeting() #prompts for procductivity and time constraints
    exit()
  elif need.lower() in ['y', 'yes']: # allows for the user to input a task and will at it to a list
    name = raw_input("What is the name of the task? \n")
    if len(name) != 0:
      time = input("How long do you think the task will take? (in minutes)? \n")
    if time != 0:
      category = raw_input("What class is this for? \n")
    else:
      print("Please enter a valid phrase or number greater than 0")
    add_task_to_list(task_list(name, time, category))
    get_action()
  else:
    print("Please answer with 'yes' or 'no' \n")
    get_action()

# Takes user input about personal productivity. Based on productivity response, user is asked about time commitments. If there is available time, user has to choose a task to complete.""
def greeting():
  
  mood = input (u"\u001b[38;5;167m" + "How productive are you feeling today? On a scale of 1-10: \n" + u"\u001b[0m")

  if int(mood) in range(0,10):
    time = int(input(u"\u001b[38;5;167m" + "How much time do you have? In minutes: \n" + u"\u001b[0m"))
    if time > 0:
      print("Please choose a task: \n")
     # task_list.print_tasks()
  else:
    print("There was an error with your input. Please try again!\n")
    greeting()


 # def recommend_task
  '''
    Need to print the tasks with numbers than allow the user to select a
    specific task by entering a number
  '''
 #   for x in task_list

 #      display_full_task(x)

#    task_num = input(f' "Please enter the number of the task you would like: /n {get_tasks()}'')
#    for x in tasks
#    task_num = input(f' "Please enter the number of the task you would like: /n {get_tasks()}'')
#    for x in tasks

if __name__ == "__main__":
    run_dashboard()
