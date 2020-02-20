
from flask import Blueprint, request, render_template, jsonify, flash, redirect #, url_for
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

new_routes = Blueprint("new_routes", __name__)

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

@new_routes.route('/chat.html')
def myform():
    print("VISITING THE FORM")
    return render_template("myformpage.html")

@new_routes.route('/sendemail', methods=["POST"])
def sendemail():
    print("SENDING AN EMAIL...")
    print("FORM DATA:", dict(request.form))
    #return jsonify(request.form)
    email_address = request.form["email_address"]
    body = request.form["inquiry"]
    #product_name = request.form["product_name"]


    
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))

    subject = "Testing 1,2,3..."

    html_content = body
    print("HTML:", html_content)

    message = Mail(from_email=MY_ADDRESS, to_emails=email_address, subject=subject, html_content=html_content)

    try:
        response = client.send(message)

        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        print(response.body)
        print(response.headers)

    except Exception as e:
        print("OOPS", e.message)



















    flash(f"Sent email to {email_address}", "success") # use the "success" category to correspond with twitter bootstrap alert colors
    return redirect("/chat.html")