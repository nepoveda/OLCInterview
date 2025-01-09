from OOP.html_elements import Div

div = Div(content="I'm the wrapper element")
div.add_children(Div(content="This is a child of the div"))
print(div)
