import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv
from tkinter import ttk
from customtkinter import * 
import customtkinter
from PIL import Image, ImageTk
import os
import re

# Set appearance mode for the entire application
set_appearance_mode("dark")

class MainApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("Main App")
        self.geometry("600x400")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)# Bind the close window event to the on_closing method
        self.frame = Signup(self)  # Set the first frame to appear here
        self.frame.pack(fill="both", expand=True)
    
    ''' Dihein '''
    #Input: frame(the current frame)
    #process: Deletes the current frame and replaces it with a new one
    #Output: The new frame that was picked
    def change(self, frame_class):
        self.frame.pack_forget()  # Remove the current frame
        self.frame = frame_class(self)
        self.frame.pack(fill="both", expand=True)  # Display the new frame

    ''' Dihein '''
    #Input: On mouse click/when the user tries to close the window.
    #Process: displays a messagebox if they wanna close the window and if ok is pressed it closes the window otherwise.
    #Output: self.destroy(), it destroys the window when ok is clicked
    def on_closing(self):
        """Handle the close window event"""
        if messagebox.askokcancel("Quit", "Are you sure you want to close this window?"):
            self.destroy()  # Close the window if the user confirms

class Signup(CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        # Create the Sign-Up window
        master.title("Sign-Up Page")
        self.pack(pady = 20, padx = 40, fill= 'both', expand = True)

        # Create the Sign-Up Page labels
        self.titleLbl = CTkLabel(self, text="Sign Up", font=("Helvetica", 30))
        self.titleLbl.grid(row=0, column=1, columnspan=1, pady=5, sticky = "n", padx=(150, 5))

        # Create the Sign-Up Page entry boxes
        self.nameEnt = CTkEntry(self ,placeholder_text="Name")
        self.nameEnt.grid(row = 1, column = 1, pady = 5, padx=(150, 5))
        self.nameEnt.bind("<Key>", self.clickName)

        self.emailEnt = CTkEntry(self,placeholder_text="Email")
        self.emailEnt.grid(row=2, column=1, pady=5, padx=(150, 5))
        self.emailEnt.bind("<Key>", self.clickEmail)

        self.passwordEnt = CTkEntry(self, show="*",placeholder_text="Password")
        self.passwordEnt.grid(row=3, column=1, pady=5, padx=(150, 5))
        self.passwordEnt.bind("<Key>", self.clickpassword)

        self.passwordConfirmEnt = CTkEntry(self, show="*",placeholder_text="Confirm Password")
        self.passwordConfirmEnt.grid(row=4, column=1, pady=10, padx=(150, 5))
        self.passwordConfirmEnt.bind("<Key>", self.clickconfirmpassword)

        #load the images
        file_path = os.path.dirname(os.path.realpath(__file__))
        self.image_1 = customtkinter.CTkImage(Image.open(file_path +
                                            "/view.png"), size=(20, 20))
        self.image_2 = customtkinter.CTkImage(Image.open(file_path +
                                            "/hide.png"), size=(20, 20))
        # Create the Sign-Up Page buttons
        self.loginbtn = CTkButton(self, text="Already have an account? Login", command=self.login)
        self.loginbtn.grid(row=6, column=1, pady=10, padx=(150, 5), sticky = "n")

        self.signUpBtn = CTkButton(self, text="Sign Up", command=self.booking, width=40)
        self.signUpBtn.grid(row=7, column=1, pady=10, padx=(210, 5), sticky = "n")

        self.clearBtn = CTkButton(self, text = "Clear", command = self.clear, fg_color='red', hover_color='darkred', width=50)
        self.clearBtn.grid(row = 7, column = 1, padx = (90,5))

        # self.click_btn= PhotoImage(file='ShowPassword.png')
        self.showBtn = customtkinter.CTkButton(self, text = "",image=self.image_1, height=20, width = 20,command=self.show)
        self.showBtn.grid(row=3, column=1 , padx = (320, 3))
        

        # Bind enter key to booking function
        self.nameEnt.bind("<Return>", self.booking)
        self.emailEnt.bind("<Return>", self.booking)
        self.passwordEnt.bind("<Return>", self.booking)
        self.passwordConfirmEnt.bind("<Return>", self.booking)

    ''' Blaine '''
    #Input: nameEnt, emailEnt, passwordEnt, passwordConfirmEnt
    #process: deletes anything within the entry fields and activates the placeholder text
    #Output: the entry boxes get cleared and placeholder text is outputted
    def clear(self):
        self.nameEnt.delete(0, 'end')
        self.nameEnt._activate_placeholder()
        self.emailEnt.delete(0, 'end')
        self.emailEnt._activate_placeholder()
        self.passwordEnt.delete(0, 'end')
        self.passwordEnt._activate_placeholder()
        self.passwordConfirmEnt.delete(0, 'end')
        self.passwordConfirmEnt._activate_placeholder()
        self.master.focus()

    ''' Blaine '''
    #Input: passwordEnt, passwordConfirmEnt
    #process: allows the user to see their password and confirmpassword text
    #Output: the revealed text in the entry boxes
    def show(self):
        self.passwordEnt.configure(show='')
        self.passwordConfirmEnt.configure(show='')
        self.showBtn.configure(command=self.hide)
        self.showBtn.configure(image = self.image_2)

    ''' Blaine '''
    #Input: passwordEnt, passwordConfirmEnt
    #Process: allows the user to hide their password and confirmpassword text
    #Output: hides the text within the entry field
    def hide(self):
        self.passwordEnt.configure(show='*')
        self.passwordConfirmEnt.configure(show='*')
        self.showBtn.configure(command=self.show)
        self.showBtn.configure(image = self.image_1)

    ''' Blaine '''
    #Input: Loginpage
    #Process: changes the frame from signup page to login page
    #Output: the current frame becomes LoginPage frame
    def login(self, event=None):
        self.master.change(Loginpage)

    ''' Blaine '''
    #Input: clickName, clickEmail, clickpassword, clickconfirmpassword
    #Process: It sets the border colors back to default if any validaiton errors occurred
    #Output: The clickName, clickEmail, clickpassword, clickconfirmpassword all have there border colors changed
    def clickName(self, key):
        self.nameEnt.configure(border_color='') 
    def clickEmail(self, key):
        self.emailEnt.configure(border_color='')
    def clickpassword(self, key):
        self.passwordEnt.configure(border_color='')
    def clickconfirmpassword(self, key):
        self.passwordConfirmEnt.configure(border_color='')

    ''' Blaine and Dihein'''
    #Input: nameEnt, emailEnt, passwordEnt, passwordConfirmEnt
    #Process: Has validation for the entries (if there are anything wrong it displays a messagebox with the errors) and then saves the signup details to a 
    # BookingWebsiteDetails.csv (plus it also checks whether the details are already registered) and changes them to the BookingPage frame.
    #Output: the errors in a list(inside a messagebox) then writes to a csv and changes the frame (to BookingPage frame)(data type is a string with integers)
    def booking(self, event=None):
        errorsLst = []
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        email = self.emailEnt.get().lower()
        if not self.nameEnt.get().isalpha() or self.nameEnt.get() == '':
            errorsLst.append('Please Input a Name with alphabetic characters only')
            self.nameEnt.configure(border_color="red")
        if not re.match(pat, email) or email == '':
            errorsLst.append('Please input a valid email')
            self.emailEnt.configure(border_color="red")
        if self.passwordEnt.get() == '':
            errorsLst.append('Please a input password')
            self.passwordEnt.configure(border_color="red")
        if self.passwordConfirmEnt.get() != self.passwordEnt.get() or self.passwordConfirmEnt.get() == '':
            errorsLst.append('Passwords do not match')
            self.passwordConfirmEnt.configure(border_color="red")

        with open('BookingWebsiteDetails.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            my_dict = {k: v for k, v in reader}

        error_message = "\n".join(errorsLst)

        if email not in my_dict:
            if error_message:
                messagebox.showerror("Error", error_message)
            else:
                with open("BookingWebsiteDetails.csv", mode="a", newline="") as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([email, self.passwordEnt.get()])
                self.master.change(Bookingpage)
        else:
            messagebox.showerror("Error", "Account already exists")

class Loginpage(CTkFrame):#To input the user's unique information to access their flight info and other things the website offer
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        #create the title and pack the frame
        master.title("Login Page")
        self.pack(pady = 20, padx = 40, fill= 'both', expand = True)
        
        #create the labels
        self.titleLbl = CTkLabel(self, text="Login", font=("Helvetica", 30))
        self.titleLbl.grid(row=0, column=1, columnspan=1, pady=5, padx=(150, 5), sticky = "n")

        #create the entry fields
        self.emailEnt = CTkEntry(self, placeholder_text="Email")
        self.emailEnt.grid(row=1, column=1, pady=5, padx=(150, 5), sticky = "n")
        self.emailEnt.bind("<Key>", self.clickEmail)

        self.passwordEnt = CTkEntry(self, show="*", placeholder_text="Password")
        self.passwordEnt.grid(row=2, column=1, pady=5, padx=(150, 5), sticky = "n")
        self.passwordEnt.bind("<Key>", self.clickpassword)

        #load the images
        file_path = os.path.dirname(os.path.realpath(__file__))
        self.image_1 = customtkinter.CTkImage(Image.open(file_path +
                                            "/view.png"), size=(20, 20))
        self.image_2 = customtkinter.CTkImage(Image.open(file_path +
                                            "/hide.png"), size=(20, 20))
        
        #create the buttons
        self.backBtn = CTkButton(self, text="Don't have an account? Sign Up", command=self.back)
        self.backBtn.grid(row=3, column=1, pady=10, padx=(150, 5), sticky = "n")

        self.signUpBtn = CTkButton(self, text="Log In", command=self.booking, width=40)
        self.signUpBtn.grid(row=4, column=1, pady=10, padx=(210, 5), sticky = "n")

        self.showBtn = CTkButton(self, text="",image=self.image_1,height=20, width = 20, command=self.show)
        self.showBtn.grid(row=2, column=1, sticky = "e")

        self.clearBtn = CTkButton(self, text = "Clear", command = self.clear, fg_color='red', hover_color='darkred', width = 50)
        self.clearBtn.grid(row = 4, column = 1, padx = (90, 5))

        #bind entry boxes to enter
        self.emailEnt.bind("<Return>", self.booking)
        self.passwordEnt.bind("<Return>", self.booking)

    ''' Harsha '''
    #Input: emailEnt, passwordEnt
    #process: deletes anything within the entry fields and activates the placeholder text
    #Output: the entry boxes get cleared and placeholder text is outputted
    def clear(self):
        self.emailEnt.delete(0, 'end')
        self.emailEnt._activate_placeholder()
        self.passwordEnt.delete(0, 'end')
        self.passwordEnt._activate_placeholder()
        self.master.focus()

    ''' Harsha '''
    #Input: passwordEnt
    #process: allows the user to see their password text
    #Output: the revealed text in the entry boxes
    def show(self):
        self.passwordEnt.configure(show='')
        self.showBtn.configure(image = self.image_1, command=self.hide)

    ''' Harsha '''
    #Input: passwordEnt
    #Process: allows the user to hide their password text
    #Output: hides the text within the entry field
    def hide(self):
        self.passwordEnt.configure(show='*')
        self.showBtn.configure(image = self.image_2, command=self.show)

    ''' Harsha '''
    #Input: clickEmail, clickpassword
    #Process: It sets the border colors back to default if any validaiton errors occurred
    #Output: The clickEmail, clickpassword all have there border colors changed
    def clickEmail(self, key):
        self.emailEnt.configure(border_color='')
    def clickpassword(self, key):
        self.passwordEnt.configure(border_color='')

    ''' Harsha and Dihein'''
    #Input: emailEnt, passwordEnt
    #Process: Has validation for the entries (if there are anything wrong it displays a messagebox with the errors) and then reads
    # from the BookingWebsiteDetail.csv and changes the current frame to the BookingPage frame.
    #Output: the errors in a list(inside a messagebox) then reads from a csv and changes the frame (to BookingPage) (data type is a string with integers)
    def booking(self, event=None):
        errorsLst = []
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        email = self.emailEnt.get().lower()
        if not re.match(pat, email) or email == '':
            errorsLst.append('Please input a valid email')
            self.emailEnt.configure(border_color = "red")
        if self.passwordEnt.get() == '':
            errorsLst.append('Please input a password')
            self.passwordEnt.configure(border_color = "red")

        error_message = "\n".join(errorsLst)

        if error_message:
            messagebox.showerror("Error", error_message)
        else:
            with open('BookingWebsiteDetails.csv', 'r') as f:
                reader = csv.reader(f, delimiter=',')
                my_dict = {k: v for k, v in reader}

            if email not in my_dict:
                messagebox.showerror("Error", "No account with this email")
                self.emailEnt.configure(border_color = "red")
            elif my_dict[email] == self.passwordEnt.get():
                self.master.change(Bookingpage)
            else:
                messagebox.showerror("Error", "Incorrect password")
                self.passwordEnt.configure(border_color = "red")
    
    ''' Harsha '''
    #Input: frame(the current frame)
    #Process: It changes the frame from LoginPage to Signup
    #Output: current frame changes to SignupPage
    def back(self):
        self.master.change(Signup)

class Bookingpage(CTkFrame):#the booking page to select what flight options the user wants
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        master.title("Booking Page")
        master.geometry("1200x800")

        self.x = tk.StringVar()
        self.y = tk.StringVar()
        self.z = tk.StringVar()
        self.v = tk.StringVar(value="Select a budget")
        options_list = ["$200-$300", "$301-$400", "$401-$500", "$501-$600", "$601-$700", "$701-$800", "$801-$900", "$901-$1000"]

        # Create the label
        self.titleLbl = CTkLabel(self, text='Booking Page', font=("Arial", 20))
        self.titleLbl.grid(row=0, column=0, columnspan=4, pady=20)

        self.planeLbl = CTkLabel(self, text='Airline:')
        self.planeLbl.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.fromLbl = CTkLabel(self, text='From (place):')
        self.fromLbl.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.toLbl = CTkLabel(self, text='To (place):')
        self.toLbl.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        self.budgetLbl = CTkLabel(self, text='Budget:')
        self.budgetLbl.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        self.infoLbl = CTkLabel(self, text = "Note: Select on the desired Airline to book ⮧", fg_color='red')
        self.infoLbl.grid(row = 3, column = 2, padx = 10)

        # Create the entry boxes
        self.planeEnt = CTkEntry(self, textvariable=self.x)
        self.planeEnt.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.fromEnt = CTkEntry(self, textvariable=self.y)
        self.fromEnt.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.toEnt = CTkEntry(self, textvariable=self.z)
        self.toEnt.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

        self.budgetDrp = CTkOptionMenu(self, values=options_list, variable=self.v)
        self.budgetDrp.grid(row=2, column=3, padx=10, pady=10, sticky="ew")

        # Create the buttons
        self.backBtn = CTkButton(self, text="Want to Login?", command=self.back)
        self.backBtn.grid(row=5, column=1, padx=10, pady=10)

        self.searchBtn = CTkButton(self, text="Search", command=self.search)
        self.searchBtn.grid(row=3, column=1, padx=10, pady=10)

        self.planeEnt.bind("<Return>", self.search)
        self.fromEnt.bind("<Return>", self.search)
        self.toEnt.bind("<Return>", self.search)


        # Create the output for search results
        self.tv = ttk.Treeview(self, columns=('col_1', 'col_2', 'col_3', 'col_4'), show='headings', height = 30)
        self.tv.column('col_1', minwidth=0, width=700)
        self.tv.column('col_2', minwidth=0, width=300)
        self.tv.column('col_3', minwidth=0, width=300)
        self.tv.column('col_4', minwidth=0, width=350)

        self.tv.heading('col_1', text='AIRLINE')
        self.tv.heading('col_2', text='FROM')
        self.tv.heading('col_3', text='TO')
        self.tv.heading('col_4', text='PRICE')

        self.tv.grid(row=4, column=0, columnspan=4)
        self.tv.bind("<<TreeviewSelect>>", self.on_treeview_select) #bind the click to the treeview
        self.load_initial_data()#load inital booking data

        #create the scroll bar
        scrollBar = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview)
        scrollBar.grid(row=4, column=4, sticky='NS')
        self.tv.configure(yscrollcommand=scrollBar.set)
 
        #configure the highlight row colour
        self.tv.tag_configure('highlight', background='lightblue')
        self.tv.bind("<Motion>", self.highlight_row)

    ''' Dihein '''
    #Input: self.tv
    #Process: It highlights the row you are currently hovering within the treeview
    #Output: Outputs the self.tv.tk.call which allows it to highlight the row currently hovered (data type is string)
    def highlight_row(self, event):
        self.tv = event.widget
        item = self.tv.identify_row(event.y)
        self.tv.tk.call(self.tv, "tag", "remove", "highlight")
        self.tv.tk.call(self.tv, "tag", "add", "highlight", item)

    ''' Dihein '''
    #Input: loads the csv file SearchCheck.csv
    #Process: It loads all the data into the treeview when u first load the frame
    #Output: It outputs the data from the csv into the treeview(data type is a string)
    def load_initial_data(self):
        file = r'C:\Users\thush\OneDrive\Desktop\Python\SearchCheck.csv'

        with open(file, 'r') as f:
            csvreader = csv.reader(f)
            csvreader_list = list(csvreader)

        for (i, n, f, g) in csvreader_list:
            self.tv.insert('', 'end', values=(i, n, f, g))

    ''' Dihein '''
    #Input: planeEnt, fromEnt, toEnt
    #Process: Has validation for the entries (if there are anything wrong it displays a messagebox with the errors) and then searchs through the SearchCheck.csv to
    # find anything that matches the inputs (if nothing matches a error is displayed) and if it does match up the corresponding searches are displayed in the treeview.
    #Output: the errors in a list(inside a messagebox) and displays the corresponding results for the search and then deletes the contents of the entry fields(data type outputted is a list of strings)
    def search(self, event=None):
        errorsLst = []
        if self.planeEnt.get().isnumeric():
            errorsLst.append('Please input a valid Airline')
            self.planeEnt.configure(border_color="red")
        if self.fromEnt.get().isnumeric():
            errorsLst.append('Please input a proper origin')
            self.fromEnt.configure(border_color="red")
        if self.toEnt.get().isnumeric():
            errorsLst.append('Please input a proper destination')
            self.toEnt.configure(border_color="red")

        error_message = "\n".join(errorsLst)

        if error_message:
            messagebox.showerror("Error", error_message)
        else:
            file = r'C:\Users\thush\OneDrive\Desktop\Python\SearchCheck.csv'

            with open(file, 'r') as f:
                csvreader = csv.reader(f)
                csvreader_list = list(csvreader)

            self.tv.delete(*self.tv.get_children())
            word = self.x.get().strip().lower()  # Convert to lowercase and remove extra spaces
            word1 = self.y.get().strip().lower()
            word2 = self.z.get().strip().lower()
            word3 = self.v.get()

            budgetMin, budgetMax = self.get_budget_range(word3)
            result_found = False  # Initialize a flag to check if any result is found

            for (i, n, f, g) in csvreader_list:
                try:
                    price = int(g.replace('$', ''))
                except ValueError:
                    continue  # Skip rows with invalid price values

                match = True

                if word and word not in i.lower():  # Convert data to lowercase before comparing
                    match = False
                if word1 and word1 not in n.lower():
                    match = False
                if word2 and word2 not in f.lower():
                    match = False
                if budgetMin > price or price > budgetMax:
                    match = False

                if match:
                    self.tv.insert('', 'end', values=(i, n, f, g))
                    result_found = True  # Set the flag to True if a match is found

            if not result_found:
                messagebox.showinfo("No Results", "Nothing matches your search results.")

            self.planeEnt.delete(0, 'end')
            self.toEnt.delete(0, 'end')
            self.fromEnt.delete(0, 'end')
            self.v.set("Select a budget")

    ''' Dihein '''
    #Input: budgetStr
    #Process: gets the users choice in the budgetDrp and splits it up into two parts which are then put into budgetMin and budgetMax
    #Output: budgetMin and budgetMax are outputted as integers(data type is a string)
    def get_budget_range(self, budgetStr):
        if budgetStr == "Select a budget":
            return (0, float('inf'))
        budget_range = budgetStr.split('-')  # Splits the budget range into two parts from the hyphen
        budgetMin = int(budget_range[0].replace('$', ''))
        budgetMax = int(budget_range[1].replace('$', ''))
        return (budgetMin, budgetMax)

    ''' Dihein '''
    #Input: frame(the current frame)
    #Process: It changes the frame from BookingPage to LoginPage
    #Output: current frame changes to LoginPage
    def back(self):
        self.master.change(Loginpage)

    ''' Dihein ''' 
    #Input: self.tv
    #Process: It takes what the user selected/clicked in the treeview and displays the airline, to, from and price in a detailWindow which also containts a Book button
    # when pressed displays a messagebox confirming their flight details.
    #Output: msgBox(which is there flight details)(data type is also a string as it outputs a messagebox)
    def on_treeview_select(self, event):
        selection = self.tv.selection()
        if selection:
            # There is an item selected
            selectedItem = selection[0]
            itemValues = self.tv.item(selectedItem, 'values')
            
            # Create the flight detail window only if there is a valid selection
            deatilWindow = CTkToplevel(self)
            deatilWindow.title("Flight Details")
            deatilWindow.geometry("400x200")

            #Input: If the book button is pressed
            #Process: It sends out a messagebox and then destroys the window when messagebox is closed
            #Output: messagebox
            def book():
                msgBox = messagebox.showinfo("Booked", f"The {itemValues[0]} plane from {itemValues[1]} to {itemValues[2]} has been booked\n{itemValues[3]} has been charged to your card\nFurther flight details have been sent to your email")
                if msgBox == "ok":
                    deatilWindow.destroy()
                    deatilWindow.update()
                    
            # Create the buttons
            bookBtn = CTkButton(deatilWindow, text="Book", command=book)
            bookBtn.pack(pady=5)
            
            # Display the details
            details = ["Airline: " + itemValues[0],
                    "From: " + itemValues[1],
                    "To: " + itemValues[2],
                    "Price: " + itemValues[3]]

            for idx, detail in enumerate(details):
                label = CTkLabel(deatilWindow, text=detail, font=("Arial", 12))
                label.pack(pady=5)
        else:
            # Handle the case where no item is selected
            itemValues = None


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()