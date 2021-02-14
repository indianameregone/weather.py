from tkinter import *
import requests


ventana = Tk()
ventana.geometry("350x450")

def show_response(clima):
    name_city = clima["name"]
    desc_city = clima["weather"][0]["description"]
    temp_city = clima["main"]["temp"]
    
    show_city["text"] = name_city
    show_desc["text"] = desc_city
    show_temp["text"] = temp_city

def weather(city):
    API_key = "190b7ee2e0fb21aa9d7edcfcb354c3f7"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parametros ={"APPID" : API_key, "q": city,"units":"metric"}
    response = requests.get(URL,params = parametros)
    clima = response.json()
    show_response(clima)
    


city = Entry(ventana, font= ("Calibri",20,"normal"),justify="center")
city.pack(padx=30,pady=30)

get_weather = Button(ventana,text="Get Weather",font =("Calibri",15,"normal"),command = lambda: weather(city.get()))
get_weather.pack()

show_city = Label(font=("Calibri",30,"normal"))
show_city.pack()

show_temp = Label(font=("Calibri",20,"normal"))
show_temp.pack()

show_desc = Label(font=("Calibri",10,"normal"))
show_desc.pack()

ventana.mainloop()