import cgi

# 创建 FieldStorage 实例来处理表单数据
form = cgi.FieldStorage()

# 获取表单数据
name = form.getvalue("name")

# 设置 HTTP 响应头
print("Content-type: text/html\n")

# 生成 HTML 页面
print("<html>")
print("<head><title>CGI Example</title></head>")
print("<body>")
print("<h1>Hello, {}!</h1>".format(name))
print("</body>")
print("</html>")