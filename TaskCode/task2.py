# Follow up: every worker takes some time to complete task

class Worker:
    def __init__(self, name, task_completion_time):
        self.name = name
        self.current_task = None
        self.task_completion_time = task_completion_time

    def assign_task(self, task):
        self.current_task = task

    def complete_task(self):
        task_name = self.current_task.name
        stage = self.current_task.stage
        print(f"Worker {self.name} finished {task_name} for {stage} at time {self.current_task.time}")
        self.current_task = None


class Task:
    def __init__(self, name, stage, time):
        self.name = name
        self.stage = stage
        self.assigned_worker = None
        self.time = time

    def assign_worker(self, worker):
        self.assigned_worker = worker
        print(f"Assigning {worker.name} to {self.name} for {self.stage}")


class Simulation:
    def __init__(self):
        self.tasks = [Task("Task A", "L0", 0), Task("Task B", "L0", 0)]
        self.workers = [Worker("Y", 2), Worker("X", 3), Worker("Z", 4)]
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
                    self.total_time += task.time

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
