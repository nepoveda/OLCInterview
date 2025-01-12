from OOP.html_elements import Div, Form, Anchor, OptGroup, Option, Select
from html_elements import Label, Image, Input, BreakLine

container = Div(attributes={"class": "container"})

image = Image(src="static/image.png", alt="An image")
container.add_children(image)
container.add_children(BreakLine())

anchor = Anchor(href="https://example.com", content="Click here")
container.add_children(anchor)
container.add_children(BreakLine())

label = Label(for_="myForm", content="Example Form")
container.add_children(label)
container.add_children(BreakLine())

form = Form(attributes={"id": "myForm"}, action="#", method="POST")
form_input = Input(
    type="text", name="username", attributes={"placeholder": "Enter your username"}
)
form.add_children(form_input)
form.add_children(BreakLine())

opt_swedish_cars = OptGroup(
    label="Swedish Cars",
    options=[
        Option(value="Volvo"),
        Option(value="Saab"),
    ],
)
opt_german_cars = OptGroup(
    label="German Cars",
    options=[
        Option(value="Mercedes"),
        Option(value="Audi"),
        Option(value="BMW"),
    ],
)
select = Select(name="cars", options=[opt_swedish_cars, opt_german_cars])
form.add_children(select)

container.add_children(form)

# Write the HTML content to a file named index.html
with open("index.html", "w") as file:
    file.write(str(container))
