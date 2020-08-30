# houseitt

Steps to get the project working open cmd go to project folder in our case (houseitt) for ex C:\Users\Hitesh\Desktop\data\project 11 django\houseitt then run python manage.py runserver

if you get amy errors (dB not found or dB model not found) then do the following at the same directory in cmd python manage.py makemigrations calc python manage.py sqlmigrate calc 0001 then rerun python manage.py runserver now youd get an internal server address (most likely 127.0.0.1:8000) now you can see the forms and in cmd you can observe the code state after completing the form you can see the data in db.sqlite3 (in the folder itself)
