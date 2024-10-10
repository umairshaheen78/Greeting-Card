import turtle

#turtle.Screen() allows you to define your screen size 
screen = turtle.Screen() 
screen.setup(500,500)
screen.bgcolor("#274173")

# dictionary of colors 
colors = {
  "blue": "#8AB6E4", 
  "yellow": "#F3F5A6", 
  "purple": "#AEBFF1", 
  "gray": "#8B9493",
  "pink" : "#F5BAF4"
}

artist = turtle.Turtle()
artist.shape("turtle")
artist.color(colors["blue"])

artist.penup()
artist.goto(0, 50)

#(font-family, font-size, font-style)
style = ("cursive", 30, "normal")
artist.write("-------------------------", font = style, align = "center")


artist.goto(0, 0)
artist.color(colors["yellow"])
style = ("fantasy", 30, "normal")
artist.write("Happy Friday!!", font = style, align = "center")

artist.goto(0, -50)
artist.color(colors["blue"])
style = ("cursive", 30, "normal")
artist.write("-------------------------", font = style, align = "center")

artist.goto(100, -200)
artist.color(colors["gray"])
style = ("Trattatello", 30, "normal")
artist.write("- Umair Shaheen", font = style, align = "center")
artist.hideturtle()
