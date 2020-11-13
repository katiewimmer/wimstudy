
def recommend_task(mood, time, task_list):
    for i, x in enumerate(0, len(task_list)):
      print(str(i+1) + ") ")
      task_list.display_full_task(x)

def recommend_study_strat(mood):
    '''
    Given the user productivity, recommend a study strategy 

    Args:
      Mood: int showing productivity of the user
      Time: int of number of minutes allocated to this task
      Task: given task
    Returns:
      string of the recommended study strategy
    '''

    '''
    Feel free to change these bounds, I just sort of did them by how long
    the focus time takes for each method
    '''
    if time <= 45:
        if mood <= 3:
            return 'Brain-Break Method'
        else:
            return 'Pomodoro Method'
    elif time < 120:
        if mood <= 3:
            return 'Brain-Break Method'
        else:
            return 'The Abby Method'
    elif 120<=time<360:
        if mood <= 3:
            return 'Pomodoro Method'
        elif 3 < mood < 8:
            return 'The Abby Method'
        elif mood >= 8:
            return 'The Sima Method'
    elif time>=360:
        if mood <= 3:
            return 'The Koki Method'
        else:
            return 'Brain-Break Method'


    

