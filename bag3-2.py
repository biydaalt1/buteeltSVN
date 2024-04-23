//6:10
class Employee:
    def __init__(self, name, years_worked):
        self.name = name
        self.years_worked = years_worked

def transfer_employees_to_backup(employees):
    backup_employees = []
    remaining_employees = employees.copy() 
    for employee in employees:
        if employee.years_worked >= 10:
            backup_employees.append(employee)
            remaining_employees.remove(employee)  
            print(f"УБ серверлүү {employee.name}-ийн мэдээлийг шилжүүлж байна...")
    return backup_employees, remaining_employees


def main():
    employees = [
        Employee("Бат", 12),
        Employee("Болд", 7),
        Employee("Буянаа", 15),
        Employee("Анхаа", 8),
        Employee("Төөгөө", 10),
        Employee("Билгүүнээ", 1),
        Employee("Базраа", 17),
        Employee("Эрдэнэ", 20),
    ]

    print("Дарханд сервер дээр байгаа ажилчид:")
    print("+----------------+------------+")
    print("|     Нэр        |   Ажилласан Жил|")
    print("+----------------+------------+")
    for employee in employees:
        print(f"| {employee.name:<14}| {employee.years_worked:^10}|")
    print("+----------------+------------+")

    backup_employees, remaining_employees = transfer_employees_to_backup(employees)

    print("\nУБ серверт байгаа ажилчид (10+ жил ажилласан):")
    print("+----------------+------------+")
    print("|     Нэр        |   Ажилласан Жил|")
    print("+----------------+------------+")
    for employee in backup_employees:
        print(f"| {employee.name:<14}| {employee.years_worked:^10}|")
    print("+----------------+------------+")

    print("\nДархан сервер дээр үлдсэн ажилчид:")
    print("+----------------+------------+")
    print("|     Нэр        |   Ажилласан Жил|")
    print("+----------------+------------+")
    for employee in remaining_employees:
        print(f"| {employee.name:<14}| {employee.years_worked:^10}|")
    print("+----------------+------------+")

if __name__ == "__main__":
    main()
//6:35
