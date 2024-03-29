"""

User
Write code and running test for this problem:

Here at Scale, customers send us collections of data over the course of each week. Let's call each unit of data a
“task”. We send these tasks to our workforce for labeling. When these tasks are labeled, we send them back to the
customer. Each task goes through three sequential stages: L0 → L1 → L2 Workers are given task stages to work on. A
task is only “complete” when it reaches the L2 stage and work is finished on the L2 stage. *Write a system that
simulates the environment and runs until all tasks are completed. Do not worry about runtime, we are looking for
correctness. On every timestamp where activity happens: Print out the timestamp and all the activities that happened
(worker assignment/completion). *At the end print out the total number of time taken to complete the simulation
Notes: - There is a 1:1 mapping between task stages and workers working on a task stage (i.e. TaskX L1 can only have
1 worker at one time that worker cannot be working on anything else). - A worker can only work on a task if the
worker has never worked on that task before. - For Hello! The content hidden in this post requires a score higher
than 188 to be viewed. Your current score is 0. Use VIP to instantly unlock reading rights or view other ways to earn
points.


finished Task A for L0 Worker Y finished Task B for L0 Assigning Y to Task A for L1 Assigning X to Task B for L1 2
Worker Z finished Task A for L2 Assigning Z to Task B for L2 4 Worker Z finished Task B for L2 Total time taken """

class Worker:
    def __init__(self, name):
        self.name = name
        self.current_task = None

    def assign_task(self, task):
        self.current_task = task

    def complete_task(self):
        task_name = self.current_task.name
        stage = self.current_task.stage
        print(f"Worker {self.name} finished {task_name} for {stage}")
        self.current_task = None


class Task:
    def __init__(self, name, stage):
        self.name = name
        self.stage = stage
        self.assigned_worker = None

    def assign_worker(self, worker):
        self.assigned_worker = worker
        print(f"Assigning {worker.name} to {self.name} for {self.stage}")


class Simulation:
    def __init__(self):
        self.tasks = [Task("Task A", "L0"), Task("Task B", "L0")]
        self.workers = [Worker("Y"), Worker("X"), Worker("Z")]
        self.total_time = 0

    def simulate(self):
        while not self.is_simulation_complete():
            self.total_time += 1
            for task in self.tasks:
                if task.stage == "L0" and task.assigned_worker is None:
                    worker = self.get_available_worker()
                    if worker:
                        task.assign_worker(worker)
                        worker.assign_task(task)
                elif task.stage == "L1" and task.assigned_worker and task.assigned_worker.current_task is None:
                    worker = self.get_available_worker()
                    if worker:
                        task.assign_worker(worker)
                        worker.assign_task(task)
                elif task.stage == "L2" and task.assigned_worker:
                    task.assigned_worker.complete_task()

    def get_available_worker(self):
        for worker in self.workers:
            if worker.current_task is None:
                return worker
        return None

    def is_simulation_complete(self):
        for task in self.tasks:
            if task.stage != "L2" or task.assigned_worker is None:
                return False
        return True

    def print_results(self):
        print(f"Total time taken: {self.total_time} min")


if __name__ == "__main__":
    simulation = Simulation()
    simulation.simulate()
    simulation.print_results()
