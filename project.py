import datetime


class Employee:
    def __init__(self, first_name, last_name, position, hire_date, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.hire_date = hire_date
        self.salary = salary

    def update_position(self, new_position):
        self.position = new_position

    def update_salary(self, new_salary):
        self.salary = new_salary

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Position: {self.position}, Hire Date: {self.hire_date}, Salary: {self.salary}"


class Position:
    def __init__(self, title, access_level, salary):
        self.title = title
        self.access_level = access_level
        self.salary = salary

    def __str__(self):
        return f"Title: {self.title}, Access Level: {self.access_level}, Salary: {self.salary}"


class Payroll:
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate

    def calculate_net_salary(self, gross_salary):
        return gross_salary * (1 - self.tax_rate)


class PersonnelManager:
    def __init__(self):
        self.employees = []
        self.positions = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, last_name):
        for employee in self.employees:
            if employee.last_name.lower() == last_name.lower():
                self.employees.remove(employee)
                print(f"Employee {last_name} has been removed.")
                return
        print(f"Employee with last name {last_name} not found.")

    def update_employee(self, last_name, new_position=None, new_salary=None):
        for employee in self.employees:
            if employee.last_name.lower() == last_name.lower():
                if new_position:
                    employee.update_position(new_position)
                if new_salary:
                    employee.update_salary(new_salary)
                print(f"Employee {last_name} has been updated.")
                return
        print(f"Employee with last name {last_name} not found.")

    def add_position(self, position):
        if not any(pos.title == position.title for pos in self.positions):
            self.positions.append(position)
            print(f"Position {position.title} has been added.")
        else:
            print(f"Position {position.title} already exists.")

    def list_employees(self, sort_by=None):
        if sort_by == 'last_name':
            self.employees.sort(key=lambda emp: emp.last_name)
        elif sort_by == 'position':
            self.employees.sort(key=lambda emp: emp.position)
        elif sort_by == 'hire_date':
            self.employees.sort(key=lambda emp: emp.hire_date)

        for employee in self.employees:
            print(employee)

    def calculate_total_salary(self):
        return sum(employee.salary for employee in self.employees)


def print_menu():
    print("\nГоловне меню:")
    print("1. Переглянути список працівників")
    print("2. Додати нового працівника")
    print("3. Надати завдання працівнику")
    print("4. Змінити посаду або зарплату працівника")
    print("5. Звільнити працівника")
    print("6. Вийти")


def view_employee_list(personnel_manager):
    sort_by = input("Сортувати за (last_name, position, hire_date): ").strip()
    personnel_manager.list_employees(sort_by)


def add_employee(personnel_manager):
    first_name = input("Введіть ім'я працівника: ").strip()
    last_name = input("Введіть прізвище працівника: ").strip()
    position = input("Введіть посаду працівника: ").strip()
    hire_date = input("Введіть дату прийняття на роботу (YYYY-MM-DD): ").strip()
    salary = float(input("Введіть зарплату працівника: ").strip())

    new_employee = Employee(first_name, last_name, position, hire_date, salary)
    personnel_manager.add_employee(new_employee)
    print("\nПрацівника успішно додано.")


def assign_task_to_employee(personnel_manager):
    employee_last_name = input("Введіть прізвище працівника: ").strip()
    task = input("Введіть завдання для працівника: ").strip()

    for employee in personnel_manager.employees:
        if employee.last_name.lower() == employee_last_name.lower():
            employee.assign_task(task)
            return
    print("Працівника з таким прізвищем не знайдено.")


def update_employee_details(personnel_manager):
    employee_last_name = input("Введіть прізвище працівника: ").strip()
    update_type = input("Що бажаєте змінити (посаду/зарплату): ").strip().lower()

    if update_type == 'посаду':
        new_position = input("Введіть нову посаду: ").strip()
        personnel_manager.update_employee(employee_last_name, new_position=new_position)
    elif update_type == 'зарплату':
        new_salary = float(input("Введіть нову зарплату: ").strip())
        personnel_manager.update_employee(employee_last_name, new_salary=new_salary)
    else:
        print("Некоректний ввід. Повинно бути 'посаду' або 'зарплату'.")


def remove_employee(personnel_manager):
    employee_last_name = input("Введіть прізвище працівника: ").strip()
    personnel_manager.remove_employee(employee_last_name)


# Головна функція
def main():
    personnel_manager = PersonnelManager()

    while True:
        print_menu()
        option = input("Виберіть опцію: ").strip()
        if option == '1':
            view_employee_list(personnel_manager)
        elif option == '2':
            add_employee(personnel_manager)
        elif option == '3':
            assign_task_to_employee(personnel_manager)
        elif option == '4':
            update_employee_details(personnel_manager)
        elif option == '5':
            remove_employee(personnel_manager)
        elif option == '6':
            print("Дякую за використання нашої системи. До побачення!")
            break
        else:
            print("Некоректний ввід. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
