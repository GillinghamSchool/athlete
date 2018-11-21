from athlete.dictionaries import assets_columns


def prettify_assets_columns(column_list):
    pp_column_list = []
    for v in column_list:
        pp_column_list.append(assets_columns[v])
    return pp_column_list
