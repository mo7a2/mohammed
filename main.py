import tkinter as tk
from tkinter import messagebox

class UtilityBill:
    def __init__(self, customer_name, consumption_kwh, price_per_kwh, tax_rate=0.05):
        self.customer_name = customer_name
        self.consumption_kwh = consumption_kwh
        self.price_per_kwh = price_per_kwh
        self.tax_rate = tax_rate

    def calculate_total_cost(self):
        cost_before_tax = self.consumption_kwh * self.price_per_kwh
        tax_amount = cost_before_tax * self.tax_rate
        total_cost = cost_before_tax + tax_amount
        return total_cost

    def generate_invoice(self):
        total_cost = self.calculate_total_cost()

        file = open("invoices.txt", "a", encoding="utf-8")
        file.write("=====================================\n")
        file.write("          Public Services Invoice         \n")
        file.write("=====================================\n")
        file.write(f"Customer Name: {self.customer_name}\n")
        file.write(f"Service Consumption: {self.consumption_kwh} units per month\n")
        file.write(f"Unit Price: ${self.price_per_kwh}\n")
        file.write(f"Taxes ({self.tax_rate * 100}%): ${total_cost - self.consumption_kwh * self.price_per_kwh:.2f}\n")
        file.write("-------------------------------------\n")
        file.write(f"Total: ${total_cost:.2f}\n")
        file.write("=====================================\n")
        file.close()

class UtilityBillGUI:
    def __init__(self, master, login_screen):
        self.master = master
        self.login_screen = login_screen
        master.title("Public Services Invoice")

        self.label_name = tk.Label(master, text="Customer Name:")
        self.label_name.pack()

        self.entry_name = tk.Entry(master)
        self.entry_name.pack()

        self.label_consumption = tk.Label(master, text="Service Consumption (units):")
        self.label_consumption.pack()

        self.entry_consumption = tk.Entry(master)
        self.entry_consumption.pack()

        self.label_price = tk.Label(master, text="Unit Price (dollars):")
        self.label_price.pack()

        self.entry_price = tk.Entry(master)
        self.entry_price.pack()

        self.generate_button = tk.Button(master, text="Generate Invoice", command=self.generate_invoice)
        self.generate_button.pack()

    def generate_invoice(self):
        customer_name = self.entry_name.get()
        consumption_kwh = float(self.entry_consumption.get())
        price_per_kwh = float(self.entry_price.get())

        bill = UtilityBill(customer_name, consumption_kwh, price_per_kwh)
        bill.generate_invoice()

        result_text = "Invoice saved to 'invoices.txt' file."
        result_label = tk.Label(self.master, text=result_text)
        result_label.pack()

        invoice_details_screen = InvoiceDetailsScreen(self.master, self, bill)
        invoice_details_screen.show_details()

    def show_utility_bill_gui(self):
        self.master.deiconify()

class LoginScreen:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        self.label_username = tk.Label(master, text="Username:")
        self.label_username.pack()

        self.entry_username = tk.Entry(master)
        self.entry_username.pack()

        self.label_password = tk.Label(master, text="Password:")
        self.label_password.pack()

        self.entry_password = tk.Entry(master, show="*")  # Show asterisks for password
        self.entry_password.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = "mohammed"
        password = "2005"

        entered_username = self.entry_username.get()
        entered_password = self.entry_password.get()

        if entered_username == username and entered_password == password:
            self.master.iconify()
            self.show_utility_bill_gui()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_utility_bill_gui(self):
        root = tk.Toplevel(self.master)
        app = UtilityBillGUI(root, self)
        root.mainloop()

class InvoiceDetailsScreen:
    def __init__(self, master, utility_bill_gui, bill):
        self.master = master
        self.utility_bill_gui = utility_bill_gui
        self.bill = bill
        master.title("Invoice Details")

        self.label_details = tk.Label(master, text="Invoice Details:")
        self.label_details.pack()

        self.details_text = tk.Text(master, height=10, width=50)
        self.details_text.pack()

        self.end_program_button = tk.Button(master, text="End Program", command=self.end_program)
        self.end_program_button.pack()

    def show_details(self):
        details = f"Customer Name: {self.bill.customer_name}\n" \
                  f"Service Consumption: {self.bill.consumption_kwh} units per month\n" \
                  f"Unit Price: ${self.bill.price_per_kwh}\n" \
                  f"Total Cost: ${self.bill.calculate_total_cost():.2f}"

        self.details_text.insert(tk.END, details)
    def end_program(self):
        self.master.destroy()

root = tk.Tk()
login_screen = LoginScreen(root)
root.mainloop()
