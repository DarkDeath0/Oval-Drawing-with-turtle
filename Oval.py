import turtle

tilt = int(input('shib ra vard konid : '))
ghotre_bozrg = int(input('ghotre_bozrg ra vard konid: '))
ghotre_kochick = int(input('ghotre_kochick ra vard konid: '))

def bizi (tilt,ghotre_bozrg,ghotre_kochick):
    wn = turtle.Screen()
    wn.bgcolor('black')

    jojo = turtle.Turtle()
    jojo.color('red')
    jojo.pensize(3)

    jojo.seth(-45+tilt)
    jojo.circle(ghotre_bozrg,90)
    jojo.circle(ghotre_kochick,90)
    jojo.circle(ghotre_bozrg,90)
    jojo.circle(ghotre_kochick,90)
    # jojo.goto(0,0)

    wn.mainloop()

bizi(tilt,ghotre_bozrg,ghotre_kochick)

