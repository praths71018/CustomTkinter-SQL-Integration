# CustomTkinter-SQL-Integration
Connecting MySQL Database with Custom Tkinter GUI in Python.

- This appplication first connects the Python program to Health Database
- When you execute the program you get a GUI asking to type the temperature.
- After entering the Temperature it finds the matching row for the Temperature in Database.
- It then Fetches the Feedback from the Database and display the GUI

## Modules / Requirements
- MySQL
- python mysql.connector
- customtkinter
- health database (health.sql)

## Database
![database](https://github.com/praths71018/CustomTkinter-SQL-Integration/blob/main/Output%20Screenshot/database.png)

## Running the application
1. Run health.sql to create the health database
2. Run main.py
   
   ```bash
   python main.py
   ```
3. A GUI will pop up as shown in below Figure.

   ![img3](https://github.com/praths71018/CustomTkinter-SQL-Integration/blob/main/Output%20Screenshot/3.png)
   
5. Enter temperature and press Enter button. Feedback will be displayed
   
   ![img1](https://github.com/praths71018/CustomTkinter-SQL-Integration/blob/main/Output%20Screenshot/1.png)
   
   ![img2](https://github.com/praths71018/CustomTkinter-SQL-Integration/blob/main/Output%20Screenshot/2.png)
