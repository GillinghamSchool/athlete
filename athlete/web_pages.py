from flask import render_template, session
from athlete.decorators import keys_required


# The WebPage class is used to return rendered web pages. The reason for
# putting it in a class is to normalise the process.
class WebPage(object):

    def __init__(self, template, title):
        self.template = template
        self.title = title

    @keys_required
    def render(self):
        username = None if "username" not in session\
            else session["username"]

        # Message displayed in the navbar to indicate login status
        rendered_logged_in_message = ("Logged in as: " + username) if username is not None\
            else "Not currently logged in"

        # True if the user is signed in, else false
        signed_in_state = True if username is not None else False

        # Gets the alert settings from the session
        alert_settings = session["alert"]
        # Boolean determining if the alert will show
        alert_state = alert_settings["state"]
        # Alert 'type' e.g. danger, alert
        alert_type = alert_settings["type"]
        # The title text of the alert
        alert_header = alert_settings["header"]
        # The body text of the alert
        alert_message = alert_settings["message"]

        return render_template(self.template,
                               title=self.title,
                               logged_in_message=rendered_logged_in_message,
                               signed_in=signed_in_state,
                               alert=alert_state,
                               alert_type=alert_type,
                               alert_header=alert_header,
                               alert_message=alert_message)
