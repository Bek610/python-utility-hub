# todo_list.py
# Project 2: To-Do List App
# The user can add, view, finish, edit and delete tasks.
# Tasks are saved in a text file (tasks.txt), so they are still there next time.

from helpers import print_title, get_whole_number, get_text, ask_yes_no

FILE_NAME = "tasks.txt"


class TodoList:

    def __init__(self):
        # Each task is a dictionary like:
        # {"title": "Study", "priority": "high", "done": False}
        # All tasks are kept in this list.
        self.tasks = []
        self.load_tasks()

        self.menu = {
            "1": "Show tasks",
            "2": "Add a task",
            "3": "Mark a task as done",
            "4": "Edit a task",
            "5": "Delete a task",
            "6": "Search tasks",
            "7": "Show tasks by priority",
            "8": "Delete all finished tasks",
            "9": "Statistics",
            "0": "Back to main menu",
        }

    # ---------- saving and loading the file ----------

    def load_tasks(self):
        # Each line in the file looks like:  done|priority|title
        # Example:                            no|high|Finish Python report
        try:
            file = open(FILE_NAME, "r")
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split("|", 2)
                if len(parts) != 3:
                    continue  # skip a broken line
                task = {
                    "done": parts[0] == "yes",
                    "priority": parts[1],
                    "title": parts[2],
                }
                self.tasks.append(task)
            file.close()
        except FileNotFoundError:
            # The first time the program runs there is no file yet
            self.tasks = []

    def save_tasks(self):
        try:
            file = open(FILE_NAME, "w")
            for task in self.tasks:
                if task["done"]:
                    done = "yes"
                else:
                    done = "no"
                file.write(done + "|" + task["priority"] + "|" + task["title"] + "\n")
            file.close()
        except OSError:
            print("Error: could not save the tasks.")

    # ---------- showing tasks ----------

    def print_task(self, number, task):
        if task["done"]:
            box = "[X]"
        else:
            box = "[ ]"
        print(str(number) + ". " + box + " " + task["title"] + "  (" + task["priority"] + ")")

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("Your list is empty.")
            return False
        number = 1
        for task in self.tasks:
            self.print_task(number, task)
            number = number + 1
        return True

    # ---------- asking which task ----------

    def pick_task(self, action):
        # Show the list and ask for a task number.
        # Returns the position in the list (0, 1, 2...) or -1 if there is a problem.
        if not self.show_tasks():
            return -1
        number = get_whole_number("Which task number do you want to " + action + "? ")
        try:
            if number < 1:
                raise IndexError
            task = self.tasks[number - 1]  # this line raises IndexError if the number is too big
            return number - 1
        except IndexError:
            print("Error: there is no task number " + str(number) + ".")
            return -1

    def pick_priority(self):
        print("Priority: 1 = high, 2 = medium, 3 = low")
        while True:
            choice = input("Choose priority: ").strip()
            if choice == "1":
                return "high"
            elif choice == "2":
                return "medium"
            elif choice == "3":
                return "low"
            else:
                print("Error: please type 1, 2 or 3.")

    # ---------- the actions ----------

    def add_task(self):
        title = get_text("Task description: ")
        priority = self.pick_priority()
        task = {"title": title, "priority": priority, "done": False}
        self.tasks.append(task)
        self.save_tasks()
        print("Added: " + title)

    def finish_task(self):
        index = self.pick_task("mark as done")
        if index != -1:
            self.tasks[index]["done"] = True
            self.save_tasks()
            print("Well done! Finished: " + self.tasks[index]["title"])

    def edit_task(self):
        index = self.pick_task("edit")
        if index != -1:
            new_title = get_text("New description: ")
            self.tasks[index]["title"] = new_title
            self.save_tasks()
            print("Changed to: " + new_title)

    def delete_task(self):
        index = self.pick_task("delete")
        if index != -1:
            title = self.tasks[index]["title"]
            if ask_yes_no("Delete '" + title + "'?"):
                self.tasks.pop(index)
                self.save_tasks()
                print("Deleted.")

    def search_tasks(self):
        word = get_text("Word to search for: ").lower()
        found = 0
        number = 1
        for task in self.tasks:
            if word in task["title"].lower():
                self.print_task(number, task)
                found = found + 1
            number = number + 1
        print("Found " + str(found) + " task(s).")

    def show_by_priority(self):
        # A tuple, because the order of priorities never changes
        priorities = ("high", "medium", "low")
        for priority in priorities:
            print("--- " + priority.upper() + " ---")
            count = 0
            number = 1
            for task in self.tasks:
                if task["priority"] == priority:
                    self.print_task(number, task)
                    count = count + 1
                number = number + 1
            if count == 0:
                print("(none)")

    def delete_finished(self):
        new_list = []
        for task in self.tasks:
            if not task["done"]:
                new_list.append(task)
        removed = len(self.tasks) - len(new_list)
        self.tasks = new_list
        self.save_tasks()
        print("Deleted " + str(removed) + " finished task(s).")

    def statistics(self):
        total = len(self.tasks)
        done = 0
        for task in self.tasks:
            if task["done"]:
                done = done + 1
        not_done = total - done
        print("Total tasks: " + str(total))
        print("Done:        " + str(done))
        print("Not done:    " + str(not_done))
        if total > 0:
            percent = done * 100 // total
            print("Progress:    " + str(percent) + "%")

    # ---------- the menu ----------

    def run(self):
        while True:
            print_title("To-Do List")
            for key in self.menu:
                print(key + ". " + self.menu[key])
            choice = input("Choose an option: ").strip()

            if choice == "0":
                print("Going back to the main menu... (your tasks are saved)")
                break
            elif choice == "1":
                print_title("Your Tasks")
                self.show_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.finish_task()
            elif choice == "4":
                self.edit_task()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                self.search_tasks()
            elif choice == "7":
                self.show_by_priority()
            elif choice == "8":
                self.delete_finished()
            elif choice == "9":
                self.statistics()
            else:
                print("Error: '" + choice + "' is not on the menu.")


# Run the to-do list by itself: python3 todo_list.py
if __name__ == "__main__":
    todo = TodoList()
    todo.run()
