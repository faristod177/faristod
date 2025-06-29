import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry

def calculate_vacation():
    try:
        start_date = entry_start.get()
        end_date = entry_end.get()
        salary = float(entry_salary.get())
        annual_vacation_days = int(entry_annual_vac.get())
        used_vacation_days = int(entry_used_vac.get())

        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        days_worked = (end - start).days + 1

        vacation_entitlement = (days_worked / 365) * annual_vacation_days
        vacation_due = vacation_entitlement - used_vacation_days
        daily_salary = salary / 30
        vacation_amount = vacation_due * daily_salary

        result_text = (
            f"عدد الأيام بين تاريخ الالتحاق والانتهاء: {days_worked} يوم\n"
            f"الإجازة المستحقة: {vacation_due:.2f} يوم\n"
            f"مبلغ راتب أيام الإجازة المستحقة: {vacation_amount:.2f} ريال"
        )
        result_label.config(text=result_text)
    except Exception as e:
        messagebox.showerror("خطأ", "يرجى التأكد من صحة البيانات المدخلة.")

root = tk.Tk()
root.title("حساب الإجازة المستحقة")
root.geometry("480x420")
root.configure(bg="#f0f4f7")

label_font = ("Arial", 13, "bold")
entry_font = ("Arial", 13)
button_font = ("Arial", 13, "bold")

main_frame = tk.Frame(root, bg="#f0f4f7")
main_frame.pack(expand=True)

def center_widgets(widget, row):
    widget.grid(row=row, column=0, columnspan=2, pady=7, padx=10, sticky="ew")

tk.Label(main_frame, text="Start Date:", bg="#f0f4f7", font=label_font, anchor="center").grid(row=0, column=0, sticky="e", pady=7, padx=10)
entry_start = DateEntry(main_frame, font=entry_font, date_pattern="yyyy-mm-dd", justify="center", background="#4caf50", foreground="white", width=18)
entry_start.grid(row=0, column=1, pady=7, padx=10)

tk.Label(main_frame, text="End Date:", bg="#f0f4f7", font=label_font, anchor="center").grid(row=1, column=0, sticky="e", pady=7, padx=10)
entry_end = DateEntry(main_frame, font=entry_font, date_pattern="yyyy-mm-dd", justify="center", background="#4caf50", foreground="white", width=18)
entry_end.grid(row=1, column=1, pady=7, padx=10)

tk.Label(main_frame, text="Monthly Salary:", bg="#f0f4f7", font=label_font, anchor="center").grid(row=2, column=0, sticky="e", pady=7, padx=10)
entry_salary = tk.Entry(main_frame, font=entry_font, justify="center", width=20)
entry_salary.grid(row=2, column=1, pady=7, padx=10)

tk.Label(main_frame, text="Annual Vacation Days:", bg="#f0f4f7", font=label_font, anchor="center").grid(row=3, column=0, sticky="e", pady=7, padx=10)
entry_annual_vac = tk.Entry(main_frame, font=entry_font, justify="center", width=20)
entry_annual_vac.grid(row=3, column=1, pady=7, padx=10)

tk.Label(main_frame, text="Used Vacation Days:", bg="#f0f4f7", font=label_font, anchor="center").grid(row=4, column=0, sticky="e", pady=7, padx=10)
entry_used_vac = tk.Entry(main_frame, font=entry_font, justify="center", width=20)
entry_used_vac.grid(row=4, column=1, pady=7, padx=10)

tk.Button(main_frame, text="احسب", command=calculate_vacation, font=button_font, bg="#4caf50", fg="white").grid(row=5, column=0, columnspan=2, pady=15, ipadx=30)

result_label = tk.Label(main_frame, text="", fg="#0d47a1", bg="#f0f4f7", font=("Arial", 13), justify="center", anchor="center")
result_label.grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_pdf():
    try:
        start_date = entry_start.get()
        end_date = entry_end.get()
        salary = float(entry_salary.get())
        annual_vacation_days = int(entry_annual_vac.get())
        used_vacation_days = int(entry_used_vac.get())

        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        days_worked = (end - start).days + 1

        vacation_entitlement = (days_worked / 365) * annual_vacation_days
        vacation_due = vacation_entitlement - used_vacation_days
        daily_salary = salary / 30
        vacation_amount = vacation_due * daily_salary

        file_name = "Vacation_Result.pdf"
        c = canvas.Canvas(file_name, pagesize=A4)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 800, "Vacation Calculation Result")
        c.setFont("Helvetica", 12)
        c.drawString(100, 760, f"Start Date: {start_date}")
        c.drawString(100, 740, f"End Date: {end_date}")
        c.drawString(100, 720, f"Monthly Salary: {salary}")
        c.drawString(100, 700, f"Annual Vacation Days: {annual_vacation_days}")
        c.drawString(100, 680, f"Used Vacation Days: {used_vacation_days}")
        c.drawString(100, 640, f"Days Worked: {days_worked} days")
        c.drawString(100, 620, f"Accrued Vacation: {vacation_due:.2f} days")
        c.drawString(100, 600, f"Vacation Pay Amount: {vacation_amount:.2f} SAR")
        c.save()
        messagebox.showinfo("Done", f"Results saved in file {file_name}")
    except Exception as e:
        messagebox.showerror("خطأ", "يرجى التأكد من صحة البيانات المدخلة.")

tk.Button(main_frame, text="Export PDF", command=export_pdf, font=button_font, bg="#1976d2", fg="white").grid(row=7, column=0, columnspan=2, pady=5, ipadx=30)

root.mainloop()
