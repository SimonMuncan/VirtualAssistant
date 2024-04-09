from assistantGUI import *
import re, datetime
from insertAndDelete import updateSQL

class CommandStrategy:
    def execute(self,main_window, command):
        pass

#make me a Piano class appointment for 2023-11-08 from 10:00 to 11:00 at Music school
# Strategy for inserting a one-time appointment
class insertOneTimeAppointment(CommandStrategy):
    def execute(self,main_window, command):
        # Regular expression pattern for matching the command
        pattern = re.compile("make me (a|an) (.*) appointment for (.*) from \d{2}:\d{2} to \d{2}:\d{2} at (.*)",re.IGNORECASE) 
        if pattern.match(command): 
            # Extracting necessary information from the command using regex
            get_activity = re.search(r"(a|an) (.*?) appointment",command,re.IGNORECASE).group(2)
            get_start_time = re.search(r"from (.*?) to",command,re.IGNORECASE).group(1)
            get_stop_time = re.search(r"to (.*?) at",command,re.IGNORECASE).group(1)
            get_location = re.search(r"at (.*)",command,re.IGNORECASE).group(1)
            date = ""
            date_get = re.findall(r"[\d]{4}-[\d]{1,2}-[\d]{1,2}",command)
            for s in date_get:
                date += s
            # SQL query to insert the appointment into the database
            sqlQuery = f"INSERT INTO AppointmentsOneTime (Date,TimeStart,TimeStop,Activity,Location) VALUES ('{str(date)}','{str(get_start_time)}','{str(get_stop_time)}','{str(get_activity)}','{str(get_location)}')"
            print(sqlQuery)
            # Execute the SQL query (updateSQL is assumed to be defined elsewhere)
            updateSQL.sqlInsertDelete(sqlQuery)

#remove my Piano class appointment for 2023-11-08 at 10:00
# Strategy for removing a one-time appointment
class removeOneTimeAppointment(CommandStrategy):
    def execute(self,main_window, command):
        pattern = re.compile("remove my (.*) appointment for (.*) at \d{2}:\d{2}",re.IGNORECASE) 
        if pattern.match(command): 
            get_activity = re.search(r"my (.*?) appointment",command,re.IGNORECASE).group(1)
            get_start_time = re.search(r"at (.*)",command,re.IGNORECASE).group(1)
            date = ""
            date_get = re.findall(r"[\d]{4}-[\d]{1,2}-[\d]{1,2}",command)
            for s in date_get:
                date += s
            # SQL query to remove the appointment from the database
            sqlQuery = f"DELETE FROM AppointmentsOneTime WHERE LOWER(TRIM(Activity)) = LOWER(TRIM('{str(get_activity)}')) AND LOWER(TRIM(TimeStart)) = LOWER(TRIM('{str(get_start_time)}')) AND LOWER(TRIM(Date)) = LOWER(TRIM('{str(date)}'))"
            print(sqlQuery)
            # Execute the SQL query
            updateSQL.sqlInsertDelete(sqlQuery)


#make me a Piano class appointment from 2023-11-06 to 2023-11-11 from 10:00 to 11:00 at Music school
# Strategy for inserting a recurring appointment
class insertReccuringAppointment(CommandStrategy):
    def execute(self,main_window, command):
        pattern = re.compile("make me (a|an) (.*) appointment from (.*) to (.*) from \d{2}:\d{2} to \d{2}:\d{2} at (.*)",re.IGNORECASE) 
        if pattern.match(command): 
            get_activity = re.search(r"(a|an) (.*?) appointment",command,re.IGNORECASE).group(2)
            get_start_time = re.search(r"from ([\d]{2}:[\d]{2}) to",command,re.IGNORECASE).group(1)
            get_stop_time = re.search(r"to ([\d]{2}:[\d]{2}) at",command,re.IGNORECASE).group(1)
            get_location = re.search(r"at (.*)",command,re.IGNORECASE).group(1)
            date_start = re.search(r"from ([\d]{4}-[\d]{2}-[\d]{2}) to",command,re.IGNORECASE).group(1)
            date_stop = re.search(r"to (.*?) from",command,re.IGNORECASE).group(1)
            # SQL query to insert the recurring appointment into the database
            sqlQuery = f"INSERT INTO AppointmentsReccuring (DateStart,DateStop,TimeStart,TimeStop,Activity,Location) VALUES ('{str(date_start)}','{str(date_stop)}','{str(get_start_time)}','{str(get_stop_time)}','{str(get_activity)}','{str(get_location)}')"
            print(sqlQuery)
            # Execute the SQL query
            updateSQL.sqlInsertDelete(sqlQuery)

#remove my Piano class appointment from 2023-11-06 to 2023-11-11 at 10:00
# Strategy for removing a recurring appointment
class removeReccuringAppointment(CommandStrategy):
    def execute(self,main_window, command):
        pattern = re.compile("remove my (.*) appointment from (.*) to (.*) at \d{2}:\d{2}",re.IGNORECASE) 
        if pattern.match(command): 
            get_activity = re.search(r"my (.*?) appointment",command,re.IGNORECASE).group(1)
            get_start_time = re.search(r"at (.*)",command,re.IGNORECASE).group(1)
            date_start = re.search(r"from (.*?) to",command,re.IGNORECASE).group(1)
            date_stop = re.search(r"to (.*?) at",command,re.IGNORECASE).group(1)
            # SQL query to remove the recurring appointment from the database
            sqlQuery = f"DELETE FROM AppointmentsReccuring WHERE LOWER(TRIM(Activity)) = LOWER(TRIM('{str(get_activity)}')) AND LOWER(TRIM(TimeStart)) = LOWER(TRIM('{str(get_start_time)}')) AND LOWER(TRIM(DateStart)) = LOWER(TRIM('{str(date_start)}')) AND LOWER(TRIM(DateStop)) = LOWER(TRIM('{str(date_stop)}'))"
            print(sqlQuery)
            # Execute the SQL query
            updateSQL.sqlInsertDelete(sqlQuery)