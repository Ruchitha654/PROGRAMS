import tkinter

def cal_bmi():
    try:
         h=float(ht_val.get())
         w=float(wt_val.get())
         h1=h/100
         bmi=w/h1**2
         if(bmi>=18.5 and bmi<=22.5):
            result= f"BMI: {round(bmi, 2)} (Normal weight)"
         elif(bmi>= 22.5):
            result= f"BMI: {round(bmi, 2)} (Overweight)"
         else:
            result=f"BMI: {round(bmi, 2)} (Underweight)"
    except:
         result="enter valid numbers"
    result_label=tkinter.Label(root, text=result, font=("Arial", 15), bg="light blue")
    result_label.pack(pady=10)
root=tkinter.Tk()
root.geometry("600x600")
root.title("BMI Calculator")
root.configure(bg="light blue")
head =tkinter.Label(root,text="BMI Calculator",font="Arial",fg="Black",bg="white")
head.pack(pady=50,padx=50)

fr=tkinter.Frame(root,bg="light blue")
fr.pack(pady=50,padx=50)

ht=tkinter.Label(fr,text="HEIGHT(in cm)",font=("Arial",15))
ht.grid(row=1,column=0,padx=5,pady=5)

ht_val=tkinter.Entry(fr)
ht_val.grid(row=1,column=1,padx=5,pady=5)

wt=tkinter.Label(fr,text="WEIGHT(in kg)",font=("Arial",15))
wt.grid(row=2,column=0,padx=5,pady=5)

wt_val=tkinter.Entry(fr)
wt_val.grid(row=2,column=1,padx=5,pady=5)

bt=tkinter.Button(fr,text="CALCULATE",font=("Arial",20,"bold"),fg="red",command=cal_bmi)
bt.grid(row=3,column=0,padx=5,pady=5)
# result=tkinter.Label(text="BMI Calculator",bg="light blue")
# cal_bmi()
root.mainloop()