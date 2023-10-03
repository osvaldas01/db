from sql_alchemy.db_management import ProjectManagement
from sql_alchemy.db_management import UserInterface
from sql_alchemy.models import Projektas

if __name__ == "__main__":

    user_interface = UserInterface()
    user_interface.run()
    # manager = ProjectManagement()
    # manager.add_value(Projektas(name="books", price=5, author="unknown", amount_of_copy=15, rating=5))
    # manager.get_value_by_id(1)
    # manager.filter_by_name("Pirmas projektas")
    # manager.update_value_by_id(1, "Atnaujintas projektas")
    # manager.delete_value(1)
    # manager.filter_by_attributes(rating=3.9)
    # manager.session.close()

