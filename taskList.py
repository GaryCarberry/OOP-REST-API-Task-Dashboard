from datetime import datetime

class Taskr:
    def __init__(self, todayList=None, tmrwList=None):#initialises the class variables
        self.todayList = []
        self.tmrwList = []

    def get_task_details(self, task_num, today=False):
        """Helper to get details for one task (name, priority, time limit)."""
        task = input(f"Enter task {task_num}: ")

        priority = input("Set priority (High / Medium / Low): ").capitalize()#intakes the priority of the choice
        while priority not in ("High", "Medium", "Low"):#error handling to ensure the correct input
            print("Invalid priority. Please enter High, Medium, or Low.")
            priority = input("Set priority (High / Medium / Low): ").capitalize()

        while True:
            time_limit = input("Enter a time limit or deadline (HH:MM) — or press Enter to skip: ")#gets the user to answer time if they choose
            if time_limit.strip() == "":#if the parsed time limit is empty then there will be no time limit in this case
                time_limit = "No time limit"
                break

            try:#try catch for the formatting of the answer
                user_time = datetime.strptime(time_limit, "%H:%M").replace(
                    year=datetime.now().year,
                    month=datetime.now().month,
                    day=datetime.now().day
                )
                if today and user_time < datetime.now():#checks if user is inputting a todolist ofr today and if so, makes sure that they dont choose a time gone by
                    print("That time has already passed. Please enter a future time.")
                    continue
                break
            except ValueError:
                print("Invalid time format. Please use HH:MM (e.g., 14:30).")

        return {"task": task, "priority": priority, "time_limit": time_limit}#returns a dictionary for each task

    def tskListmaker(self):
        answer = "yes"
        while "y" in answer.lower():# only uses y so if the user chooses a variation of ye, yeah or other types it can still catch that
            choice = input("Hi! Would you like to make a list for today or tomorrow? ").lower()

            if "tod" in choice:#same logic as "y" in answer
                no_tasks = int(input("How many tasks are you thinking of creating today? "))
                for i in range(no_tasks):
                    self.todayList.append(self.get_task_details(i + 1, today=True))#runs taskdetails for as many times as the user wants

            elif "tom" in choice:#tomorrow is simpler in this respect as the time limit wont apply but it still follows the same logic
                no_tasks = int(input("How many tasks are you thinking of creating tomorrow? "))
                for i in range(no_tasks):
                    self.tmrwList.append(self.get_task_details(i + 1))

            else:
                print("Invalid input, please try again.")

            answer = input("Would you like to add more tasks? (yes/no) ")

    def display_tasks(self):#final function for showing the user their input
        print("\nHere are your tasks:")
        if self.todayList:#if a list for today has been made...
            print("\nToday's Tasks:")
            for t in self.todayList:
                print(f"- {t['task']}  | Priority: {t['priority']} | Time Limit: {t['time_limit']}")
        if self.tmrwList:#if a list for today has been made...
            print("\nTomorrow's Tasks:")
            for t in self.tmrwList:
                print(f"- {t['task']}  | Priority: {t['priority']} | Time Limit: {t['time_limit']}")

    def tskFiler(self, weather=None):
        self.tskListmaker()
        self.display_tasks()

        save_answer = input("\nWould you like me to save these to notepad files? (yes/no) ").lower()#after displaying prompts the use if they want it in a file
        if save_answer == "yes":
            now = datetime.now()#creates a timestamp of when the request was made
            date_str = now.strftime("%d %m %Y")
            time_str = now.strftime("%H:%M")

            if self.todayList:
                with open('today.txt', 'w', encoding='utf-8') as f:#writes into a file called today.txt using the universal encoding ;utf-8'
                    f.write(f"Today's tasks {date_str} are here, made at {time_str}\n")
                    if weather:#if weather was called previously in taskhub it will also show up here
                        f.write("\nToday's weather forecast:\n")
                        f.write(f"{weather[0]}, {weather[1]}\n")
                        f.write(f"Temperature: {weather[2]}°C\n")
                        f.write(f"Condition: {weather[3]}\n")
                        f.write(f"Humidity: {weather[4]}%\n")
                        f.write(f"Wind Speed: {weather[5]} kph\n\n")

                    f.write("=" * 60 + "\n\n")# creates a line of '=' to improve the look of the file
                    for t in self.todayList:#writes out todaylists fore each item in todaylist
                        f.write(f"- {t['task']}\n")
                        f.write(f"  Priority: {t['priority']}\n")
                        f.write(f"  Time Limit: {t['time_limit']}\n")

                        if t['time_limit'] != "No time limit":#logic for comparing current time to deadline time
                            try:
                                limit_time = datetime.strptime(t['time_limit'], "%H:%M").replace(
                                    year=now.year, month=now.month, day=now.day
                                )
                                diff = (limit_time - now).total_seconds() / 3600#if the limit is within 2 hours from now it will need an alert
                                if 0 < diff <= 2:
                                    f.write(f"  Needs to be done within {diff:.1f} hour(s)!\n")
                            except ValueError:
                                f.write("  Invalid time format entered for this task.\n")

                        f.write("\n")

            if self.tmrwList:#tomorrow list is the same minus the time limit logic
                with open('tomorrow.txt', 'w', encoding='utf-8') as f:
                    f.write(f"Tomorrow's tasks {date_str} are here, made at {time_str}\n")
                    f.write("=" * 60 + "\n\n")
                    for t in self.tmrwList:
                        f.write(f"- {t['task']}\n")
                        f.write(f"  Priority: {t['priority']}\n")
                        f.write(f"  Time Limit: {t['time_limit']}\n")
                        f.write("\n")

            print("Tasks saved to notepad successfully!")
        else:
            print("Okay, nothing was saved. Have a great day!")

if __name__ == "__main__":
    taskr = Taskr()
    taskr.tskFiler()
    
