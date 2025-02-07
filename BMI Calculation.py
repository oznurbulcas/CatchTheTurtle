from tkinter import *

window=Tk()
window.title("BMI Calculator")
window.minsize(300,200)

def calculation():
    weight_info = weight_entry.get()
    height_info = height_entry.get()
    if weight_info=="" or height_info=="":
        result_label.config(text="Please enter both weight and height!")
    else:
        try:
            bmi=float(weight_info)/(float(height_info)/100)**2
            result_text=bmi_interval(bmi)
            result_label.config(text=result_text)

        except:
            result_label.config(text="Please enter a valid number")


def bmi_interval(bmi):
    result_text=f"Your BMI is {round(bmi,2)} and You are "
    if bmi < 18.5:
        result_text += "underweight"
    elif 18.5 <= bmi <= 24.9:
        result_text += "normal "
    elif 25 <= bmi <= 29.9:
        result_text += "overweight "
    elif 30 <= bmi <= 34.9:
        result_text += "obese"
    elif 35 <= bmi <= 39.9:
        result_text += "severely obese"
    elif bmi > 40:
        result_text += "morbidly obese"
    return result_text


#labels and entries
weight_label=Label(text="Enter Your Weight (kg)")
weight_label.pack()
weight_entry=Entry()
weight_entry.pack()

height_label=Label(text="Enter Your Height (cm)")
height_label.pack()
height_entry=Entry()
height_entry.pack()

calculate_button=Button(text="Calculate",command=calculation)
calculate_button.pack()

result_label=Label()
result_label.pack()

window.mainloop()