# Import thư viện
import urllib.request
import re


def main():
    # Lấy source web
    html = urllib.request.urlopen(
        "http://www.pythonchallenge.com/pc/def/equality.html").read().decode()

    # Lọc lấy đoạn thông tin cần tìn nằm trong <!-- --!>
    data = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]

    # Tìm và in ra đoạn thông tin theo đúng yêu cầu được 3 kí tự hoa bao quanh
    print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))


if __name__ == '__main__':
    main()
