def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_url = "http://172.28.39.146:8000/complete/weibo/"
    auth_url = weibo_auth_url + "?client_id={client_id}&redirect_uri={rel_url}".format(client_id=3832728633, rel_url=redirect_url)
    print(auth_url)

def get_access_token(code="5c7dfc074c6ea128eff64bd5129afab2"):
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    import requests
    re_dict = requests.post(access_token_url, data={
        "client_id": "3832728633",
        "client_secret": "587c9f00d20324da1168dcd9e3b02fb3",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://172.28.39.146:8000/complete/weibo/",
    })
    #'{"access_token":"2.00eJ6PzHlnj4LE9ce097438cwh1fYC","remind_in":"157679999","expires_in":157679999,"uid":"7317957938","isRealName":"true"}'
    pass

if __name__ == '__main__':
    get_auth_url()
    get_access_token(code="5c7dfc074c6ea128eff64bd5129afab2")