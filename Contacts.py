# -*- coding: utf-8 -*-
"""
Implement a class that manages a directory that is saved in a text file.
The data saved includes:
    a.Name
    b.Email
    c.Age
    d.Country of Origin
The class should have capabilities to:
    -Add new record
    -Delete a record
    -Look for a record by mail and age
    -List on screen all record information

Name: Fabián Munoz Aguirre
Student ID: A00354910
"""
import json

class Contacts_Directory():
    directory_file_name = ""
    contacts = {}
    
    def __init__(self, directory_file_name):
        Contacts_Directory.directory_file_name = directory_file_name
        Contacts_Directory.contacts["contacts"] = []
    
    @classmethod
    def open_directory(cls, directory_file_name):
        with open(directory_file_name, encoding="utf-8") as json_file:
            cls.contacts = json.load(json_file)
            
    @classmethod
    def list_directory(cls):
        for record in cls.contacts["contacts"]:
            print("Name: ",record["name"])
            print("email: ",record["email"])
            print("Age: ",record["age"])
            print("Country: ",record["country"])
            print("-------\n")
            
    @classmethod
    def add_record(cls):
        new_contact_name = input("Enter the contact name: " )
        new_contact_email = input("Enter the contact email: " )
        new_contact_age = input("Enter the contact age: " )
        new_contact_country = input("Enter the country: " )
        cls.contacts["contacts"].append({"name": new_contact_name, "email": new_contact_email, "age": new_contact_age, "country": new_contact_country})
    
    @classmethod
    def delete_record(cls):
        print("Remove contact from directoy by email")
        rmv_contact_email = input("Enter the email: ")
        for i in range(len(cls.contacts["contacts"])):
            if cls.contacts["contacts"][i]["email"] == rmv_contact_email:
                cls.contacts["contacts"].pop(i)
    
    @classmethod
    def search_record(cls):
        print("Search contact from directoy by email or age")
        srch_contact = input("Enter the contact email or contact age: ")
        for i in range(len(cls.contacts["contacts"])):
            if (cls.contacts["contacts"][i]["email"] == srch_contact or cls.contacts["contacts"][i]["email"] == srch_contact):
                print("Name: ", cls.contacts["contacts"][i]["name"])
                print("email: ", cls.contacts["contacts"][i]["email"])
                print("Age: ", cls.contacts["contacts"][i]["age"])
                print("Country: ", cls.contacts["contacts"][i]["country"])
                print("-------\n")
                break
            
    @classmethod
    def commit_changes(cls):
        with open(cls.directory_file_name, "w") as json_file:
            json.dump(cls.contacts, json_file)


if __name__ == "__main__":
    print("Very Simple Contacts Directory programm")
    print("Please select the option")
    print("1.-Add a new contact record")
    print("2.-Delete a contact record")
    print("3.-Search a contact record")
    print("4.-List all contact records")
    print("5.-Exit")
    
    Contacts_Directory("C:\\Users\\fabmunoz\\Documents\\Personal - Maestria\\TC4002.1\\Lab 3\\contacts.txt")
    Contacts_Directory.open_directory(Contacts_Directory.directory_file_name)
    
    while True:
        option = input("Please select the option by number: ")
        if option == "1":
            Contacts_Directory.add_record()
        elif option == "2":
            Contacts_Directory.delete_record()
        elif option == "3":
            Contacts_Directory.list_directory()
        elif option == "4":
            Contacts_Directory.list_directory()
        elif option == "5":
            Contacts_Directory.commit_changes()
            break
        else:
            print("Please type a valid option")