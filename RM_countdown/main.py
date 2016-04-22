#! Python2
# Real Madrid countdown - This program will create a countdown for the upcoming match of Real Madrid and also show some relevent informations
#Author: Tanzim Rizwan


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty
from kivy.clock import Clock
import datetime
import requests
from bs4 import BeautifulSoup


class Counter_Timer(BoxLayout):
    l_name = StringProperty()
    days = StringProperty()
    hours = StringProperty()
    minutes = StringProperty()
    seconds = StringProperty()
    op_team = StringProperty()
    place = StringProperty()


    def update(self, dt):
        url = 'http://www.realmadrid.com/en/football/schedule'

        r = requests.get(url)
        r.raise_for_status()

        soup = BeautifulSoup(r.content,'html.parser')

        name = soup.find("header", {"class": "m_highlighted_next_game_header"}).span.contents
        date = soup.find("header",{"class": "m_highlighted_next_game_header"}).time.contents
        location =  soup.find("p", {"class": "m_highlighted_next_game_location"}).text
        team1 = soup.find("div", {"class": "m_highlighted_next_game_team"}).strong.contents
        team2 = soup.find("div", {"class": "m_highlighted_next_game_team m_highlighted_next_game_second_team"}).strong.contents
        opponent = team2[0]
        if team1[0] != 'Real Madrid':
            opponent = team1[0]

        time = soup.find("div",{"class": "m_highlighted_next_game_info_wrapper"}).time.contents

        time1 = time[0]
        hour = int(time1[:2])+4
        minute = int(time1[3:5])
        d = date[0]
        day = int(d[8:10])
        year = int(d[:4])
        month = int(d[5:7])
        n_day = day
        n_hour = hour
        if hour>24:
            n_hour = hour-24
            n_day = day+1

        start = datetime.datetime.now()
        end = datetime.datetime(year = year, month = month, day = n_day, hour = n_hour, minute = minute)
        diff  = end - start
        delta = diff
        a = 1
        if delta.days == 0:
            a =0
        self.days = str(delta.days)
        hour_string = str(delta).split(', ')[a]
        self.hours = hour_string.split(':')[0]
        self.minutes = hour_string.split(':')[1]
        self.seconds = hour_string.split(':')[2].split('.')[0]
        self.l_name = name[0]
        self.op_team = opponent
        self.place = location

class countdown(App):
    def build(self):
        counter = Counter_Timer()
        Clock.schedule_interval(counter.update, 1.0)
        return counter

if __name__=='__main__':
    Window.clearcolor = get_color_from_hex('#101216')

    countdown().run()
