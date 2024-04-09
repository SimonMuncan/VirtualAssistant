from assistantGUI import *
import re, datetime
from insertAndDelete import updateSQL

class CommandStrategy:
    def execute(self,main_window, command):
        pass

#schedule me for Monday gym from 12:00 to 14:00 at Snagatorijum
# Strategy for inserting an item from the schedule
class insertSchedule(CommandStrategy):
    def execute(self,main_window, command):
        # Regular expression pattern for matching the command
        pattern = re.compile("schedule me for (Monday|Tuesday|Wednesday|Thrusday|Friday|Saturday|Sunday|work) (.*) from \d{2}:\d{2} to \d{2}:\d{2} at (.*)",re.IGNORECASE) 
        if pattern.match(command): 
            get_table_name = re.search("(Monday|Tuesday|Wednesday|Thrusday|Friday|Saturday|Sunday|work)",command,re.IGNORECASE)
            get_activity = re.search(r"(Monday|Tuesday|Wednesday|Thrusday|Friday|Saturday|Sunday|work) (.*?) from",command,re.IGNORECASE).group(2)
            get_start_time = re.search(r"from (.*?) to",command,re.IGNORECASE).group(1)
            get_stop_time = re.search(r"to (.*?) at",command,re.IGNORECASE).group(1)
            get_location = re.search(r"at (.*)",command,re.IGNORECASE).group(1)
            # SQL query to insert the schedule into the corresponding table
            sqlQuery = f"INSERT INTO {get_table_name[0]} (TimeStart,TimeStop,Activity,Location) VALUES ('{str(get_start_time)}','{str(get_stop_time)}','{str(get_activity)}','{str(get_location)}')"
            print(sqlQuery)
            # Execute the SQL query
            updateSQL.sqlInsertDelete(sqlQuery)

#remove from my Monday schedule gym at 12:00
# Strategy for removing an item from the schedule
class removeSchedule(CommandStrategy):
    def execute(self,main_window, command):
        # Regular expression pattern for matching the command
        pattern = re.compile("remove from my (Monday|Tuesday|Wednesday|Thrusday|Friday|Saturday|Sunday|work) schedule (.*) at \d{2}:\d{2}",re.IGNORECASE) 
        if pattern.match(command): 
            # Extracting necessary information from the command using regex
            get_table_name = re.search("(Monday|Tuesday|Wednesday|Thrusday|Friday|Saturday|Sunday|work)",command,re.IGNORECASE)
            get_activity = re.search(r"schedule (.*?) at",command,re.IGNORECASE).group(1)
            get_start_time = re.search(r"at (.*)",command,re.IGNORECASE).group(1)
            # SQL query to remove the item from the corresponding table
            sqlQuery = f"DELETE FROM {get_table_name[0]} WHERE LOWER(TRIM(Activity)) = LOWER(TRIM('{str(get_activity)}')) AND LOWER(TRIM(TimeStart)) = LOWER(TRIM('{str(get_start_time)}'))"
            print(sqlQuery)
            # Execute the SQL query
            updateSQL.sqlInsertDelete(sqlQuery)
    
