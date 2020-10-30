
#Uncoded
def run_dashboard():
  '''
  Will open and allow access to the three tools
  '''
  greeting()

# Takes user input about personal productivity. Based on productivity response, user is asked about time commitments. If there is available time, user has to choose a task to complete.""
def greeting():
  
  mood = input ("How productive are you feeling today? On a scale of 1-10: \n")

  if int(mood) in range(0,10):
    time = int(input ("How much time do you have? In minutes: \n"))
    if time > 0:
      print("Please choose a task: \n")
      task_list.get_tasks()
  else:
    print("There was an error with your input. Please try again!\n")
    greeting()
  
  
  # If user doesn't answer in the format of [yes, y, no, n], then this method forces the user to enter an appropriate answer and select a task
  def get_action():

    need_task = input("Do you want to select a specific task? \n")

    if need_task.lower() in ['n', 'no']:
        print("Fantastic, lets get started!\n")
        study()
        exit()
    elif need_task.lower() in ['y', 'yes']:
        recommend_task()
    else:
        print("Please answer yes or no.\n")
        get_action()
        
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

def study():
  return #spacer
  
#def show_tasks():
   
  #returns the list of stored tasks

if __name__ == "__main__":
    run_dashboard()

  
