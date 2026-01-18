from Student import Student

class Main:
    @staticmethod
    def show_all_students():
        with open('Student.txt', 'r') as file:
            for i in file:
                print(i)


    @staticmethod
    def main():
        while True:
            print("\n1. Enroll New Student")
            print("2. Show Enrolled Students Details")
            print("3. Press any other key to exit")

            choice = input("Enter your choice: ")

            if choice == "1":

                name = input("Enter your name: ")
                roll = input("Enter your roll: ")
                password = input("Enter your password: ")
                student = Student(name, roll, password)

                while True:
                    course = input("Enter your course {or done if finished}: ")
                    if course == "done":
                        break
                    else:
                        student.course.add_courses(course)

                student.write_to_file()

            elif choice == "2":
                Main.show_all_students()

            else:
                print("Exiting...")
                break

if __name__ == "__main__":
    Main.main()

