
class task:
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

    def get_category(self):
        return self.category

