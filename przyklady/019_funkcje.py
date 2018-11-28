import turtle


def kwadrat(dlugosc_boku):
    for i in range(4):
        turtle.forward(dlugosc_boku)
        turtle.left(90)


kwadrat(100)
kwadrat(200)
kwadrat(350)

turtle.mainloop()

