import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1", port="8889", user="root", password="root")

cursor = mydb.cursor()

cursor.execute('CREATE DATABASE geoguesser')
cursor.execute('USE geoguesser')
cursor.execute('CREATE TABLE location (name varchar(255), y_coordinate FLOAT(7,4) , x_coordinate FLOAT(7,4)  )')
cursor.execute('CREATE TABLE scoreboard (username varchar(255), score INT)')

cursor.execute('CREATE USER \'backend\'@\'localhost\' IDENTIFIED BY \'backend\'')
cursor.execute('GRANT SELECT,INSERT ON geoguesser.location TO \'backend\'@\'localhost\'')
cursor.execute('GRANT SELECT,INSERT,UPDATE ON geoguesser.scoreboard TO \'backend\'@\'localhost\'')

cursor.execute('INSERT INTO location VALUES(\'Keleti\',47.5006,19.0821)'),
cursor.execute('INSERT INTO location VALUES(\'NemzetiM\',47.4910,19.0616)')
cursor.execute('INSERT INTO location VALUES(\'I\',47.4725,19.0592)')
cursor.execute('INSERT INTO location VALUES(\'K\',47.4818,19.0561)')
cursor.execute('INSERT INTO location VALUES(\'Citadella\',47.4872,19.0455)')
cursor.execute('INSERT INTO location VALUES(\'Bazilika\',47.5006,19.0528)')
cursor.execute('INSERT INTO location VALUES(\'Parlament\',47.5062,19.0469)')
cursor.execute('INSERT INTO location VALUES(\'Szabadsagter\',47.5043,19.050)')
cursor.execute('INSERT INTO location VALUES(\'Szecheny\',47.5191,,19.0815)')
cursor.execute('INSERT INTO location VALUES(\'Szerb\',47.5193,19.2304)')
cursor.execute('INSERT INTO location VALUES(\'ALLEE\',47.4739,19.0483)')
cursor.execute('INSERT INTO location VALUES(\'Nyugati\',47.5101,19.0566)')
cursor.execute('INSERT INTO location VALUES(\'Mori\',47.5122,19.0505)')
cursor.execute('INSERT INTO location VALUES(\'57\',47.50134,19.0641)')
cursor.execute('INSERT INTO location VALUES(\'Asia center\',47.5486,19.1479)')
cursor.execute('INSERT INTO location VALUES(\'xD\',47.4868,19.0573)')
cursor.execute('INSERT INTO location VALUES(\'Zsinaggoga\',47.4963,19.0603)')
cursor.execute('INSERT INTO location VALUES(\'ors\',47.5044,19.1369)')
cursor.execute('INSERT INTO location VALUES(\'Blaha\',47.4969,19.0704)')
cursor.execute('INSERT INTO location VALUES(\'Rudas\',47.4886,19.0486)')
cursor.execute('INSERT INTO location VALUES(\'var\',47.4970,19.0391)')




mydb.commit()


