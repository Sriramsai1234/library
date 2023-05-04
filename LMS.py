import os
import pickle


class Customer:
    def __init__(self, cid, cname, bname, ccontact, cfine):
        self.cid = cid
        self.cname = cname
        self.bname = bname
        self.ccontact = ccontact
        self.cfine = cfine


class LibraryManagement:
    def __init__(self):
        self.customers = {}


    def add_customer(self):
        while True:
            try:
                cid = int(input("Enter Customer ID: "))
                if cid <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid Customer ID, Please enter a valid ID number")

        while True:
            cname = input("Enter Customer Name: ")
            if not cname.isalpha():
                print("Invalid Customer Name, Name must only contain alphabetic characters.")
            else:
                break

        bname = input("Enter book name")

        while True:
            try:
                ccontact = int(input("Enter customer contact number: "))
                if len(str(ccontact)) != 10:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input, Contact number must be a 10 digit number.")

        while True:
            try:
                cfine = float(input("Enter number of days delay: "))
                if cfine < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input, Please enter a positive number")

        cus = Customer(cid, cname, bname, ccontact, cfine)
        self.customers[cid] = cus
        self.save_data()
        print("Record Added")

    def show_customers(self):
        print("ID\t Name\t Address\t\t ContactNo\t\t Hourly Wage")
        for cus in self.customers.values():
            print(f"{cus.cid}\t {cus.cname}\t {cus.bname}\t {cus.ccontact}\t {cus.cfine}")

    def search_customers(self):
        i = input("Enter the ID to be searched:")
        cus = self.customers.get(int(i))
        if cus:
            print(f"{cus.cid}\t {cus.cname}\t {cus.bname}\t {cus.ccontact}\t {cus.cfine}")
        else:
            print("Record not found")

    def delete_customers(self):
        i = input("Enter the ID to remove from file:")
        if int(i) in self.customers:
            del self.customers[int(i)]
            self.save_data()
            print("Record deleted")
        else:
            print("Record not found")

    def update_customer(self):
        cid = input("Enter customer ID: ")
        cus = self.customers.get(int(cid))
        if cus:
            while True:
                cname = input("Enter customer name: ")
                if not cname.isalpha():
                    print("Invalid input. Name must only contain alphabetic characters.")
                else:
                    break
            bname = input("Enter book name")

            while True:
                try:
                    ccontact = int(input("Enter customer contact number: "))
                    if len(str(ccontact)) != 10:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Contact number must be a 10-digit integer.")

            while True:
                try:
                    cfine = float(input("Enter number of days delay: "))
                    if cfine < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter a positive number of days")

            cus.cname = cname
            cus.bname = bname
            cus.ccontact = ccontact
            cus.cfine = cfine
            self.save_data()
            print("Record updated")
        else:
            print("Record not found")
    def calculate_fine(self):
        cid = input("Enter customer ID: ")
        cus = self.customers.get(int(cid))
        if cus:
          while True:
            try:
              day_delay = float(input("Enter number of delayed : "))
              if day_delay < 0:
                raise ValueError
              break
            except ValueError:
              print("Invalid input. Please enter non negative worked.")
          tfine = day_delay * 2
          print(f"customer ID: {cus.cid}\nCustomer Name: {cus.cname}\nTotal Fine:${tfine}")
        else:
          print("Record not found")

    def save_data(self):
        with open('data.txt', 'w') as f:
            # code to write the data to the file
            pass

    def menu(self):
      while(True):
        password = input("Enter a password:  ")
        if password=="python":
          print("Welcome")
          break
        else:
          print("Incorrect password try again and chances left")
      while True:
        print("\nMENU")
        print("1. Add Customer")
        print("2. Show Customer")
        print("3. Search Customer")
        print("4. Delete Customer")
        print("5. Update Customer")
        print("6. Calculate Fine")
        print("7. Exit")
        try:
          choice = int(input("Enter your choice: "))
        except ValueError:
          print("Invalid input. Please enter a valid choice.")
          continue
        
        if choice == 1:
          self.add_customer()
        if choice == 2:
          self.show_customers()
        if choice == 3:
          self.search_customers()
        if choice == 4:
          self.delete_customers()
        if choice == 5:
          self.update_customer()
        if choice == 6:
          self.calculate_fine()
        if choice == 7:
          print("End of the session")
          break  

if __name__ == "__main__":
  cus = LibraryManagement()
  cus.menu() 
