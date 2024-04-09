from assistantGUI import *
import re

class CommandStrategy:
    def execute(self,main_window, command):
        pass
    
# Strategy for showing the schedule for a specific day
class ShowSchedule(CommandStrategy):
    def execute(self,main_window, command):
        # Regular expression pattern for matching the command
        pattern = re.compile("show my schedule for (Monday|Tuesday|Wednesday|Thrusday|Friday|Saturday|Sunday|work)",re.IGNORECASE) 
        if pattern.match(command):
            # Extract the day from the command 
            get_a_day = re.search("(Monday|Tuesday|Wednesday|Thrusday|Friday|Saturday|Sunday|work)",command,re.IGNORECASE)
            # Clear the contents of the main window
            main_window.view.clearContents()
            # SQL query to fetch the schedule for the specified day
            sql_query = f"SELECT * FROM {get_a_day[0]} ORDER BY TimeStart"
            print(sql_query)
            # Show the schedule in the main window
            main_window.showSchedule(sql_query)
        
# Strategy for showing the schedule for a specific activity
class ShowActivitySchedule(CommandStrategy):
    def execute(self,main_window, command):
        # Regular expression pattern for matching the command
        pattern = re.compile("show my (.*) schedule",re.IGNORECASE) 
        if pattern.match(command): 
            # Extract the activity from the command
            get_an_activity = pattern.match(command).groups(1)
            # Clear the contents of the main windo
            main_window.view.clearContents()
            # SQL query to fetch the schedule for the specified activity across all days
            sql_query = f"""
                        SELECT * FROM (
                            SELECT * FROM Monday WHERE LOWER(TRIM(Activity)) = LOWER(TRIM('{get_an_activity[0]}'))
                            UNION 
                            SELECT * FROM Tuesday WHERE LOWER(TRIM(Activity)) = LOWER(TRIM('{get_an_activity[0]}'))
                            UNION 
                            SELECT * FROM Wednesday WHERE LOWER(TRIM(Activity)) = LOWER(TRIM('{get_an_activity[0]}'))
                            UNION 
                            SELECT * FROM Thursday WHERE LOWER(TRIM(Activity)) = LOWER(TRIM('{get_an_activity[0]}'))
                            UNION 
                            SELECT * FROM Friday WHERE LOWER(TRIM(Activity)) = LOWER(TRIM('{get_an_activity[0]}'))
                            UNION 
                            SELECT * FROM Saturday WHERE LOWER(TRIM(Activity)) = LOWER(TRIM('{get_an_activity[0]}'))
                            UNION 
                            SELECT * FROM Sunday WHERE LOWER(TRIM(Activity)) = LOWER(TRIM('{get_an_activity[0]}'))
                        ) AS combined_tables"""
            print(sql_query)
            # Show the activities in the main window
            main_window.ShowActivities(sql_query)
        