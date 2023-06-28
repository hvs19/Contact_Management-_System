#CONTACT_MANAGEMENT_SYSTEM BY HARSH VARDHAN SINGH
import os
import csv
import datetime
from time import strftime

#creating title for all pages
def title():
   line_1 = "------------------------------------------"
   Tq     = " Contacts Management System"
   line_2 = "------------------------------------------"
   print(line_1.center(130))
   print(Tq.center(130))
   print(line_2.center(130))

#creating class
class contact_numbers:
   contact_fields = ["Name", "Mobile_No"]
   contact_database = "contacts.csv"
   contact_data = []

   #writing create() function to create contacts
   def create(self):
    os.system('cls')
    title()
    print("    Create Contact:")
    print("    ---------------")
    print("")
    for fields in self.contact_fields:
      contact_details = input("    Enter " + fields + ":")
      print("")
      self.contact_data.append(contact_details)
      
    Date = datetime.datetime.today()
    d = Date.strftime("%B %d %Y")
    self.contact_data.append(d)

    with open(self.contact_database, 'a') as file:
      write = csv.writer(file)
      write.writerows([self.contact_data])
    self.contact_data=[]
    print("")
    print("Contact is created successfully".center(129))
    #os.system('mpg123' + 'Correct sound 2.mp3')
    
    print("\n")
    #input("\t   Press enter key to continue..")
    
   #writing view() function to see created contacts 
   def view(self):
      os.system('cls')
      title()
      print("Contacts:".center(10))
      print("---------".center(10))
      print("")
      count = 0
      with open(self.contact_database, 'r') as file:
       read = csv.reader(file)
       for data1 in read:
         if len(data1) > 0:
            count = count + 1
       print("Total Contacts: ", count)
       print("")

      with open(self.contact_database, 'r') as file:
       read = csv.reader(file)
       if os.path.getsize(self.contact_database)==0: print("Contact Book is empty, Please create contacts".center(129))
       else:
         for fields in self.contact_fields:
            print('{0:<10}'.format(fields).center(10), end="\t\t")
         print('{0:<10}'.format("Date"))
         print('{:<10}\t\t{:<10}\t\t{:<10}'.format('----','---------','----'))
         print("")
         
         for data in read:
            
            for item in data:
                 print( '{:<10}'.format(item).center(10), end="\t\t")  
            print("")
      print("\n")
      input("\t Press enter key to continue..".center(120))
      os.system('cls')
      
   #writing search function
   def search(self):
      os.system('cls')
      title()
      print("Search Contacts:".center(10))
      print("----------------".center(10))
      print("")
      self.contact_person_match = 'false'
      search_value = input("Enter your name: ")
      print("")
      for fields in self.contact_fields:
         print('{0:<10}'.format(fields).center(10), end="\t\t")
      print('{0:<10}'.format("Date"))
      print('{:<10}\t\t{:<10}\t\t{:<10}'.format('----','---------','----').center(10))
      print("")
      with open(self.contact_database, 'r') as file:
         read = csv.reader(file)
         for data in read:
          if len(data)>0:
           if search_value == data[0]:
             self.contact_person_match = 'true'
             print( '{:<10}\t\t{:<10}\t\t{:<10}'.format(data[0], data[1], data[2]).center(10))
      if self.contact_person_match == 'false':
         print("")
         print("Sorry!, there is no contact by this name".center(129))  
      print("")
      #input("\t press enter key to continue..")
       
   #writing delete function
   def delete(self):
        os.system('cls')
        title()
        print("")
        print("Delete Contacts:")
        print("----------------")
        print("")
        
        self.contact_person_match = 'false'
        update_contact = input("Enter the name: ")
        update_list = []
        with open(self.contact_database, 'r') as file:
         read = csv.reader(file)
         for data in read:
          if len(data)>0:
           if update_contact != data[0]: 
              update_list.append(data)
           else:
              self.contact_person_match = 'true'
   
         if self.contact_person_match == 'true':
            with open(self.contact_database, 'w') as file:
              write = csv.writer(file)
              write.writerows(update_list)
              print("")
              print("Contact is deleted successfully!".center(129))
              print("")
        if self.contact_person_match == 'false':
            print("")
            print("Sorry! data not found")
            print("")
        #input("\t Press enter key to continue..")
   




#creating object of the class
contact_class = contact_numbers()

os.system('cls')
title()
while True:
  print("1. View Contacts".center(128))
  print("2. Create Contacts".center(129))
  print("3. Search Contacts".center(129))
  print("4. Delete Contacts".center(129))
  print("5. Exit".center(120))
  print("_______________________".center(131))
  option = int(input("\t\t\t\t\t\t\tChoose you option: "))

  if option == 1: 
   contact_class.view()
   title()

  if option == 2:
   while True:
    contact_class.create()
    ans = input("\t\t\t\t\tDo you want to create another contact number?[Y/N]: ")
    if ans == 'Y' or ans == 'y':
      continue
    else: break
   os.system('cls')
   title()

  if option == 3:
   while True:
    contact_class.search()
    print("")
    ans = input("\t\t\t\t\tDo you want to search another contact number?[Y/N]: ")
    if ans == 'Y' or ans == 'y':
      continue
    else: break
   os.system('cls')
   title()

  if option == 4:
   while True:
      contact_class.delete()
      ans = input("\t\t\t\t\tDo you want to delete another contact number?[Y/N]: ")
      if ans == 'Y' or ans == 'y':
        continue
      else: break
   os.system('cls')
   title()
  #writing exit code
  if option == 5:
   os.system('cls')
   line_1 = "------------------------------------------"
   Tq     = "   Thank you for using this software"
   line_2 = "------------------------------------------"
   print(line_1.center(130))
   print(Tq.center(130))
   print(line_2.center(130))
   break
  #error message for selecting the wrong option
  if option > 5 or option < 1:
      os.system('cls')
      print("Invalid choice. Please choose valid option".center(129))
      print("\n")
      input("Press enter key to continue...".center(130))
      os.system('cls')
      title()








				

				



	


