import tkinter as tk
import json
import requests
from PIL import ImageTk, Image


HEIGHT = 575
WIDTH = 960

class Pogoda:
  def __init__(self, miasto):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {"callback": "test", "id": "2172797", "units": "%22metric%22 or %22imperial%22",
                     "mode": "xml%2C html", "q": miasto}
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "bf66404f35mshecd7b9b3525744bp1d79a8jsna94048c27ef6"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    jaka_pogoda.delete('1.0', tk.END)
    jaka_pogoda.insert(tk.INSERT,"Zachmurzenie: " + json.loads(response.text[5:-1])['weather'][0]['main'] + "\n")
    jaka_pogoda.insert(tk.INSERT, "Temperatura: " + str(int((json.loads(response.text[5:-1])['main']['temp']) - 273.15)) +" C\n")
    jaka_pogoda.insert(tk.INSERT, "Odczuwalna Temperatura: : " + str(int((json.loads(response.text[5:-1])['main']['feels_like']) - 273.15)) + " C\n")
    jaka_pogoda.insert(tk.INSERT, "Minimalna Temperatura: " + str(int((json.loads(response.text[5:-1])['main']['temp_min']) - 273.15)) + " C \n")
    jaka_pogoda.insert(tk.INSERT, "Maksymalna Temperatura: " + str(int((json.loads(response.text[5:-1])['main']['temp_max']) - 273.15)) + " C \n")



root = tk.Tk()
root.iconbitmap(r'cloud.ico')

root.title("Moja pierwsza aplikacja")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, background="#C9F6CD")

frame.place(relwidth=1, relheight=1)

img = ImageTk.PhotoImage(Image.open("globus.jpg"))

label = tk.Label(frame, image=img)
label.pack()

miasto = tk.Entry(frame, bd="3")
miasto.place(relheight=0.05, relwidth=0.3, relx=0.4, rely=0.1)

jaka_pogoda = tk.Text(frame)
jaka_pogoda.config(state="normal")
jaka_pogoda.place(relheight=0.3, relwidth=0.4, relx=0.4, rely=0.3)

button = tk.Button(frame, text="Sprawdz pogode", bd="3", command=lambda: Pogoda(miasto.get()))
button.place(relheight=0.05, relwidth=0.1, relx=0.1, rely=0.1)


root.mainloop()







