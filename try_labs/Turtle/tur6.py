import turtle

turtle.shape('turtle')

kolvo_lap_pauka = 9
dlina_lapi = 50

ugol_povorota = 360/kolvo_lap_pauka

for  i  in  range(kolvo_lap_pauka):
    turtle.forward(dlina_lapi)
    turtle.stamp()
    turtle.backward(dlina_lapi)
    turtle.left(ugol_povorota)
