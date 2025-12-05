from jinja2 import Environment, PackageLoader, select_autoescape
from http.server import HTTPServer, BaseHTTPRequestHandler
from Models import author
import Models
main_author  = author.Author("Vika", "P3121")
from controllers import CurrencyRatesCRUD

env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape()
)

template = env.get_template("index.html")

result=template.render(myapp="Приложение",
                      author_name = main_author.name,
                      group = main_author.group,
                      navigation=[{'caption': 'Основная страница',
                                   'href' : "/vikAaaaa_3121"},
                                  {"user": "пользователь",
                                   'href' : "/vika_3121_user"},
                                  {"autorization": "Авторизация",
                                   'href' : "/vika_3121_auto"},
                                  {"user_currencies": "подписчики на группу валют",
                                   'href' : "/vika_3121_usercur"},
                                  {"logout": "Выход",
                                   'href' : "/vika_3121_log"},
                                  {"courses": "Курсы валют",
                                   'href' : "/vika_3121_course"}]
                      )
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global result
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        # result = ""
        print(self.path)
        self.wfile.write(bytes(result, "utf-8"))



class CurrencyRatesMock():
    def __init__(self):
        self.__values =  [("USD", "02-04-2025 11:10", "90"),
              ("EUR", "02-04-2025 11:11", "91"),
              ("GBP", '02-04-2025 11:37', '100')]

    @property
    def values(self):
        return self.__values

c_r = CurrencyRatesMock()
c_r_controller = CurrencyRatesCRUD(c_r)
c_r_controller._create()
c_r_controller._read()


if __name__ == "__main__":
    print('server is running')

    httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    httpd.serve_forever()


