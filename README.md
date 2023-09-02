# CSV2URDF

Generate *.URDF file using *.csv file from SW. This can be very handy when you want to modify only certain numbers in the URDF by touching the *csv file.

Put your *.CSV file in the ./files folder.

Open main.py and edit the value of ```robot_name```, which should match the name of your csv file.

For example, my csv file is "fun_guy.csv" then I should edit the main.py file so that I have: ```robot_name = "fun_guy"```

Run main.py and you will get your *.urdf in the ./files folder

## If you are working with BRUCE-OP:

(Note: If you are generating URDF directly from SW: make sure you create your URDF project with the name "bruce" to avoid and problem with linking model files.)

After modifying properties in the *.csv file to update your BRUCE-OP model, make sure your *.csv file is named as "bruce.csv" before you generate the URDF file, and rename your URDF file to "model.urdf" before transfering it into your BRUCE simulation project.
