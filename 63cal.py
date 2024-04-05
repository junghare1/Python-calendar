import tkinter as tk
from tkinter import ttk
import calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")
        self.root.geometry("400x500")
        self.root.config(bg="#f0f0f0")

        self.selected_date = tk.StringVar()

        # Calendar Header
        self.calendar_label = tk.Label(root, text="Calendar", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333")
        self.calendar_label.pack(pady=10)

        # Year Entry
        self.year_label = tk.Label(root, text="Enter Year:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
        self.year_label.pack()
        self.year_entry = tk.Entry(root, font=("Helvetica", 12), bg="#fff", fg="#333", highlightbackground="#ccc", highlightthickness=1)
        self.year_entry.pack(pady=5)

        # Month Combobox
        self.month_label = tk.Label(root, text="Select Month:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
        self.month_label.pack()
        self.month_combo = ttk.Combobox(root, values=[calendar.month_name[i] for i in range(1, 13)], font=("Helvetica", 12), state="readonly")
        self.month_combo.current(0)  # Set default to January
        self.month_combo.pack(pady=5)

        # Show Calendar Button
        self.show_button = tk.Button(root, text="Show Calendar", bg="#007bff", fg="white", font=("Helvetica", 12), command=self.show_calendar)
        self.show_button.pack(pady=10)

        # Calendar Display
        self.calendar_frame = tk.Frame(root, bg="#f0f0f0")
        self.calendar_frame.pack()

        # Exit Button
        self.exit_button = tk.Button(root, text="Exit", bg="#dc3545", fg="white", font=("Helvetica", 12), command=root.quit)
        self.exit_button.pack(pady=10)

    def show_calendar(self):
        year = int(self.year_entry.get())
        month = self.month_combo.current() + 1
        cal_content = calendar.month(year, month)

        # Clear previous calendar
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        # Display new calendar
        self.calendar_display = tk.Label(self.calendar_frame, text=cal_content, font=("Courier", 12), bg="#f0f0f0", fg="#333")
        self.calendar_display.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()



