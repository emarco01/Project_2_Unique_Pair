from tkinter import *
import csv
from random import *

members_list: list = []
# empty list to store members throughout the user interaction


class GUI:
    """
    Class that represents the whole of the Graphical User Interface
    """
    def __init__(self, window) -> None:
        """
        Constructor for each of the frames within the GUI
        """
        self.window = window

        # The title frame
        self.frame_title = Frame(self.window)
        self.label_title = Label(self.frame_title, text='Create Your Unique Groups', font=25)
        self.label_title.pack(side='top')
        self.frame_title.pack(pady=10)

        # The frame for the label and entry of the text file name.
        self.frame_members_file = Frame(self.window)
        self.label_members_file = Label(self.frame_members_file, text='File Name for Members:')
        self.entry_members_file = Entry(self.frame_members_file)
        self.label_members_file.pack(side='left', padx=10)
        self.entry_members_file.pack(side='left', padx=10)
        self.frame_members_file.pack(pady=10)

        # A frame for the submit button corresponding to the text file's name.
        self.frame_submit_members_file = Frame(self.window)
        self.button_submit_members_file = Button(self.frame_submit_members_file, text='Submit', command=self.clicked_submit_members_file)
        self.button_submit_members_file.pack()
        self.frame_submit_members_file.pack(pady=10)

        # The frame for an error message corresponding to the text file.
        self.frame_error_members_file = Frame(self.window)
        self.label_error_message_member_file = Label(self.frame_error_members_file, text='')
        self.label_error_message_member_file.pack(side='left')
        self.frame_error_members_file.pack(pady=10)

        # A frame for the label, entry, and submit corresponding to the addition of members.
        self.frame_member_addition = Frame(self.window)
        self.label_entry_addition = Label(self.frame_member_addition, text='Enter Member:')
        self.entry_member_addition = Entry(self.frame_member_addition)
        self.button_submit_addition = Button(self.frame_member_addition, text='Submit', command=self.clicked_submit_addition)
        self.label_entry_addition.pack(side='left', padx=9)
        self.entry_member_addition.pack(side='left', padx=10)
        self.button_submit_addition.pack(side='left', padx=10)
        self.frame_member_addition.pack(pady=20)

        # A frame for the label, entry, and submit corresponding to the removal of members.
        self.frame_member_removal = Frame(self.window)
        self.label_entry_removal = Label(self.frame_member_removal, text='Remove Member:')
        self.entry_member_removal = Entry(self.frame_member_removal)
        self.button_submit_removal = Button(self.frame_member_removal, text='Submit', command=self.clicked_submit_removal)
        self.label_entry_removal.pack(side='left')
        self.entry_member_removal.pack(side='left', padx=10)
        self.button_submit_removal.pack(side='left', padx=10)
        self.frame_member_removal.pack(pady=10)

        # The frame for an error message corresponding to the addition or removal of members.
        self.frame_error_members = Frame(self.window)
        self.label_error_message_member = Label(self.frame_error_members, text='')
        self.label_error_message_member.pack(side='left')
        self.frame_error_members.pack(pady=10)

        # A frame to prompt the user when to continue.
        self.frame_message = Frame(self.window)
        self.label_continue_message = Label(self.frame_message, text='Continue once the list of members is up to date.')
        self.label_continue_message.pack(side='left')
        self.frame_message.pack(pady=10)

        # A frame for the labels and entry for the csv file for creation/writing and reading
        self.frame_csv_file = Frame(self.window)
        self.label_entry_csv_file = Label(self.frame_csv_file, text='File Name for Groups:')
        self.entry_csv_file = Entry(self.frame_csv_file)
        self.label_entry_csv_file.pack(side='left', padx=10)
        self.entry_csv_file.pack(side='left', padx=7)
        self.frame_csv_file.pack(pady=10)

        # The frame for an error message corresponding to the csv file.
        self.frame_error_file = Frame(self.window)
        self.label_error_message_csv_file = Label(self.frame_error_file, text='')
        self.label_error_message_csv_file.pack(side='left')
        self.frame_error_file.pack(pady=10)

        # The frame for the create button
        self.frame_create = Frame(self.window)
        self.button_create_groups = Button(self.frame_create, text='Create Groups', command=self.clicked_submit_create)
        self.button_create_groups.pack(side='left')
        self.frame_create.pack(pady=10)

        # Default file names to help prevent FileNotFoundError
        self.members_file = 'Members.txt'
        self.groups_file = 'Groups.csv'

    def clicked_submit_members_file(self) -> None:
        """
        Method that tries to open a pre-existing file, named by user input, and if there is not a file
        it creates and opens one for appending. If the file does exist it is read for its contents, which are sent
        to members_list to be used later.
        """
        self.members_file: str = self.entry_members_file.get()

        try:
            with open(self.members_file, 'r') as file_m:
                for line in file_m:
                    members_list.append(line)
        except FileNotFoundError:
            with open(self.members_file, 'w'):
                pass

        self.entry_members_file.delete(0, END)

    def clicked_submit_addition(self):
        """
        Method that adds members from both the file, and list within the code. User input required on the GUI.
        An error message is displayed if the member already exists in the file/list.
        """
        member = self.entry_member_addition.get()

        if type(member) != str:
            raise ValueError('Non-string Value')

        if member not in members_list:
            members_list.append(member)
            with open(self.members_file, 'a', newline='') as file_m:
                file_m.write(member + '\n')

        else:
            self.label_error_message_member.config(text='Error: Member already present in list')

        self.entry_member_addition.delete(0, END)

    def clicked_submit_removal(self) -> None:
        """
        Method that remove members from both the file, and list within the code. User input required on the GUI.
        An error message is displayed if the member does not exist in the file/list.
        """
        member = self.entry_member_removal.get()
        if type(member) != str:
            raise TypeError('Non-string Value')

        if member in members_list:
            members_list.remove(member)
            with open(self.members_file, 'w', newline='') as file_m:
                for member in members_list:
                    file_m.write(member + '\n')
        else:
            self.label_error_message_member.config(text='Error: Member not present in list')

        self.entry_member_removal.delete(0, END)

    def clicked_submit_create(self) -> None:
        """
        Method to create the groups of members. The groups should be pairs, which are unique sets of members.
        An input in the GUI is required for a csv file. If there is a pre-existing file, its contents are added to the
        groups list (a list of sets). Then the groups are made to be unique and stored in the csv file.
        If there is not a pre-existing file, the file is created and the groups are written to it.
        """
        self.groups_file = self.entry_csv_file.get()
        members_file_content: list = []
        # A list of the members from the previous file/list.

        with open(self.members_file, 'r') as file_m:
            for line in file_m:
                members_file_content.append(line)

        try:
            with open(self.groups_file, 'r+', newline='') as csvfile:
                content_reader = csv.reader(csvfile, delimiter=',')
                content_writer = csv.writer(csvfile)
                groups: list = []

                for group in content_reader:
                    groups.append(group)

                for member in members_file_content:
                    group = set()
                    group.add(member)
                    while True:
                        while True:
                            other = members_file_content[randint(0, len(members_file_content) - 1)]
                            if other != member and other not in group:
                                group.add(other)
                                break
                        if group not in groups:
                            groups.append(group)
                            break

                content_writer.writerows(groups)

        except FileNotFoundError:
            with open(self.groups_file, 'a', newline='') as csvfile:
                content_writer = csv.writer(csvfile)
                groups = []

                for member in members_file_content:
                    group = set()
                    group.add(member)
                    while True:
                        while True:
                            other = members_file_content[randint(0, len(members_file_content) - 1)]
                            if other != member and other not in group:
                                group.add(other)
                                break
                        if group not in groups:
                            groups.append(group)
                            break

                content_writer.writerows(groups)
