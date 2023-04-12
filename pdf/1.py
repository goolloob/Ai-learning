import requests

headers = {
    'content-type': 'text/plain;',
}
data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockcount", "params": [] }'
response = requests.post('http://192.168.3.131:8080', headers=headers, data=data, auth=('CF', 'ITsupport'))
print(response.text)
#一般情况下就可以请求成功得到返回值
# curl --user CF --data-binary \
# '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockcount", "params": [] }' \
# -H 'content-type: text/plain;' http://183.2.185.113:8332


# curl --user CF --data-binary \
# '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockcount", "params": [] }' \
# -H 'content-type: text/plain;' --resolve 127.0.0.1:80:127.0.0.1 http://127.0.0.1:12345