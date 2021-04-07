from kivy.app import App
#kivy.require("1.9.1")
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()
    def search_location(self):

        search_template = "api.openweathermap.org/data/2.5/forecast/daily?APPID=ef4f6b76310abad083b96a45a6f547be&q=" + "{}"
        search_url = search_template.format(self.search_input.text)
        print search_url
        request = UrlRequest(search_url, self.found_location)
        print request
        print "Result: ", request.result

    def found_location(self, request, data):
        print request
        print data
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
            for d in data['list']]
        print   cities
        self.search_results.item_strings = cities
        print "DONE"

class WeatherApp(App):
    pass


if __name__ == '__main__':
    WeatherApp().run()