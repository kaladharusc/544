import requests
import jwt
import time
import uuid
def getJWT():
    token = jwt.encode({"iss": "45711582",
      "iat": int(time.time()),
      "exp": int(time.time()) + 180,
      "ist": "project",
      "jti": str(uuid.uuid4())},
      '9acbc422391cc15f593fa86b6adfcda8e3b7424b',
      algorithm='HS256')
    return token
def delete():
    token = getJWT()
    "https://api.opentok.com/v2/project/<api_key>/archive/<archive_id>"
    url = "https://api.opentok.com/v2/project/45620232/archive/"
    listReq = requests.get(url, headers={"X-OPENTOK-AUTH": token});
    archiveList = listReq.json()
    for item in archiveList['items']:
        print(item['id'])
        deleteUrl = "https://api.opentok.com/v2/project/45620232/archive/" + item['id']
        deleteReq = requests.delete(deleteUrl, headers={"X-OPENTOK-AUTH": token})

        print(deleteReq.status_code)

if __name__ == '__main__':
    #delete()
    print(getJWT())
