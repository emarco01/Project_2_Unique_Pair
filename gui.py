from tkinter import *
import csv
from random import *


members_list = []


class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_one = Frame(self.window)
        self.label_title = Label(self.frame_one, text='Create Your Unique Groups')
        self.label_title.pack(side='top')
        self.frame_one.pack()

        self.frame_two = Frame(self.window)
        self.label_entry_addition = Label(self.frame_two, text='Enter Member:')
        self.entry_member_addition = Entry(self.frame_two)
        self.button_submit_addition = Button(self.frame_two, text='Submit', command=self.clicked_submit_addition)
        self.label_entry_addition.pack(side='left', padx=9)
        self.entry_member_addition.pack(side='left', padx=10)
        self.button_submit_addition.pack(side='left', padx=10)
        self.frame_two.pack(pady=20)

        self.frame_three = Frame(self.window)
        self.label_entry_removal = Label(self.frame_three, text='Remove Member:')
        self.entry_member_removal = Entry(self.frame_three)
        self.button_submit_removal = Button(self.frame_three, text='Submit', command=self.clicked_submit_removal)
        self.label_entry_removal.pack(side='left')
        self.entry_member_removal.pack(side='left', padx=10)
        self.button_submit_removal.pack(side='left', padx=10)
        self.frame_three.pack(pady=10)

        self.frame_four = Frame(self.window)
        self.label_error_message_member = Label(self.frame_four, text='')
        self.label_error_message_member.pack(side='left')
        self.frame_four.pack(pady=10)

        self.frame_five = Frame(self.window)
        self.label_continue_message = Label(self.frame_five, text='Continue once the list of members is up to date.')
        self.label_continue_message.pack(side='left')
        self.frame_five.pack(pady=10)

        self.frame_six = Frame(self.window)
        self.label_entry_group_size = Label(self.frame_six, text='Size of Groups:')
        self.entry_groups_size = Entry(self.frame_six)
        self.label_entry_group_size.pack(side='left')
        self.entry_groups_size.pack(side='left', padx=10)
        self.frame_six.pack(pady=10)

        self.frame_seven = Frame(self.window)
        self.label_entry_file = Label(self.frame_seven, text='File Name:')
        self.entry_file = Entry(self.frame_seven)
        self.label_entry_file.pack(side='left', padx=10)
        self.entry_file.pack(side='left', padx=7)
        self.frame_seven.pack(pady=10)

        self.frame_eight = Frame(self.window)
        self.label_error_message_file = Label(self.frame_eight, text='error')
        self.label_error_message_file.pack(side='left')
        self.frame_eight.pack(pady=10)

        self.frame_nine = Frame(self.window)
        self.button_create_groups = Button(self.frame_nine, text='Create Groups', command=self.clicked_submit_create)
        self.button_create_groups.pack(side='left')
        self.frame_nine.pack(pady=10)

        self.frame_ten = Frame(self.window)
        self.button_close = Button(self.frame_ten, text='Close', command=self.window.destroy)
        self.button_close.pack(side='left')
        self.frame_ten.pack(pady=25)

    def clicked_submit_addition(self):
        member = self.entry_member_addition.get()

        if type(member) != str:
            raise ValueError('Non-string Value')

        if member not in members_list:
            members_list.append(member)
        else:
            self.label_error_message_member.config(text='Error: Member already present in list')

        self.entry_member_addition.delete(0, END)

        print('clicked')
        print(members_list)
        print()

    def clicked_submit_removal(self):
        member = self.entry_member_removal.get()
        if type(member) != str:
            raise ValueError('Non-string Value')

        if member in members_list:
            members_list.remove(member)
        else:
            self.label_error_message_member.config(text='Error: Member not present in list')

        self.entry_member_removal.delete(0, END)

        print('clicked')
        print(members_list)
        print()

    def clicked_submit_create(self):
        group_size = self.entry_groups_size.get()
        file_name = self.entry_file.get()

        with open(file_name, 'a', newline='') as members_file:
            for member in members_list:
                members_file.write(member + '\n')

        try:
            with open('Groups.csv', 'r+', newline='') as csvfile:
                content_reader = csv.reader(csvfile)
                content_writer = csv.writer(csvfile)
                members_file_content = []
                groups = []

                with open(file_name, 'r') as members_file:
                    for line in members_file:
                        members_file_content.append(line)

                for member in members_file_content:
                    other = members_file_content[randint(0, len(members_file_content) - 1)]
                    group = []
                    group.append(member)
                    group.append(other)
                    content_writer.writerow(group)

        except FileNotFoundError:
            with open('Groups.csv', 'a', newline='') as csvfile:
                content_writer = csv.writer(csvfile)
                members_file_content = []
                groups = []

                with open(file_name, 'r') as members_file:
                    for line in members_file:
                        members_file_content.append(line)

                for member in members_file_content:
                    other = members_file_content[randint(0, len(members_file_content) - 1)]
                    group = set()
                    group.add(member)
                    group.add(other)
                    content_writer.writerow(group)

        print('clicked')
