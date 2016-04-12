import http.client

conn = http.client.HTTPConnection("127.0.0.1:8081")

payload = "{\"admin\":false,\"usernames\":[\"edx_xblock_jupyter\"]}"

headers = {
    'referer': "127.0.0.1:8081/hub/",
    'content-type': "application/json",
    }

conn.request("GET", "/hub/api/authorizations/token/2514fff9f3fc42d730c09ba60a33a373d9e3b8e1c7e12fc20893b53427b12084", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
