from student_registry import Student, StudentRegistry

def main():
    registry = StudentRegistry()

    while True:
        print("\nStudent Registry")
        print("1. Add student")
        print("2. Remove student")
        print("3. Find student")
        print("4. List students")
        print("5. Exit")

        option = input("Seleccione una opción: ")

        if option == "1":
            student_id = input("Ingrese el ID del estudiante: ")
            name = input("Ingrese el nombre del estudiante: ")
            age = input("Ingrese la edad del estudiante: ")
            student = Student(student_id, name, age)
            registry.add_student(student)

        elif option == "2":
            student_id = input("Ingrese el ID a eliminar: ")
            registry.remove_student(student_id)

        elif option == "3":
            student_id = input("Ingrese el ID a buscar: ")
            registry.find_student(student_id)

        elif option == "4":
            registry.list_students()

        elif option == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":

    main()
