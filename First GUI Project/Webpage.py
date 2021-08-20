#!/usr/bin/python3
import cgi
import cgitb
import json

cgitb.enable()

print("Content-type: text/html\n")
print('''
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>First GUI Project</title>
  </head>
  <body style="text-align: center;">
    <div class="container">
        <h1>First GUI Project</h1>
''')

arguments = cgi.FieldStorage()
try:
    if arguments["state"].value == "On":
        with open("state.json", "w") as file:
            file.write(json.dumps({"state": 1}))
        print('<h5>State of the pin: On</h5>')
    elif arguments["state"].value == "Off":
        with open("state.json", "w") as file:
            file.write(json.dumps({"state": 0}))
        print('<h5>State of the pin: Off</h5>')
except:
    pass

print('''
        <form action="Webpage.py" method="get">
            <input type="submit" value="On" name="state" class="btn btn-primary" style="margin: 10px; width: 100px;"/><br/>
            <input type="submit" value="Off" name="state" class="btn btn-danger" style="margin: 10px; width: 100px;"/>
        </form>
    </div>
  </body>
</html>
''')
