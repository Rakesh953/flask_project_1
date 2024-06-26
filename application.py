from flask import Flask
FAI=Flask(__name__)

@FAI.route('/rakesh')
def rakesh():
    return '<center><h1>This is the First Flask Project</h1></center>'

FAI.run(debug=True)