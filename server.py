from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route('/')
def index():
	mysql = connectToMySQL("lead_gen_business")
	clients = mysql.query_db("SELECT clients.first_name, clients.last_name, COUNT(leads.id) AS leads FROM clients LEFT JOIN sites ON clients.id = sites.clients_id LEFT JOIN leads on sites.id = leads.id GROUP BY clients.last_name")
	x = []
	for client in clients:
		x.append({"y": client['leads'], "label": client['last_name']})
	print(x)
	return render_template('index.html', clients = clients, x=x)

if __name__ == "__main__":
	app.run(debug=True)