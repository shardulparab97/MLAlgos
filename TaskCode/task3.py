from collections import defaultdict
import heapq

class Worker:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.tasks_completed = set()
        self.current_task_completion_time = 0

class Task:
    def __init__(self, name, level_times):
        self.name = name
        self.levels = [(f"L{i}", t) for i, t in enumerate(level_times)]
        self.current_level = 0

class TaskScheduler:
    def __init__(self):
        self.tasks = {}
        self.workers = {}
        self.current_time = 0

    def assign_task(self, task_name, worker_name):
        task = self.tasks[task_name]
        level, time_required = task.levels[task.current_level]
        print(f"{self.current_time}: Assigning {worker_name} to {task_name} for {level}")
        time_taken = time_required / self.workers[worker_name].speed
        completion_time = self.current_time + time_taken
        self.workers[worker_name].current_task_completion_time = max(completion_time, self.workers[worker_name].current_task_completion_time)
        heapq.heappush(self.events, (completion_time, "complete", task_name, worker_name))

    def complete_task(self, task_name, worker_name):
        task = self.tasks[task_name]
        level, _ = task.levels[task.current_level]
        print(f"{self.current_time}: Worker {worker_name} finished Task {task_name} for {level}")
        self.workers[worker_name].tasks_completed.add(task_name)
        task.current_level += 1
        if task.current_level == len(task.levels):
            del self.tasks[task_name]

    def simulate(self):
        self.events = []
        for task_name, task in self.tasks.items():
            level, time_required = task.levels[0]
            heapq.heappush(self.events, (self.current_time, "assign", task_name, None))

        while self.events:
            time, action, *args = heapq.heappop(self.events)
            self.current_time = time
            if action == "assign":
                task_name, _ = args
                task = self.tasks[task_name]
                if task.current_level < len(task.levels):
                    level, _ = task.levels[task.current_level]
                    available_workers = [(worker.current_task_completion_time, worker_name) for worker_name, worker in self.workers.items() if task_name not in worker.tasks_completed]
                    if available_workers:
                        next_worker_completion_time, worker_name = min(available_workers)
                        if next_worker_completion_time <= self.current_time:
                            self.assign_task(task_name, worker_name)
            elif action == "complete":
                task_name, worker_name = args
                task = self.tasks[task_name]
                level, _ = task.levels[task.current_level]
                self.complete_task(task_name, worker_name)

        # Check if all tasks are completed
        if self.tasks:
            print("All tasks could not be completed.")
            return -1
        else:
            print(f"Total time taken: {self.current_time}")
            return self.current_time

    def add_task(self, task_name, level_times):
        self.tasks[task_name] = Task(task_name, level_times)

    def add_worker(self, worker_name, speed):
        self.workers[worker_name] = Worker(worker_name, speed)

if __name__ == "__main__":
    scheduler = TaskScheduler()

    # Adding tasks with time required for each level (L0, L1, L2)
    scheduler.add_task("A", [6, 4, 3])  # Task A takes 6 units of time for L0, 4 for L1, and 3 for L2
    scheduler.add_task("B", [4, 3, 2])  # Task B takes 4 units of time for L0, 3 for L1, and 2 for L2

    # Adding workers with their speeds
    scheduler.add_worker("X", 2)  # Speed of worker X is 2 units per timestamp
    scheduler.add_worker("Y", 3)  # Speed of worker Y is 3 units per timestamp
    scheduler.add_worker("Z", 1)  # Speed of worker Z is 1 unit per timestamp

    scheduler.simulate()
