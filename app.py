from flask import Flask, jsonify, request, render_template

# Intitialise the app
app = Flask(__name__)


# Define what the app does
@app.get("/greet")
def index():
    f_name = request.args.get("f_name")
    lname = request.args.get("lname")
    if not f_name and not lname:
        # If both first name and last name are missing, return an error
        return jsonify({"status": "error"})
    elif f_name and not lname:
        # If first name is present but last name is missing
        response = {"data": f"Hello, {f_name} !"}
    elif not f_name and lname:
        # If first name is missing but last name is present
        response = {"data": f"Hello, Mr. {lname} !"}
    else:
        # if none of the above is true, then both names must be present
        response = {"data": f"Is your name {f_name} {lname} ?"}
    return render_template('index.html', response=response)
    #return render_template('index.html', response=jsonify(response))
