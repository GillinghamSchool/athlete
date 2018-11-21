from flask import request, redirect, url_for, session, abort

from athlete import app
from athlete.authentication import verify_password, get_permission_level
from athlete.decorators import login_required
from athlete.web_pages import WebPage
from athlete.alerts import set_alert

web_pages = {"main": WebPage("main.html", "Home"),
             "login": WebPage("login.html", "Login"),
             "logged_in": WebPage("logged_in.html", "Logged In")}

# @app.before_first_request
# def startup():
#     session["credentials"] = {}
#     session["credentials"]["username"] = None
#     session["permission_level"] = 0
#     set_alert()


@app.route("/")
def main():
    rendered_page = web_pages["main"].render()
    set_alert()
    return rendered_page


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        # If the user is already logged in, let them know
        if "username" in session:
            rendered_page = web_pages["logged_in"].render()
            set_alert()
            return rendered_page
        # If the user is not logged in, show them the login page
        else:
            rendered_page = web_pages["login"].render()
            set_alert()
            return rendered_page
    # If the user has POSTed the a form
    elif request.method == "POST":
        # If they've posted the login form
        if "username" in request.form:
            # If either login field is empty, notify the user
            if request.form["username"] == "" or request.form["password"] == "":
                set_alert(True, "warning", "Login attempt failed",
                          "Please fill in all fields")
                return redirect(url_for("login"))
            else:
                # If the user is verified, set the username and
                # permission_level in the session, and alert them
                if verify_password(request.form["username"],
                                   request.form["password"]):
                    username = request.form["username"]
                    session["username"] = username
                    session["permission_level"] = get_permission_level(username)

                    set_alert(True, "success", "Logged in",
                              "You are now logged in as " + username)
                    return redirect(url_for("main"))
                else:
                    set_alert(True, "danger", "Login attempt failed",
                              "Incorrect username or password")
                    return redirect(url_for("login"))
        # If they've posted the sign out form
        elif "sign_out" in request.form:
            return redirect(url_for("sign_out"))


@app.route("/sign_out")
def sign_out():
    if request.method == "GET":
        set_alert(True, "success", "Signed out", "You are now signed out")
        session.pop("username")
        session.pop("permission_level")
        return redirect("/")


@app.route("/testing")
@login_required
def testing():
    if session["permission_level"] == 4:
        rendered_page = web_pages["main"].render()
        set_alert(True, "info", "Heya Seiya", "look at this blue alert")
        return rendered_page
    elif session["permission_level"] > 0:
        return "Hi, user!"
    else:
        abort(403)
