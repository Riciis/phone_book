contacts = []
while (True):

 print("Ievadi")
 print("ADD, lai ievadītu jaunu kontaktu")
 print("SEE, lai izvadītu kontaktus")
 print("END, lai beigtu darbu")
 kodarisim = input("-")

 if kodarisim == "ADD" :



   person_name = input("Name :")
   person_surname = input("Surname :")
   person_phone = input("Phone :")
   person_email = input("Email :")

   person_contact = {
   "name" : person_name,
   "surname" : person_surname,
   "phone" : person_phone,
   "email" : person_email
   }
   
   contacts.append(person_contact)



 elif kodarisim == "SEE" :
    print(contacts)

 elif kodarisim == "END" :
    break
