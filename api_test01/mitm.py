from mitmproxy import http


# # 直接修改返回值
# def request(flow: http.HTTPFlow):
#     if flow.request.pretty_url == "https://www.baidu.com/":
#         flow.response = http.HTTPResponse.make(
#             200,
#             "Hellow world1！！！",
#             {"Content-type": "text/html"}
#         )

# # 读取文件
def request(flow: http.HTTPFlow):
    if flow.request.pretty_url == "https://www.baidu.com/":
        with open("./tmp.json") as f:
            flow.response = http.HTTPResponse.make(
                200,
                f.read(),
                # {"Content-type": "text/html"}
                {"Content-type": "application/json"}
            )


def response(flow: http.HTTPFlow):
    if flow.request.pretty_url == "https://www.baidu.com/":
        flow.response.text = "xxxxxx"
