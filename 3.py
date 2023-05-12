import http.client

conn = http.client.HTTPSConnection("api.cloudflare.com")

headers = {
    'Content-Type': "application/json",
    # 'X-Auth-Key': "PHEeansQ8jxawHZCYeZLV2AuorJF5_Sap5tjnUDD"
    # 'X-Auth-Key':"1c26fbfe8cb56cd4eb01630756eeb134a31f8"
    'Authorization': "Bearer fWGRSkfYwg64A7bAjz9PsFADqcuR5eSQ9agsSRZ3",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    # "Accept-Language": "en-US,en;q=0.5"
    }

conn.request("GET", "/client/v4/zones/09de3d8611fd29df29b07bf649475d9a/email/routing/rules", headers=headers)

res = conn.getresponse()
data = res.read()

a = data.decode("utf-8")
print(a)


