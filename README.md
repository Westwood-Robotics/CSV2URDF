# CSV2URDF

Generate *.URDF file using *.csv file from SW. This can be very handy when you want to modify only certain numbers in the URDF by touching the *csv file.

Put your *.CSV file in the ./files folder.

Open main.py and edit the value of ```robot_name```, which should match the name of your csv file.

For example, my csv file is "fun_guy.csv" then I should edit the main.py file so that I have: ```robot_name = "fun_guy"```

Run main.py and you will get your *.urdf in the ./files folder
