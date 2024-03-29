# Follow up: every worker takes some time to complete task

from collections import defaultdict
import heapq

class Worker:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.tasks_completed = set()

class Task:
    def __init__(self, name, stage):
        self.name = name
        self.stage = stage

class TaskScheduler:
    def __init__(self):
        self.tasks = defaultdict(list)
        self.workers = {}
        self.current_time = 0

    def assign_task(self, task_name, worker_name):
        task = self.tasks[task_name][0]
        if task.stage == "L0":
            print(f"{self.current_time}: Assigning {worker_name} to {task_name} for L1")
            time_taken = self.workers[worker_name].speed * 1
            heapq.heappush(self.events, (self.current_time + time_taken, "assign", task_name, worker_name, "L1"))
        elif task.stage == "L1":
            print(f"{self.current_time}: Assigning {worker_name} to {task_name} for L2")
            time_taken = self.workers[worker_name].speed * 1
            heapq.heappush(self.events, (self.current_time + time_taken, "assign", task_name, worker_name, "L2"))

    def complete_task(self, task_name, worker_name):
        task = self.tasks[task_name][0]
        print(f"{self.current_time}: Worker {worker_name} finished Task {task_name} for {task.stage}")
        time_taken = self.workers[worker_name].speed * 1
        heapq.heappush(self.events, (self.current_time + time_taken, "complete", task_name, worker_name))

    def simulate(self):
        self.events = []
        for task_name, tasks in self.tasks.items():
            task = tasks[0]
            heapq.heappush(self.events, (self.current_time, "assign", task_name, None, "L0"))

        while self.events:
            time, action, *args = heapq.heappop(self.events)
            self.current_time = time
            if action == "assign":
                task_name, worker_name, stage = args
                if task_name not in self.workers[worker_name].tasks_completed:
                    if self.tasks[task_name][0].stage == stage:
                        self.assign_task(task_name, worker_name)
            elif action == "complete":
                task_name, worker_name = args
                if task_name not in self.workers[worker_name].tasks_completed:
                    self.complete_task(task_name, worker_name)

        # Check if all tasks are completed
        if any(tasks for tasks in self.tasks.values()):
            print("All tasks could not be completed.")
            return -1
        else:
            print(f"Total time taken: {self.current_time}")
            return self.current_time

    def add_task(self, task_name, stage):
        self.tasks[task_name].append(Task(task_name, stage))

    def add_worker(self, worker_name, speed):
        self.workers[worker_name] = Worker(worker_name, speed)

if __name__ == "__main__":
    scheduler = TaskScheduler()

    scheduler.add_task("A", "L0")
    scheduler.add_task("B", "L0")
    scheduler.add_worker("X", 2)  # Speed of worker X is 2 units per timestamp
    scheduler.add_worker("Y", 3)  # Speed of worker Y is 3 units per timestamp
    scheduler.add_worker("Z", 1)  # Speed of worker Z is 1 unit per timestamp

    scheduler.simulate()
