import http.client

conn = http.client.HTTPSConnection("api.cloudflare.com")

payload = "{\n  \"actions\": [\n    {\n      \"type\": \"forward\",\n      \"value\": [\n        \"noahwsl@163.com\"\n      ]\n    }\n  ],\n  \"enabled\": true,\n  \"matchers\": [\n    {\n      \"field\": \"to\",\n      \"type\": \"literal\",\n      \"value\": \"abc@chainedfinance.net\"\n    }\n  ],\n  \"name\": \"Send to noahwsl@163.com rule.\",\n  \"priority\": 0\n}"

headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer cANCdo0GJvDOZmkxLqYJywHDhGGxl6NCC5WlKjo6",
    }

conn.request("PUT", "/client/v4/zones/09de3d8611fd29df29b07bf649475d9a/email/routing/rules/de222db26a8c40978ef087c17a8d37a9", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))