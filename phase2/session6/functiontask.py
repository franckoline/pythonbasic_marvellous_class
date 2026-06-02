#1. Material cost.
def calculate_material_cost(material, quantity):
    p_cement = 14500
    p_sand = 75000
    p_gravel = 90000

    if material == "cement":
        material_cost = p_cement * quantity
        print(f"The total cost for cement is {material_cost}NGN")
    elif material == "sand":
        material_cost = p_sand * quantity
        print(f"The total cost for sand is {material_cost}NGN")
    elif material == "gravel":
        material_cost = p_gravel * quantity
        print(f"The total cost for gravel is {material_cost}NGN")
    else:
        print("Material unavailable.")

calculate_material_cost("gravel", 23)

# 2.Project Timeline Estimator
def estimate_project_days():
    task_list = []
    days = []
    total = 0
    num = int(input("\nHow many tasks do you have for the project: "))

    for i in range(num):
        task = input(f"Enter the {i + 1} task: ")
        task_list.append(task)

    for i in range(num):
        day = int(input(f"Enter estimated duration in days for {task_list[i]}: "))
        days.append(day)

    for day in days:
        total = total + day
    print(f"\n{total} days is needed to complete this project.")


estimate_project_days()

#3.Worker allocator

def allocate_workers(total_tasks, workers_available):
    if total_tasks % workers_available == 0:
        work_per_person = total_tasks / workers_available
        print(f"each worker will handle {work_per_person} task(s)")
    elif total_tasks % workers_available != 0:
        work_per_person = total_tasks // workers_available
        print(f"Each worker will handle {work_per_person} task(s)")
        remain = total_tasks - work_per_person * workers_available
        print(f"There will be {remain} task(s) left unassigned")




total_tasks = int(input("\nHow many task are available? "))
workers_available = int(input("How many workers are available? "))

allocate_workers(total_tasks, workers_available)

#. 4.Construction Budget Planner
def budget_summary(labor_cost, materials_cost, equipment_rental):
    total = labor_cost + materials_cost + equipment_rental
    print(f"\nLabour cost: {labor_cost}NGN ")
    print(f"materials cost: {materials_cost}NGN ")
    print(f"equipment rental: {equipment_rental}NGN ")
    print(f"The total project budget is {total}NGN")


budget_summary(50000, 12000, 30000)

#7. Worker Attendance Percentage

def attendance_percentage(present_days, total_days):
    attendance_rate = (present_days / total_days) * 100
    return attendance_rate

p_days =int(input("\nHow many days where you present: "))
print(f"This worker had an attendance rate of {attendance_percentage(p_days, 6): .2f} percent.")





