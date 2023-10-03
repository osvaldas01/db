from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sql_alchemy.models import Projektas
from constants import print_menu


class ProjectManagement:
    def __init__(self):
        self.engine = create_engine('sqlite:///project.db')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_value(self, projektas: Projektas):
        self.session.add(projektas)
        self.session.commit()

    def get_value_by_id(self, id):
        value = self.session.query(Projektas).get(id)
        print(value)

    def filter_by_name(self, name):
        value = self.session.query(Projektas).filter_by(name=name).all()
        print(value)

    def filter_by_attributes(self, **kwargs):
        query = self.session.query(Projektas)
        for key, value in kwargs.items():
            query = query.filter(getattr(Projektas, key) == value)
        results = query.all()
        print(results)

    def update_value_by_id(self, id, new_name):
        value = self.session.query(Projektas).get(id)
        value.name = new_name
        self.session.commit()

    def delete_value(self, id):
        value = self.session.query(Projektas).get(id)
        self.session.delete(value)
        self.session.commit()

    def get_data(self):
        value = self.session.query(Projektas).all()
        print(value)


class UserInterFace(ProjectManagement):

    def __init__(self):
        super().__init__()
        self.menu_options = {
            1: self.add_value,
            2: self.get_value_by_id,
            3: self.filter_by_name,
            4: self.filter_by_attributes,
            5: self.update_value_by_id,
            6: self.delete_value,
            7: self.get_data,
        }

    def run(self):
        while True:
            for key, option in print_menu.items():
                print(f"{key}. {option}")
            choice = input("Enter the number: ").strip()

            if choice.isdigit():
                choice = int(choice)
                if choice in self.menu_options:
                    self.menu_options[choice]()
                else:
                    print("Invalid choice. Please enter a number!")
            if choice == 8:
                break

    def add_value(self):
        print("Add a New Project: ")
        name = input("Project Name: ")
        price = input("Price: ")
        author = input("Author: ")
        amount_of_copy = input("Number of Copies Made: ")
        rating = input("Rating: ")

        project = Projektas(
            name=name,
            price=price,
            author=author,
            amount_of_copy=amount_of_copy,
            rating=rating,
        )

        self.session.add(project)
        self.session.commit()
        print("Project has been successfully added to your database!")

    def get_value_by_id(self):
        value = input("Write an ID: ")
        self.get_value_by_id(value)

    def filter_by_name(self):
        name = input("Write name you want to filter by: ")
        self.filter_by_name(name)

    def filter_by_attributes(self):
        attributes = {}
        while True:
            key = input("Write your attribute (To end press Enter):  ").lower()
            if not key:
                break
            value = input(f"Write {key} value: ").lower()
            attributes[key] = value
        self.filter_by_attributes(**attributes)

    def update_value_by_id(self):
        id = input("Write project ID: ")
        new_name = input("Write new name for the project: ")
        self.update_value_by_id(id, new_name)
        print("Project name was updated!.")

    def delete_value(self):
        value = input("Enter an ID of a project that you want to delete: ")
        self.delete_value(value)
        print("Project was deleted!")

    def get_data(self):
        self.get_data()