from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    tickets = [
    {
        "title": "Impresora dañada",
        "content": "La impresora de recepción no está funcionando."
    },
    {
        "title": "Problema con el correo",
        "content": "No puedo enviar correos desde mi cuenta."
    },
    {
        "title": "Solicitud de acceso",
        "content": "Necesito acceso al sistema de inventario."
    }
    ]   
    return render_template("home.html", tickets = tickets)

@app.route("/crear-ticket", methods = ["GET","POST"])
def create_ticket():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        print(f"Título: {title}")
        print(f"Descripción: {content}")
        return redirect(url_for("home"))
    return render_template("create_ticket.html")