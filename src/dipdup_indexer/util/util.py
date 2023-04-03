def getTagFromToken(fa2_address, fa2_id):
    if fa2_id is None:
        tag = "".join([fa2_address, ":null"])
    else:
        tag = "".join([fa2_address, ":" + fa2_id])

    return tag
