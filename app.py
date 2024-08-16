from flask import flask 

app  =  Flask(name) 

@app.route('/') 

def hello_world() :

  return 'destroyer'

if name == "main":

  app.run() 
