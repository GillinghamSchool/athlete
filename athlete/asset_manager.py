from flask import render_template, session

from athlete import app
from athlete.asset_handling import get_assets
title = "Asset Manager"


@app.route("/app/asset_manager")
def asset_manager():

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

        asset_count = 25
        column_list = ["AssetID", "AssetNo", "AssetName", "AssetSerialNumber", "DateOriginallyAdded"]

        asset_list = get_assets(asset_count, column_list)
        print(asset_list)

        return render_template("asset_manager.html",
                               title=title,
                               logged_in_message=rendered_logged_in_message,
                               signed_in=signed_in_state,
                               alert=alert_state,
                               alert_type=alert_type,
                               alert_header=alert_header,
                               alert_message=alert_message,
                               columns=column_list,
                               assets=asset_list)
