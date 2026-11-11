from tasks import show_tasks, save_tasks
from dotenv import load_dotenv
import os


load_dotenv()

name = input("enter your name: ")
print("hello", name, "welcome to personal task manager")

admin_mode = input("do you want to enter admin mode (yes/no)? ")
if admin_mode == "yes":
    admin_password = input("enter admin password: ")
    if admin_password == os.getenv("admin_pass"):
        print("admin mode activated")
    else:
        print("wrong password")


tasks = []
count = int(input("how many tasks do you want to add? : "))
for i in range(count):
    task = input("enter a task: ")
    priority = input("enter priority(low/medium/high): ").lower()
    task = {
        "name" : task,
        "priority" : priority
    }

    tasks.append(task)


show_tasks(tasks)
save_tasks(tasks)