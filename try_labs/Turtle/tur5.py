import turtle

turtle.shape('turtle')

kolvo_kvadratov = 10
storona_pervogo_kvadrata = 20
shag_kvadrata = 20

for  i  in  range(kolvo_kvadratov):

    storona_kvadrata = storona_pervogo_kvadrata + i*shag_kvadrata

    turtle.forward(storona_kvadrata)
    turtle.left(90)
    turtle.forward(storona_kvadrata)
    turtle.left(90)
    turtle.forward(storona_kvadrata)
    turtle.left(90)
    turtle.forward(storona_kvadrata)

    if  i == (kolvo_kvadratov - 1):
        break

    turtle.right(45)
    turtle.penup()
    turtle.forward(shag_kvadrata/2**0.5)
    turtle.pendown()
    turtle.left(135)    
