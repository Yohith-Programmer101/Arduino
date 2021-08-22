#!/usr/bin/python3
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/html\n")
print('''
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>Continuous Input From Potentionmeter</title>
  </head>
  <body style="text-align: center;">
    <div class="container" style="max-width: 500px; padding: 10px; margin-top: 10px; border-radius: 5px; border: 1px solid black;">
        <h2>Continuous Input From Potentionmeter</h2><br/>
        <h4>Value:</h4>
        <h3 id="value">0<h3>
    </div>
    <script>
        const func = () => fetch('data.json').then(data => data.text()).then(str => document.getElementById('value').innerText = str).catch(err => console.log(err))
        i = setInterval(func, 100)
    </script>
  </body>
</html>
''')
