import customtkinter
import mysql.connector as sql

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root=customtkinter.CTk()
root.geometry("500x350")

def fetch():
        temp=entry1.get()
        print("{}".format(temp))

        conn = sql.connect(host="localhost", user="root", passwd="pr@tham262003", database="health")
        if conn.is_connected:
            print("Database Connection is Successful")
            cur=conn.cursor()
            cur.execute("SELECT Overall_Health FROM HealthCare WHERE Temp = %s;",(temp,))
            # cur.execute("SELECT Overall_Health FROM HealthCare WHERE Temp = 99.2")
            result=cur.fetchone()
            label_feedback.configure(text="{}".format(result))
            conn.close()

        else:
            print("Database not connected")

font=customtkinter.CTkFont(family='Roboto',size=24)

label_temperature=customtkinter.CTkLabel(master=root,text="Enter Temperature".capitalize(),font=font)
label_temperature.pack(pady=12,padx=10)

entry1=customtkinter.CTkEntry(master=root,placeholder_text="Temperature")
entry1.pack(pady=12,padx=10)

label_feedback=customtkinter.CTkLabel(master=root,text="FeedBack is displayed here",font=font)

label_feedback.pack(pady=12,padx=10)

button=customtkinter.CTkButton(master=root,text="Enter",command=fetch)
button.pack(pady=12,padx=10)

root.mainloop()








