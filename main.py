from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/", methods=["POST"])
def signup():
	username = request.form.get("username");
	password = request.form.get("password");
	verify = request.form.get("verify");
	email = request.form.get("email");

	username_error = ''
	if not username or len(username) <= 3 or len(username) >= 20:
		username_error = "That's not a valid username"

	password_error = ''
	if not password or len(username) <= 3 or len(username) >= 20:
		password_error = "That's not a valid password"

	verify_error = ''
	if verify != password:
		verify_error = "Passwords don't match"

	email_error = ''
	if len(email) > 0:
		if (len(email) <= 3 or len(email) >= 20) or email.count('@') != 1 or email.count('.') != 1:
			email_error = "That's not a valid email"

	if username_error or password_error or verify_error or email_error:
		return render_template("index.html", username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)
	else:
		return render_template("welcome.html", username=username)


app.run()