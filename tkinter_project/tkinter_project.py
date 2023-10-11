import tkinter as tk
from tkinter import Label, Entry, Button, Toplevel, simpledialog, messagebox
from alchemy.db_management import ProjectManagement
from alchemy.models import Projektas
from constants_file.naujastestas import THISTEXT
from tkinter_logging_main import Logger

logger = Logger()
game = ProjectManagement()


class Demo1(ProjectManagement):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.frame = tk.Frame(self.master)
        self.text = THISTEXT

        button_info = [
            ("Get Value", self.get_value),
            ("Update Value", self.update_value),
            ("Create Value", self.create_value),
            ("Delete Value", self.delete_value),
            ("Save text to file", self.save_to_file),
            ("Get symbols", self.get_symbols),
            ("Change words", self.change_words),
            ("Add word", self.add_word),
            ("Delete words", self.delete_words),
            ("Get number of symbols", self.get_most_popular_word)
        ]

        for text, command in button_info:
            button = Button(self.frame, text=text, command=command)
            button.pack()

        self.frame.pack()

    def get_value(self):
        logger.logger.debug("Get value button pressed")
        get_value_window = Toplevel(self.master)
        get_value_window.title("Get Value")

        for value in game.get_data():
            label = Label(get_value_window, text=value)
            label.pack()

        logger.logger.info(f"Project data: {game.get_data()}")

        get_value_window.mainloop()

    def update_value(self):
        logger.logger.debug("Update value button pressed")
        update_window = Toplevel(self.master)
        update_window.title("Update Value")

        def update_by_id():
            try:
                id_value = id_entry.get()
                attribute_value = attribute_entry.get()
                new_value = get_value_entry.get()
                game.update_value_by_id(id_value, attribute_value, new_value)
                update_window.destroy()
            except Exception as e:
                logger.logger.error(f"Error while updating value: {e}")

        id_label = Label(update_window, text="ID:")
        id_label.pack()
        id_entry = Entry(update_window)
        id_entry.pack()

        attribute_label = Label(update_window, text="Attribute:")
        attribute_label.pack()
        attribute_entry = Entry(update_window)
        attribute_entry.pack()

        get_value_label = Label(update_window, text="Value:")
        get_value_label.pack()
        get_value_entry = Entry(update_window)
        get_value_entry.pack()

        submit_button = Button(update_window, text="Update", command=update_by_id)
        submit_button.pack()

        update_window.mainloop()

    def create_value(self):
        logger.logger.debug("Create value button pressed")
        try:
            create_window = Toplevel(self.master)
            create_window.title("Create Project")

            attributes = [
                ("Name:", tk.Entry),
                ("Price:", tk.Entry),
                ("Author:", tk.Entry),
                ("Amount of copy:", tk.Entry),
                ("Rating:", tk.Entry)
            ]
            entries = {}

            for label_text, entry_type in attributes:
                label = tk.Label(create_window, text=label_text)
                label.pack()
                entry = entry_type(create_window)
                entry.pack()
                entries[label_text] = entry

            submit_button = tk.Button(create_window, text="Submit",
                                      command=lambda: self.add_project(create_window, entries))
            submit_button.pack()
            logger.logger.info(f"Project with Name: {entries['Name:'].get()}, "
                               f"Price: {entries['Price:'].get()}, "
                               f"Author: {entries['Author:'].get()}, "
                               f"Amount of copy: {entries['Amount of copy:'].get()}, "
                               f"Rating: {entries['Rating:'].get()} created successfully")
        except Exception as e:
            logger.logger.error(f"Error while creating project: {e}")

    def add_project(self, create_window, entries):
        project_info = {}
        for label_text, entry in entries.items():
            project_info[label_text] = entry.get()

        try:
            project = Projektas(
                name=project_info["Name:"],
                price=int(project_info["Price:"]),
                author=project_info["Author:"],
                amount_of_copy=int(project_info["Amount of copy:"]),
                rating=float(project_info["Rating:"]),
            )
            game.add_value(project)
            create_window.destroy()

            logger.logger.info(f"Project added:{project_info['Name:']}, "
                               f"Price:{project_info['Price:']}, "
                               f"Author:{project_info['Author:']}, "
                               f"Amount of copy:{project_info['Amount of copy:']}, "
                               f"Rating:{project_info['Rating:']}")
        except Exception as e:
            logger.logger.error(f"Error while adding project: {e}")

    def delete_value(self):
        logger.logger.debug("Delete value button pressed")
        delete_window = Toplevel(self.master)
        delete_window.title("Delete Value")

        def delete_by_id():
            id_value = id_entry.get()
            try:
                game.delete_value(id_value)
                logger.logger.info(f"Project deleted:{id_value}")
            except Exception as e:
                logger.logger.error(f"Error while deleting project: {e}")
            delete_window.destroy()

        id_label = Label(delete_window, text="ID:")
        id_label.pack()
        id_entry = Entry(delete_window)
        id_entry.pack()

        submit_button = Button(delete_window, text="Delete", command=delete_by_id)
        submit_button.pack()
        delete_window.mainloop()

    def save_to_file(self):
        logger.logger.debug("Save to file button pressed")
        variable = simpledialog.askstring("Input variable", "Enter a variable name", parent=self.master)
        if variable:
            with open(variable + ".txt", "w") as file:
                file.write(self.text)
        messagebox.showinfo("Info", "File saved successfully")
        logger.logger.info(f"File with name: {variable} saved successfully")

    def get_symbols(self):
        logger.logger.debug("Get symbols button pressed")
        variable = simpledialog.askstring("Input variable", "Enter a variable name", parent=self.master)
        symbols_to_find = simpledialog.askstring("Input letters",
                                                 "Enter a letter or letters to find", parent=self.master)
        words_with_symbols = []
        try:
            with open(f"{variable}.txt", "r") as file:
                for word in file.read().split():
                    if all(symbol in word for symbol in symbols_to_find):
                        words_with_symbols.append(word)

                if words_with_symbols:
                    result = "\n".join(words_with_symbols)
                    messagebox.showinfo(f"Words with {words_with_symbols} ", result)
                else:
                    messagebox.showinfo("Info", "No words found")

            logger.logger.info(f"In a file {variable} found words with {symbols_to_find} symbols, {result}")
        except Exception as e:
            logger.logger.error(f"Error while getting symbols: {e}")

    def change_words(self):
        logger.logger.debug("Change words button pressed")
        variable = simpledialog.askstring("Input variable", "Enter a variable name", parent=self.master)
        word_to_change = simpledialog.askstring("Input word", "Enter a word to change", parent=self.master)
        new_word = simpledialog.askstring("Input new word", "Enter a new word", parent=self.master)

        try:
            with open(f"{variable}.txt", "r") as file:
                text = file.read()
                words = text.split()
                updated_words = [word.replace(word_to_change, new_word) for word in words]
                updated_text = " ".join(updated_words)
                with open(f"{variable}.txt", "w") as file:
                    file.write(updated_text)
                messagebox.showinfo("Info", "Words changed successfully")
                logger.logger.info(f"In a file {variable} changed words {word_to_change} to {new_word}")
        except Exception as e:
            logger.logger.error(f"Error while changing words: {e}")

    def add_word(self):
        logger.logger.debug("Add word button pressed")
        variable = simpledialog.askstring("Input variable", "Enter a variable name", parent=self.master)
        word_to_add = simpledialog.askstring("Input word", "Enter a word to add", parent=self.master)

        try:
            with open(f"{variable}.txt", "a") as file:
                file.write(f" {word_to_add}")
            messagebox.showinfo("Info", "Word added successfully")
            logger.logger.info(f"In a file {variable} added word {word_to_add}")
        except Exception as e:
            logger.logger.error(f"Error while adding word: {e}")

    def delete_words(self):
        logger.logger.debug("Delete words button pressed")
        try:
            variable = simpledialog.askstring("Input variable", "Enter a variable name", parent=self.master)
            word_to_delete = simpledialog.askstring("Input word", "Enter a word to delete", parent=self.master)

            with open(f"{variable}.txt", "r") as file:
                text = file.read()
                words = text.split()
                updated_words = [word for word in words if word != word_to_delete]
                updated_text = " ".join(updated_words)
                with open(f"{variable}.txt", "w") as file:
                    file.write(updated_text)
                messagebox.showinfo("Info", "Word deleted successfully")
                logger.logger.info(f"In a file {variable} deleted word {word_to_delete}")
        except Exception as e:
            logger.logger.error(f"Error while deleting words: {e}")

    def get_most_popular_word(self):
        logger.logger.debug("Get most popular word button pressed")
        word_count = {}
        variable = simpledialog.askstring("Input variable", "Enter a variable name", parent=self.master)
        try:
            with open(f"{variable}.txt", "r") as file:
                text = file.read()
                for word in text.split():
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
                most_popular_word = max(word_count, key=word_count.get)
                label = Label(self.master,
                              text=f"Most popular word is ( {most_popular_word} ), "
                                   f"it appears {word_count[most_popular_word]} times")
                label.pack()
                logger.logger.info(f"In a file {variable} found most popular word {most_popular_word}")
        except Exception as e:
            logger.logger.error(f"Error while getting most popular word: {e}")
