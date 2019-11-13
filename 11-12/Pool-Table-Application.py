
import time
import datetime

tables = []

class Table:
    def __init__(self, table_number, is_occupied):
        self.table_number = table_number
        self.is_occupied = False
        tables.append(self)

    def start_time(self):
        self.time_start = time.time()
        #self.time_started = strftime('%y-%m-%d %H:%M:%S', localtime())
        self.time_started = datetime.datetime.now()
    
    def end_time(self):
        self.time_end = time.time()
        #self.time_ended = strftime('%y-%m-%d %H:%M:%S', localtime())
        self.time_ended = datetime.datetime.now()
        self.time_played()

    def time_played(self):
        self.time_passed = self.time_end - self.time_start
        self.minutes_passed = round(self.time_passed / 60,2)
        self.cost = self.minutes_passed * .50
            
        #print(end_time(self)-start_time(self))

    def start_table(self):
        self.start_time()
        self.is_occupied = True
        print(f'Table {self.table_number} Started at {self.time_started}')

    def end_table(self):
        self.is_occupied = False
        self.end_time()
        print(f'Table {self.table_number} Ended at {self.time_ended}')
        self.print_to_txt()
    
    def print_to_txt(self):
        with open('table_logs.txt','a') as file_object:
            file_object.write(f'Table {self.table_number}: \r START TIME: {self.time_started} \r END TIME: {self.time_ended} \r TOTAL TIME PLAYED: {self.minutes_passed} MINUTES \r TOTAL COST: ${self.cost} \r _______________________________________________ \n') 

def print_free_tables():
    print('free tables:')
    for i in range(0,len(tables)):
        if tables[i].is_occupied == False:
            print(tables[i].table_number)

def print_occ_tables():
    print('occupied tables:')
    for i in range(0,len(tables)):
        if tables[i].is_occupied:
            print(f'Table: {tables[i].table_number} has been occupied since {tables[i].time_started}')

def initialize_tables():
    for index in range(1,13):
        table = Table(index, False)

def user_input():
    user_input = ("enter your choice here:")

def which_to_start():
    to_start = int(input("Input which table you would like to check out:")) - 1
    if not tables[to_start].is_occupied:
        tables[to_start].start_table()
    else:
        print(f"Table {tables[to_start].table_number} is occupied already. Sorry!")

def which_to_end():
    to_end = int(input("Input which table you would like to check back in:")) - 1
    if tables[to_end].is_occupied:
        tables[to_end].end_table()    
    else:
        print(f"Table {tables[to_end].table_number} is occupied already. Sorry!")    

def print_all_tables():
    print_free_tables()
    print_occ_tables()

def take_user_input():
    menu = input("Type START to start a table, END to end a table, VIEW to view a table.").upper()
    if(menu == "START"):
        which_to_start()
    elif(menu == "END"):
        which_to_end()
    elif(menu == "VIEW"):
        print_all_tables()

initialize_tables()
while True:
    take_user_input()
