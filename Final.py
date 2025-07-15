from datetime import date
import tkinter as tk           #our GUI library
from tkinter import messagebox      #Messagebox to display messages and errors
import pyttsx3                  #Library for voice output
import matplotlib.pyplot as plt       #library to plot Graphs For Data Analysis

users = {"admin":"1234","Arsal":"1999","Turrab":"1199","Abdullah":"1119"} #Dictionary to store accounts
events =[] #Main list to store Multiple Events As Sublists

#Creation Of the main login/signup window 
def login_signup_window(): 
    def login(): #inside Function to login
        username = username_entry.get() #Enter the username
        password = password_entry.get() #Enter the Password
        if users.get(username) == password:
            '''This condition checks wether the key username is in users library and its 
            corresponding key password is the same'''   
            messagebox.showinfo("Login Successful!"," Welcome")  #messagebox is used here to show info
            login_window.destroy()   # login window is destroyed here 
            Open_main_window()       # and the Main window is called  
        else:
            messagebox.showerror("Error :" ,"Invalid Username or Password!") #messagebox is used here
    def signup(): #inside function to sign up
        username = username_entry.get() #Enter username 
        password = password_entry.get() #Enter password
        if username in users: 
            ''' this condition checks wether username is in the dictionary users
            and if it is present it will show error saying that this username already exists '''
            messagebox.showerror("Error","This name already exists")
        elif not username or not password:
            '''If username or password or both of the fields are empty it will show
            error using messagebox'''
            messagebox.showerror("The fields cannot be empty")
        else:
            '''Here The entered username and passwords are put into the dictionary as
            key value pairs '''
            users[username] = password
            messagebox.showinfo("Signup successful", "Welcome!")

    login_window = tk.Tk()  #Creates A login window
    login_window.title("Login/Signup")  #The login window has title "Login/Signup"
    login_window.geometry('400x350')    #The length of login window is 400 with 350 width

    tk.Label(login_window,text="Username").pack(pady = 5) 
    #Username label is created and added on login window 
    username_entry = tk.Entry(login_window) 
    username_entry.pack(pady=5)
    #Entery widget to enter username is Created and added on login window
   
    tk.Label(login_window,text="Password").pack(pady = 5)
    #Password Label is Created and added on login window
    password_entry = tk.Entry(login_window,show='*')
    password_entry.pack(pady=5)
    #Entery widget to enter password is created and added on login window

    tk.Button(login_window, text="Sign Up", command=signup, width = 10,bg='blue',fg='white').pack(pady=5)
    #Button which calls the singup functions and saves the username and password
    tk.Button(login_window, text="login" , command=login, width= 10,bg='blue',fg='white').pack(pady =5)
    #Button widget which calls the login function and checks the login and password 
    
    login_window.mainloop() #uses mainloop function to keep the login window open

#Function for voice Output
def speak_events(event):
    engine = pyttsx3.init()  
    engine.setProperty('rate',150)  #Set the Speed of the Output
    engine.setProperty('volume',1.0)  #Sets the Volume
    engine.say(event)                
    engine.runAndWait()

#Function To Analyse and Plot the Graph of Given Data
def plot_graph(Graph_index,title,ylabel):  
    if not events:
        messagebox.showerror("No event","No event to Display")
        return
    graph_name = [event[0] for event in events] #This List Comprehension finds the Name of event
    Index_value = [event[Graph_index] for event in events] #This list Comprehension finds information like budget,etc
    plt.figure(figsize=(8,5))  #This sets the dimensions of the figure
    plt.bar(graph_name, Index_value, color = 'red') #Bar Graph is plotted with color red
    plt.title(title)   #title of the Graph
    plt.xlabel("Event Name")  #X label beneath the bar Graph
    plt.ylabel(ylabel)  
    plt.show()

#Function For the main window
def Open_main_window():
    root = tk.Tk() #Creates the main application window
    root.title("Event Management System")  #Titles the Window as Event Management System
    root.geometry('300x400') #sets the Length as 3oo and width as 400
    #Sub Function to add details
    def Add_details():
        #Sub Funtion to save the details in the list
        def save_details():
            #Taking input
            event_name = event_name_entry.get()
            guests = guests_entry.get()
            attendee = atendee_entry.get()
            event_date = event_date_entry.get()
            venue = venue_entry.get()
            budget = budget_entry.get()
            ticket_price = ticket_price_entry.get()

            #checking the input
            if not event_date or not event_name or not guests or not attendee or not venue or not budget or not ticket_price:
                messagebox.showerror("Error!","Please fill out the full form!")
                return
            #assigning data type to the inputs
            try:
                guests = int(guests)
                attendee = int(attendee)
                budget = int(budget)
                ticket_price = int(ticket_price)
                event_date_obj = date.fromisoformat(event_date) #When in specific format string becomes obj
            except ValueError:
                messagebox.showerror("Invalid Input!","Please check Your Enteries!!!")
                return
            
            '''This line finds the profit of the event considering the number of attendee, ticket price
            and the total budget spent on the event'''
            profit = (ticket_price*attendee) - budget
            #Storing all the event details in the events list as a list using append function
            events.append([event_name,guests,attendee,event_date_obj,venue,budget,ticket_price,profit])
            messagebox.showinfo("Success",f"Event with the name {event_name} has been added successfully")
            add_window.destroy() #destroying this window after adding the events

        add_window = tk.Toplevel(root) #A new window to add events is created
        add_window.title("Add Details") #its title
        add_window.geometry('400x500') #dimensions

        '''Here below the lines of code consists of Graphical interface which take input and
        then are attached to the add window using geometric organizers'''
        tk.Label(add_window,text='Event Name: ').pack(pady=5) 
        event_name_entry = tk.Entry(add_window)
        event_name_entry.pack(pady=5)

        tk.Label(add_window,text="Number of Guests: ").pack(pady=5)
        guests_entry = tk.Entry(add_window)
        guests_entry.pack(pady=5)

        tk.Label(add_window,text="Number of Atendee: ").pack(pady=5)
        atendee_entry = tk.Entry(add_window)
        atendee_entry.pack(pady=5)

        tk.Label(add_window,text="Date of the Event YYYY-MM-DD: ").pack(pady=5)
        event_date_entry = tk.Entry(add_window)
        event_date_entry.pack(pady=5)
        
        tk.Label(add_window,text="Enter the Venue: ").pack(pady=5)
        venue_entry = tk.Entry(add_window)
        venue_entry.pack(pady=5)
        
        tk.Label(add_window,text="Enter the Budget: ").pack(pady=5)
        budget_entry = tk.Entry(add_window)
        budget_entry.pack(pady=5)

        tk.Label(add_window,text="Enter the Ticket Price: ").pack(pady=5)
        ticket_price_entry = tk.Entry(add_window)
        ticket_price_entry.pack(pady=5)

        '''This button calls the Save_details function which was created above and appends the details 
        to the main list events as a sublist'''
        tk.Button(add_window,text="Save Event",bg='blue',fg='white',command=save_details).pack(pady=10)
        
    #Sub_list to Display the event
    def show_event():
        #Shows info if not event is present
        if not events:
            messagebox.showinfo("No Events", "No events to display!")
            return
        
        events_window = tk.Toplevel(root) #creating a window for the display of events
        events_window.title("All Events") 
        events_window.geometry("400x300") #Dimensions

        for idx, event in enumerate(events, start=1):
            event_details = (
                f"Event {idx}: {event[0]} - Guests: {event[1]}, Attendees: {event[2]}, "
                f"Date: {event[3]}, Venue: {event[4]}, Budget: {event[5]},"
                f"Ticket-Price: {event[6]} Profit: {event[7]}"
            )
            #This label Displays the Events inside the Event Window 
            tk.Label(events_window, text=event_details, wraplength=350, justify="left").pack(pady=5)
    
    #Function To delete an event
    def delete_event():
        if not events:
            messagebox.showinfo("No events","There is no event Present to delete!")
            return
        
        def Conf_delete():
            try:
                '''Takes the number of Event and subtracts 1 because indexing starts from
                0'''
                idx = int(event_index_entry.get()) -1 
                if 0<= idx < int(len(events)): #A check for the Entered number
                    deleted_event = events.pop(idx) #Delets the sublist
                    messagebox.showinfo("Success",f"Deleted Event: {deleted_event[0]}")
                    delete_window.destroy()
                else:
                    messagebox.showerror("Error!","Invalid number!")
            except ValueError:
                messagebox.showerror("Error!","Enter a valid Event Number!")

        delete_window = tk.Toplevel(root)   #Creates a New window
        delete_window.title('Delete Event') 
        delete_window.geometry('300x300')

        tk.Label(delete_window, text="Enter Event Number to Delete:").pack(pady=5)
        event_index_entry = tk.Entry(delete_window)
        event_index_entry.pack(pady=5)

        #Button To call the Conf_delete function
        tk.Button(delete_window, text="Delete", command=Conf_delete,bg='blue',fg='white').pack(pady=10)
    
    '''As per the guidelines we played around with a new library pyttsx3 to add an interesting feature
    in our program. This will take the event number as an input and then it will speak that event.'''
    def speak_event():
        if not events:
            messagebox.showinfo("No Events", "No events to speak!")
            return

        def speak_selected_event():
            try:
                idx = int(event_idx_entry.get()) - 1
                if 0 <= idx < len(events):
                    event = events[idx]
                    text = (
                        f"The event {event[0]} is being held on {event[3]}. "
                        f"There are {event[1]} guests and {event[2]} attendees. "
                        f"The venue is {event[4]}. "
                        f"The budget is {event[5]} rupees"
                        f"the price of the ticket is {event[6]} and the profit is {event[7]} rupees."
                    )
                    speak_events(text) #This calls the function we declared above
                    messagebox.showinfo("Speaking", f"Speaking details of event: {event[0]}")
                    speak_window.destroy()
                else:
                    messagebox.showerror("Error", "Invalid event number!")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number!")

        speak_window = tk.Toplevel(root) #New window to display the speak event
        speak_window.title("Speak Event")
        speak_window.geometry("300x150")

        tk.Label(speak_window, text="Enter Event Number to Speak:").pack(pady=5)
        event_idx_entry = tk.Entry(speak_window) #Enter the number of event
        event_idx_entry.pack(pady=5)

        tk.Button(speak_window, text="Speak", command=speak_selected_event,bg='blue',fg='white').pack(pady=10)

    #These are the buttons on the root window which will perfrom main actions
    tk.Label(root, text="Event Management System", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="Add Event", command=Add_details, width=20,bg='blue',fg='white').pack(pady=10)
    tk.Button(root, text="Show Events", command=show_event, width=20,bg='blue',fg='white').pack(pady=10)
    tk.Button(root, text="Delete Event", command=delete_event, width=20,bg='blue',fg='white').pack(pady=10)
    tk.Button(root, text="Speak Event Details", command=speak_event, width=20,bg='blue',fg='white').pack(pady=10)
    tk.Button(root, text="Plot Costs", command=lambda: plot_graph(5, "Event Budgets", "Budget (Rupees)"), width=20,bg='blue',fg='white').pack(pady=10)
    tk.Button(root, text="Plot Guests", command=lambda: plot_graph(1, "Event Guests", "Number of Guests"), width=20,bg='blue',fg='white').pack(pady=10)
    tk.Button(root, text="Plot Atendees", command=lambda: plot_graph(2, "Event Atendees", "Number of Atendee"), width=20,bg='blue',fg='white').pack(pady=10)
    tk.Button(root, text="Plot Profits", command=lambda: plot_graph(7, "Event Profits", "Profit (Rupees)"), width=20,bg='blue',fg='white').pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit, width=20, bg="red", fg="white").pack(pady=20)

    root.mainloop() #Looping the root window which will be our main window

#start of the program
#calling the Signup window
login_signup_window()
