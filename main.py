import kivy
import pymongo
from pymongo import MongoClient
import datetime


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
import string

class Second(Screen):
    text = StringProperty ('')
    listReminders = ObjectProperty()
    def ukaz_vse(self):
        cluster = MongoClient (
            "mongodb+srv://root:HonzaKupka1818*@cluster0-urwfe.mongodb.net/test?retryWrites=true&w=majority")
        db = cluster["mycak"]
        collection = db["udaje"]

        result = collection.find()

        resultvse = ""
        for x in enumerate(result):
            resultvse += str(x) + "\n"


            self.listReminders.text = str(resultvse)


class Manager(ScreenManager):
    pass


class Start(Screen):
    user = ObjectProperty()

    def zapsat(self):
        cluster = MongoClient (
            "mongodb+srv://root:HonzaKupka1818*@cluster0-urwfe.mongodb.net/test?retryWrites=true&w=majority")
        db = cluster["mycak"]
        collection = db["udaje"]
        mongo_querry2 = (self.user.text)
        mongo_querry3 = (datetime.datetime.utcnow())
        collection.insert_many(
                            [{"jmeno":mongo_querry2,"date":mongo_querry3 }
                             ]
                               )



    def ukaz(self):
        cluster = MongoClient (
            "mongodb+srv://root:HonzaKupka1818*@cluster0-urwfe.mongodb.net/test?retryWrites=true&w=majority")
        db = cluster["mycak"]
        collection = db["udaje"]

        results = collection.find()
        results1 = collection.find().sort([('_id', -1)]).limit(2)

        for result in results:

            more = result["jmeno"]
            more1= result["date"]


            self.ids.labelfetchname.text=str(more)
            self.ids.labelfetchdate.text = str(more1)

        for result in results1:
            more = result["jmeno"]
            more1 = result["date"]

            self.ids.labelfetchname1.text = str(more)
            self.ids.labelfetchdate1.text = str(more1)


class Main(App):
    cluster = MongoClient (
        "mongodb+srv://root:HonzaKupka1818*@cluster0-urwfe.mongodb.net/test?retryWrites=true&w=majority")
    db = cluster["mycak"]
    collection = db["udaje"]


if __name__ == "__main__":
    Main().run()



