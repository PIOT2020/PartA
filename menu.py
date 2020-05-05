from database_utils import DatabaseUtils

class Menu:
    def main(self):
        with DatabaseUtils() as db:
            db.createDatabase()
        self.runMenu()

    def runMenu(self):
    
        selection = 0
        print()

        if(selection == "1"):
            self.listPeople()
        elif(selection == "2"):
            self.insertPerson()
        elif(selection == "3"):
            print("Goodbye!")
        else:
            print("Invalid input - please try again.")

    def listPeople(self):
        print("--- People ---")
        print("{:<15} {}".format("Person ID", "Name"))
        with DatabaseUtils() as db:
            for person in db.getPeople():
                print("{:<15} {}".format(person[0], person[1]))

    def insertPerson(self):
        print("--- Insert Person ---")
        name = raw_input("Enter the person's name: ")
        with DatabaseUtils() as db:
            if(db.insertPerson(name)):
                print("{} inserted successfully.".format(name))
            else:
                print("{} failed to be inserted.".format(name))

if __name__ == "__main__":
    Menu().main()
