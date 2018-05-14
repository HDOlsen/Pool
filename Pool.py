from datetime import datetime, timedelta
import datetime
from time import strftime, gmtime
import time
import pickle
import random

class Pool: 
    def __init__(self, position):
         self.position = position
         self.status = "Not checked out"
         self.time = None
         self.start_time_str = None
         self.end_time_str = None
         self.start_time = None
         self.end_time = None
         self.total_time = None

    def open(self):
        self.status = "Checked out"
        #self.start_time_st= time.strftime("%D %B %Y :%H:%M:%S")
        #self.start_time = time.strftime("%H:%M:%S")

        time_values = datetime.datetime.now()
        time_log = time.asctime( time.localtime(time.time()))
        self.start_time = time_values
        self.start_time_str = time_log

    def close (self):
        self.status = "Not checked out"
        # self.end_time_str = time.strftime("%D %B %Y :%H:%M:%S") 
        # self.end_time = time.strftime("%H:%M:%S")
        # sum(x * int(t) for x, t in zip([3600, 60, 1], self.end_time.split(":")))

        time_values = datetime.datetime.now()
        time_log = time.asctime( time.localtime(time.time()))

        self.end_time = time_values
        self.end_time_str = time_log
        beginning = self.start_time
        end = self.end_time
        total_time = end - beginning
        self.total_time = total_time
        hours_seconds = divmod(total_time.days * 86400 + total_time.seconds, 60)
        total_minutes = hours_seconds[0]*60 + hours_seconds[1]

        transaction = f"session table: {self.position} | session start: {self.start_time_str} | duration: {str(self.total_time)} \r\n"
        self.write_to_file(transaction)

        #this is a test of saving data
        #self being passed in could be any piece of python data, any object, array, dictionary whatever.
        self.save_python_data(self)

        #this is a test of loading data
        #put this wherever you need to load saved data
        #pass in the file name of the file that you want to load data from
        self.load_python_data('tables_data.pkl')


    def write_to_file(self, transaction): 
        file = open('poolcheck.txt','a+')
        file.write(transaction)
        file.close()

    def save_python_data(self, output):
      
        with open('tables_data.pkl', 'wb') as output_file:
            # Pickle the 'data' using the highest protocol available.
            pickle.dump(output, output_file, pickle.HIGHEST_PROTOCOL)

    def load_python_data(self, file_name):

        with open(file_name, 'rb') as input_file:
            # The protocol version used is detected automatically, so we do not
            # have to specify it.
            data = pickle.load(input_file)

        # data variable is just the python data we saved, you could do anything with it
        print(data, "this is the data")
        print(data.position, "this is the table's position")

    def __repr__(self):
        return (f"Table position: {self.position} \n Table Status: {self.status} \n Time Checked Out: {self.start_time_str} \n Time Checked In: {self.end_time_str} \n Time Played: {self.total_time} \n ")
    
# name = input("Please input your first and last name:")
class Manager:

    def __init__(self):
        self.tables = []
        self.generate_tables()
        self.give_user_options()


    def generate_tables(self):
  
        for i in range(1,13):
            table = Pool(i)
            self.tables.append(table)
        

    def give_user_options(self):

        user_choice = int(input("1. view tables | 2. open table | 3. return table | 4. exit "))

        if user_choice == 1:
            
            self.view_tables()

        if user_choice == 2:

            chosen_table_number = int(input("enter table number to open: "))

            table = self.find_table(chosen_table_number)
            self.open_table(table)

        if user_choice == 3:

            chosen_table_number = int(input("enter table number to return: "))

            table = self.find_table(chosen_table_number)
            self.return_table(table)

        if user_choice == 4:

            self.exit()

    def find_table(self, position):

        chosen_table_obj = None

        for table in self.tables:

            if table.position == position:

                chosen_table_obj = table

                return chosen_table_obj


    def start_shift(self, employee_name):
        self.employee_name = employee_name 
        print(f"You are clocked in, {self.employee_name}!")
    def end_shift(self, end_of_day): #to print out closing pool table list
        self.end_of_day = end_of_day
        print({self.end_of_day})

    def open_table(self, table_obj):

        print(table_obj)
        table_obj.open()

        self.give_user_options()


    def return_table(self, table_obj):


        table_obj.close()

        self.give_user_options()

    def view_tables(self):


        print(self.tables)

        self.give_user_options()

    def exit(self):

        print('Goodbye!')

emp = Manager()
# emp.start_shift(name)

 
  #to view all tables and their status (open)







    

        


        
