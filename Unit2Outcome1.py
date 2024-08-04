import tkinter as tk
from tkinter import messagebox
import csv
from tkinter import ttk

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = Signup(self) # set first frame to appear here
        self.frame.pack()

    def change(self, frame):
        self.frame.pack_forget() # delete currrent frame
        self.frame = frame(self)
        self.frame.pack() # make new frame

class Signup(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        
        master.title("Sign-Up Page")
        master.geometry("600x400")
                
            
        #create the labels
        self.Titlelbl = tk.Label(self, text ="Sign Up Page", font = ("Arial", 15))
        self.Titlelbl.grid(row = 0, column = 0, pady = 5, sticky = "N")

        self.namelbl = tk.Label(self, text = "Name: ")
        self.namelbl.grid(row = 1, column = 0, sticky = "w")

        self.emaillbl = tk.Label(self, text = "Email: ")
        self.emaillbl.grid(row = 2, column = 0, sticky = "w")

        self.passwordlbl = tk.Label(self, text = "Password: ")
        self.passwordlbl.grid(row = 3, column = 0, sticky = "w")

        self.Confirmpasswordlbl = tk.Label(self, text = "Confirm Password: ")
        self.Confirmpasswordlbl.grid(row = 4, column = 0, sticky = "w")

        #create the entry boxes
        self.nameEnt = tk.Entry(self, text = "")
        self.nameEnt.grid(row = 1, column = 1, pady = 5, sticky = "w")

        self.emailEnt = tk.Entry(self, text = "")
        self.emailEnt.grid(row = 2, column = 1, pady = 5, sticky = "w")

        self.passwordEnt = tk.Entry(self, text = "")
        self.passwordEnt.grid(row = 3, column = 1, pady = 5, sticky = "w")
        self.passwordEnt.config(show = "*")

        self.passwordconfirmEnt = tk.Entry(self, text = "")
        self.passwordconfirmEnt.grid(row = 4, column = 1, pady = 5, sticky = "w")
        self.passwordconfirmEnt.config(show = "*")

        #create the buttons
        self.Loginbtn = tk.Button(self, text ="Already have an account? Login in",command = self.login)
        self.Loginbtn.grid(row = 6, column = 0, pady = 10)

        Bookingbtn = tk.Button(self, text ="Sign up",command = self.booking)
        Bookingbtn.grid(row = 7, column = 0, pady = 10)

        self.showbtn = tk.Button(self, text = "Show password", command = self.show)
        self.showbtn.grid(row = 3, column = 2, pady = 10)

        #bind enter key to booking function
        self.nameEnt.bind("<Return>", self.booking)
        self.emailEnt.bind("<Return>", self.booking)
        self.passwordEnt.bind("<Return>", self.booking)
        self.passwordconfirmEnt.bind("<Return>", self.booking)

    def show(self):
        self.passwordEnt.config(show = '')
        self.passwordconfirmEnt.config(show = '')
        self.showbtn.config(text = "Hide password")
        self.showbtn.config(command=self.hide)
    
    def hide(self):
        self.passwordEnt.config(show = '*')
        self.passwordconfirmEnt.config(show = "*")
        self.showbtn.config(text = "Show password")
        self.showbtn.config(command = self.show)
    
    def login(self, event=None):
        self.master.change(Loginpage)

    def booking(self, event=None):
        y = []
        if not self.nameEnt.get().isalpha() or self.nameEnt.get() == '':
            y.append('Please Input a First name with alphabetic characters only')
        if '@' not in self.emailEnt.get() or '.com' not in self.emailEnt.get() or self.emailEnt.get() == '':
            y.append('Please input a valid email')
        if self.passwordEnt.get() == '':
            y.append('Please input password')
        if self.passwordconfirmEnt.get() != self.passwordEnt.get() or self.passwordconfirmEnt.get() == '':
            y.append('Password is not matching')

        with open('BookingWebsiteDetails.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            my_dict = {k:v for k,v in reader}
        p1 = self.emailEnt.get()

        error_message = "\n".join(y)

        if p1 not in my_dict:
            if error_message:
                messagebox.showerror("Error", error_message)
            else:
                with open("BookingWebsiteDetails.csv", mode="a", newline="") as csv_file:
                    csv_writer = csv.writer(csv_file)
                    # Write the data to the CSV file
                    csv_writer.writerow([self.emailEnt.get(), self.passwordEnt.get()])
                self.master.change(Bookingpage) # correct password, switch to the second frame
        else:
            messagebox.showerror("error", "Already an account")
class Loginpage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        master.title("Main application")
        master.geometry("600x400")

        self.Titlelbl = tk.Label(self, text='Login Page', font = ("Arial", 15))
        self.Titlelbl.grid(row = 0, column = 0, pady = 10, sticky="N")

        self.Namelbl = tk.Label(self, text='Email:')
        self.Namelbl.grid(row = 1, column = 0, pady = 10, sticky="w")

        self.passwordlbl = tk.Label(self, text='Password:')
        self.passwordlbl.grid(row = 2, column = 0, pady = 10, sticky="w")

        #create the entry fields
        self.EmailEnt = tk.Entry(self, text = "", )
        self.EmailEnt.grid(row = 1, column = 1, pady = 10, sticky="w")

        self.passwordEnt = tk.Entry(self, text = "", )
        self.passwordEnt.grid(row = 2, column = 1, pady = 10, sticky="w")
        self.passwordEnt.config(show = "*")

        #create the buttons
        self.backbtn = tk.Button(self, text ="Don't have an account? Sign up",command = self.back)
        self.backbtn.grid(row = 3, column = 0)
        
        self.Signupbtn = tk.Button(self, text ="Log in",command = self.booking)
        self.Signupbtn.grid(row = 4, column = 0, pady = 10)
        
        self.EmailEnt.bind("<Return>", self.booking)
        self.passwordEnt.bind("<Return>", self.booking)

        self.showbtn = tk.Button(self, text = "Show password", command = self.show)
        self.showbtn.grid(row = 2, column = 2, pady = 10)

    def show(self):
        self.passwordEnt.config(show = '')
        self.showbtn.config(text = "Hide password")
        self.showbtn.config(command=self.hide)
    
    def hide(self):
        self.passwordEnt.config(show = '*')
        self.showbtn.config(text = "Show password")
        self.showbtn.config(command = self.show)

    def booking(self, event=None):
        y = []
        if '@' not in self.EmailEnt.get() or '.com' not in self.EmailEnt.get() or self.EmailEnt.get() == '':
            y.append('Please input a valid email')
        if self.passwordEnt.get() == '':
            y.append('Please input password')

        global p1

        error_message = "\n".join(y)

        if error_message:
            messagebox.showerror("Error", error_message)
        else:
            with open('BookingWebsiteDetails.csv', 'r') as f:
                reader = csv.reader(f, delimiter=',')
                my_dict = {k:v for k,v in reader}
            p1 = self.EmailEnt.get()
            password1 = self.passwordEnt.get()
            if p1 not in my_dict:
                messagebox.showerror("Name error", "Not a Email with an account")
            if (my_dict[p1]) == (password1):
                self.master.change(Bookingpage)
            else:
                messagebox.showerror("Login error", "Incorrect password")
    
    def back(self):
        self.master.change(Signup)

class Bookingpage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        
        master.title("booking")
        master.geometry("1000x750")

        self.x = tk.StringVar()
        self.y = tk.StringVar()
        self.z = tk.StringVar()
        self.v = tk.StringVar()
        self.v.set("Select a budget")
        options_list = ["$200-$300","$301-$400", "$401-$500", "$501-$600", "$601-$700"]

        # Create the label
        self.Titlelbl = tk.Label(self, text='Booking Page', font=("Arial", 15))
        self.Titlelbl.grid(row=0, column=1, pady=10)

        self.Planelbl = tk.Label(self, text='Airline:')
        self.Planelbl.grid(row=1, column=0, padx=10, pady=10)

        self.Fromlbl = tk.Label(self, text='From:')
        self.Fromlbl.grid(row=1, column=1, padx=10, pady=10)

        self.Tolbl = tk.Label(self, text='To:')
        self.Tolbl.grid(row=1, column=2, padx=10, pady=10)

        self.budgetlbl = tk.Label(self, text='Budget:')
        self.budgetlbl.grid(row=1, column=3, padx=10, pady=10)

        # Create the entry boxes
        self.PlaneEnt = tk.Entry(self, textvariable=self.x)
        self.PlaneEnt.grid(row=2, column=0, padx=10, pady=10)

        self.FromEnt = tk.Entry(self, textvariable=self.y)
        self.FromEnt.grid(row=2, column=1, padx=10, pady=10)

        self.ToEnt = tk.Entry(self, textvariable=self.z)
        self.ToEnt.grid(row=2, column=2, padx=10, pady=10)

        self.budgetDrp = tk.OptionMenu(self, self.v, *options_list)
        self.budgetDrp.grid(row=2, column=3, padx=10, pady=10)

        # Create the buttons
        self.backbtn = tk.Button(self, text="Want to Login?", command=self.back)
        self.backbtn.grid(row=5, column=1, padx=10, pady=10)

        self.searchbtn = tk.Button(self, text="Search", command=self.search)
        self.searchbtn.grid(row=3, column=1, padx=10, pady=10)

        self.PlaneEnt.bind("<Return>", self.search)
        self.FromEnt.bind("<Return>", self.search)
        self.ToEnt.bind("<Return>", self.search)
        self.master.bind("<Return>", self.search) 

        # Create the output for search results
        self.tv = ttk.Treeview(self, columns=('col_1', 'col_2', 'col_3', 'col_4'), show='headings')
        self.tv.column('col_1', minwidth=0, width=400)
        self.tv.column('col_2', minwidth=0, width=100)
        self.tv.column('col_3', minwidth=0, width=100)
        self.tv.column('col_4', minwidth=0, width=100)

        self.tv.heading('col_1', text='AIRLINE')
        self.tv.heading('col_2', text='FROM')
        self.tv.heading('col_3', text='TO')
        self.tv.heading('col_4', text='PRICE')

        self.tv.grid(row=4, column=0, columnspan=4, padx=10, pady=10)
        self.tv.bind("<<TreeviewSelect>>", self.on_treeview_select)
        self.load_initial_data()

    def load_initial_data(self):
        file = r'C:\Users\thush\OneDrive\Desktop\Python\SearchCheck.csv'

        with open(file, 'r') as f:
            csvreader = csv.reader(f)
            csvreader_list = list(csvreader)

        for (i, n, f, g) in csvreader_list:
            self.tv.insert('', 'end', values=(i, n, f, g))

    def search(self):
        
        y = []
        if self.PlaneEnt.get().isnumeric():
            y.append('Please input a valid Airline')
        if self.FromEnt.get().isnumeric():
            y.append('Please input a proper origin')
        if self.ToEnt.get().isnumeric():
            y.append('Please input a proper destination')

        error_message = "\n".join(y)

        if error_message:
            messagebox.showerror("Error", error_message)
        else:
            file = r'C:\Users\thush\OneDrive\Desktop\Python\SearchCheck.csv'

            with open(file, 'r') as f:
                csvreader = csv.reader(f)
                csvreader_list = list(csvreader)

            self.tv.delete(*self.tv.get_children())
            word = self.x.get().title()
            word1 = self.y.get()
            word2 = self.z.get()
            word3 = self.v.get()

            budget_min, budget_max = self.get_budget_range(word3)

            for (i, n, f, g) in csvreader_list:
                try:
                    price = int(g.replace('$', ''))
                except ValueError:
                    continue  # Skip rows with invalid price values
                
                match = True

                if word and word not in i:
                    match = False
                if word1 and word1 not in n:
                    match = False
                if word2 and word2 not in f:
                    match = False
                if budget_min > price or price > budget_max:
                    match = False

                if match:
                    self.tv.insert('', 'end', values=(i, n, f, g))

            self.PlaneEnt.delete(0, 'end')
            self.ToEnt.delete(0, 'end')
            self.FromEnt.delete(0, 'end')
            self.v.set("Select a budget")

    def get_budget_range(self, budget_str):
        if budget_str == "Select a budget":
            return (0, float('inf'))
        budget_range = budget_str.split('-')  # Splits the budget range into two parts from the hyphen
        budget_min = int(budget_range[0].replace('$', ''))
        budget_max = int(budget_range[1].replace('$', ''))
        return (budget_min, budget_max)

    def back(self):
        self.master.change(Loginpage)

    def on_treeview_select(self, event):
        selected_item = self.tv.selection()[0]
        item_values = self.tv.item(selected_item, 'values')
        
        # Create a new window
        detail_window = tk.Toplevel(self)
        detail_window.title("Flight Details")
        detail_window.geometry("400x200")

        
        # Create the functions
        def book():
            messagebox.showinfo("Booked", f"The {item_values[0]} plane from {item_values[1]} to {item_values[2]} has been booked\n{item_values[3]} has been charged to your card")
        
        # Create the buttons
        bookbtn = tk.Button(detail_window, text="Book", command=book)
        bookbtn.pack(pady=5)
        # Display the details
        details = ["Airline: " + item_values[0],
                "From: " + item_values[1],
                "To: " + item_values[2],
                "Price: " + item_values[3]]

        for idx, detail in enumerate(details):
            label = tk.Label(detail_window, text=detail, font=("Arial", 12))
            label.pack(pady=5)
        

if __name__=="__main__":
    app=MainApp()
    app.mainloop()