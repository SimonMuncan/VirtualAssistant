from assistantGUI import *
import re, datetime

class CommandStrategy:
    def execute(self,main_window, command):
        pass

class ShowAllAppointments(CommandStrategy):
    def execute(self,main_window, command):
        # Regular expression pattern for matching the command
        pattern = re.compile("show my (one time|reccuring) appointments",re.IGNORECASE) 
        if pattern.match(command): 
            # Extract the type of appointment from the command
            get_type_of_appointment = re.search("(one time|reccuring)",command,re.IGNORECASE)
            # Clear the contents of the main window
            main_window.view.clearContents()
            if "one time" in get_type_of_appointment[0]:
                # SQL query to fetch one-time appointments
                sql_query = f"SELECT * FROM AppointmentsOneTime ORDER BY TimeStart"
                # Show one-time appointments in the main window
                main_window.showOneTimeAppointments(sql_query)
            elif "reccuring" in get_type_of_appointment[0]:
                # SQL query to fetch recurring appointments
                sql_query = f"SELECT * FROM AppointmentsReccuring ORDER BY TimeStart"
                # Show recurring appointments in the main window
                main_window.showRecurringAppointments(sql_query)

# Strategy for showing appointments for a specific date (today, tomorrow, or specified date)
class ShowAppointments(CommandStrategy):
    def execute(self,main_window, command):
        # Regular expression pattern for matching the command
        pattern = re.compile("show my appointments for (today|tomorrow|(.*))",re.IGNORECASE) 
        if pattern.match(command):
            # Extract the date from the command 
            get_date = re.search("(today|tomorrow)",command,re.IGNORECASE)
            if get_date is None:
                get_date = "none"
            date = ""
            if "today" in get_date[0]:
                date = datetime.date.today()
            elif "tomorrow" in get_date[0]:
                date = datetime.date.today() + datetime.timedelta(1)
            else:                       # 2023-01-15     
                # Extract specified date in the format YYYY-MM-DD            
                date_get = re.findall(r"[\d]{4}-[\d]{1,2}-[\d]{1,2}",command)
                for s in date_get:
                    date += s
            # Check if the date is valid
            res = True
            try: 
                res = bool(datetime.datetime.strptime(str(date), "%Y-%m-%d"))
                if res:
                    # Clear the contents of the main window
                    main_window.view.clearContents()
                    # Show appointments for the specified date in the main window
                    main_window.showAppointmentsDate(date)
            except ValueError:
                # Show error dialog for wrong date format
                main_window.dialogErorr("Wrong format of date!")
            
