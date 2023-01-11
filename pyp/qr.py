import pyqrcode


s = "hello"
url = pyqrcode.create(s)
url.svg("testfile.svg", scale = 8)
url.png('testfile.png', scale=6)