from athlete.databaser import connect
connection = connect()
cursor = connection.cursor()


# Returns 'count' * assets in dictionary form
def get_assets(count=25, columns=["AssetID", "AssetNo", "AssetName"]):
    # Joins the desired columns into a SQL compatible string
    fields = ", ".join(columns)
    query = "SELECT TOP " + str(count) + " " + fields + " FROM Assets"
    cursor.execute(query)

    # Loops through the results from the query
    assets = []
    for asset in cursor.fetchall():  # cursor.fetchall() returns tuples
        row = list(asset)  # Turns the returned tuple into an asset list
        assets.append(map_asset(row, columns))

    return assets  # Returns the data to be processed by Jinja and displayed


# Maps an asset list to a query
def map_asset(asset, columns):
    asset_dict = {}
    for column, data in zip(columns, asset):  # Loops through the two tables
        asset_dict.update({column: data})  # Links the data together
    return asset_dict  # Returns the data to be appended to a list
