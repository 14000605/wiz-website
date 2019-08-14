BASE_ENDPOINT_URL = "https://cheezewizards.alchemyapi.io/"

def construct_query_from_dict(params):
        query = ""
        for param in params:
                if query != "":
                        query += "&"
                if params[param] != None:
                        query += str(param) + "=" + str(params[param])
        return query