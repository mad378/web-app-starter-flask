
from flask import Blueprint, request, render_template, jsonify, flash, redirect #, url_for

new_routes = Blueprint("new_routes", __name__)

@new_routes.route('/myform')
def myform():
    print("VISITING THE FORM")
    return render_template("myformpage.html")

@new_routes.route('/sendemail', methods=["POST"])
def sendemail():
    print("SENDING AN EMAIL...")
    print("FORM DATA:", dict(request.form))
    #return jsonify(request.form)

    #product_name = request.form["product_name"]
    flash(f"Sent email to Sebastian esquire", "success") # use the "success" category to correspond with twitter bootstrap alert colors
    return redirect("/myform")
