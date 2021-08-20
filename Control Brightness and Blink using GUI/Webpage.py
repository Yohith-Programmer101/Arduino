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
    <title>Control Brightness and Blink using GUI</title>
  </head>
  <body style="text-align: center;">
    <div class="container" style="max-width: 500px; padding: 10px; margin-top: 10px; border-radius: 5px; border: 1px solid black;">
        <h2>Control Brightness and Blink using GUI</h2><br/>
''')

arguments = cgi.FieldStorage()
try:
    if int(arguments['delay'].value):
        if int(arguments['brightness'].value):
            with open("data.json", "w") as file:
                file.write(json.dumps({"delay": int(
                    arguments['delay'].value)/10, "brightness": int(arguments['brightness'].value)/100}))
        else:
            pass
    else:
        pass
except:
    pass

print('''
        <form action="Webpage.py" method="get">
            <div class="form-group">
                <label for="delay">Enter a value between 1 and 10 for the blink delay:</label>
                <input type="number" class="form-control" min="1" max="10" name="delay" required/>
            </div>
            <div class="form-group">
                <label for="brightness">Brightness:</label>
                <input type="range" name="brightness" class="form-control" min="0" max="100" required/>
            </div>
            <button type="submit" class="btn btn-primary">Start</button>
        </form>
    </div>
  </body>
</html>
''')
