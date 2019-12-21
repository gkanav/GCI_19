import requests

def calc(x):
    input_string=x
    URL = " https://codeforces.com/api/user.info?handles="+input_string
    rtmp = requests.get(url = URL)
    r=rtmp.json()
    
    if r['status'] == "FAILED":
        return str(r['comment']), "0", "0", "0", "0"
    else :
        if 'rating' in r['result'][0]: 
            return str(r['result'][0]['handle']), str(r['result'][0]['rating']), str(r['result'][0]['rank']), str(r['result'][0]['maxRating']), str(r['result'][0]['maxRank'])
        else:
            return str(r['result'][0]['handle']), "0", "unrated", "0", "unrated"
        

