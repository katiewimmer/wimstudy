#Uncoded
from task import task

def run_dashboard():
    print_hello() #visually pleasing entry message
    all_tasks = get_tasks()
    greeting(all_tasks) #prompts for procductivity and time constraints

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

def get_tasks():
  """
  If user doesn't answer in the format of [yes, y, no, n], then this method forces the user to enter an appropriate answer and select a task

  Returns:
    List[task]: The list of tasks created by the user.
  """
  all_tasks = []

  while True:
    need = raw_input (u"\u001b[38;5;105m" + "\nHello, do you want to add a new task to your list? Answer 'yes' or 'no' \n" + u"\u001b[0m") 

    if need.lower() in ['n', 'no']: # if no new tasks are added, the study process will begin
      print(u"\u001b[38;5;105m" + "\nFantastic, lets get started!\n" + u"\u001b[0m")
      return all_tasks

    elif need.lower() in ['y', 'yes']: # allows for the user to input a task and will at it to a list
      name = raw_input(u"\u001b[38;5;105m" + "\nWhat is the name of the task? \n" + u"\u001b[0m")
      if len(name) == 0:
        print("Please enter a valid name")
        continue

      time = input( u"\u001b[38;5;105m" + "\nHow long do you think the task will take? (in minutes)? \n" + u"\u001b[0m")
      if time == 0:
        print("Please enter a valid time")
        continue

      category = raw_input(u"\u001b[38;5;105m" + "\nWhat class is this for?\n" + u"\u001b[0m")
      if len(category) == 0:
        print("Please enter a valid category")
        continue

      new_task = task(name, time, category)
      all_tasks.append(new_task)
    else:
      print("Please answer with 'yes' or 'no' \n")
      continue

# Takes user input about personal productivity. Based on productivity response, user is asked about time commitments. If there is available time, user has to choose a task to complete.""
def greeting(all_tasks):
  """
  Args:
    all_tasks (List[task]): The user's tasks
  """
  
  mood = input (u"\u001b[38;5;167m" + "How productive are you feeling today? On a scale of 1-10: \n" + u"\u001b[0m")

  if int(mood) in range(1,11):
    time = int(input(u"\u001b[38;5;167m" + "How much time do you have? In minutes: \n" + u"\u001b[0m"))
    if time > 0:
      print("\n Here are your current tasks: \n")
      print_tasks(all_tasks)
      need_recommendation = raw_input("\nDo you want to chose a task? \n")
      if need_recommendation.lower() in ['n', 'no']:
        class_preference = raw_input("\nDo you have a prefered class? \n")
        if class_preference.lower() in ['n','no']:
          recommend_task(all_tasks, time, mood)
        elif class_preference.lower() in ['y', 'yes']:
          pref = raw_input("\nWhat class do you prefer?\n")
          recommend_task(all_tasks, time, mood, pref)
        else:
          print("\nPlease answer yes or no\n")
          greeting()
      return
  else:
    print("There was an error with your input. Please try again!\n")
    greeting(all_tasks)

def print_tasks(list_of_tasks):
  print("The available tasks are: \n")
  for x in list_of_tasks:
    print ("TASK: " + x.get_name())
    print ("TIME: " + str(x.get_time()))
    print ("CLASS: " + x.get_category() + '\n')

def recommend_task(list_of_tasks, time, productivity, class_pref):
  for x in list_of_tasks:
      if x.get_time() == time:
        print("\nHere is the recommended task: \n" + x.get_name() + " for " + x.get_category())
        exit()
      elif class_pref in [x.get_category()]:
        print("\nHere is the recommended task: \n" + x.get_name() + " for " + x.get_category())
      elif x.get_time() < time: 
        print("\nHere is the recommended task: \n" + x.get_name() + " for " + x.get_category())
        exit()
      elif mood > 7 & x.get_time() > time:
        print("\nHere is the recommended task: \n" + x.get_name() + " for " + x.get_category())
      else:
        print("\nNo task to recommend, please manually select")
        select_task()

def select_task():

  '''
    Need to print the tasks with numbers than allow the user to select a
    specific task by entering a number
  '''

if __name__ == "__main__":
    run_dashboard()
    list_of_tasks = []
    time = 0
    mood = 0
