import unittest

from OOP.html_elements import *


class TestHTMLElement(unittest.TestCase):
    def test_element_initialization(self):
        element = HTMLElement(
            "div", id="main", attributes={"class": "container"}, content="Hello"
        )
        self.assertEqual(element.tag, "div")
        self.assertEqual(element.id, "main")
        self.assertEqual(element.attributes, {"class": "container"})
        self.assertEqual(element.content, "Hello")
        self.assertEqual(element.children, [])

    def test_element_string_representation(self):
        element = HTMLElement(
            "div", id="main", attributes={"class": "container"}, content="Hello"
        )
        self.assertEqual(
            str(element), '<div id="main" class="container">\r\nHello\r\n</div>\r\n'
        )

    def test_add_unique_child(self):
        parent = HTMLElement("div")
        child = HTMLElement("span")
        parent.add_children(child)
        self.assertIn(child, parent.children)
        self.assertEqual(len(parent.children), 1)

    def test_add_duplicate_child(self):
        parent = HTMLElement("div")
        child = HTMLElement("span")
        parent.add_children(child)
        parent.add_children(child)
        self.assertEqual(len(parent.children), 1)

    def test_div_initialization(self):
        div = Div(attributes={"class": "container"}, content="Hello")
        self.assertEqual(div.tag, "div")
        self.assertEqual(div.attributes, {"class": "container"})
        self.assertEqual(div.content, "Hello")

    def test_anchor_initialization(self):
        anchor = Anchor(href="https://example.com", content="Click here")
        self.assertEqual(anchor.tag, "a")
        self.assertEqual(anchor.attributes, {"href": "https://example.com"})
        self.assertEqual(anchor.content, "Click here")

    def test_input_initialization(self):
        input_element = Input(type="text", name="username", value="user1")
        self.assertEqual(input_element.tag, "input")
        self.assertEqual(
            input_element.attributes,
            {"type": "text", "name": "username", "value": "user1"},
        )

    def test_option_initialization(self):
        option = Option(value="1")
        self.assertEqual(option.tag, "option")
        self.assertEqual(option.attributes, {"value": "1"})

    def test_optgroup_initialization(self):
        option1 = Option(value="1")
        option2 = Option(value="2")
        optgroup = OptGroup(label="Group 1", options=[option1, option2])
        self.assertEqual(optgroup.tag, "optgroup")
        self.assertEqual(optgroup.attributes, {"label": "Group 1"})
        self.assertIn(option1, optgroup.children)
        self.assertIn(option2, optgroup.children)

    def test_label_initialization(self):
        label = Label(for_="input1", content="Username")
        self.assertEqual(label.tag, "label")
        self.assertEqual(label.attributes, {"for": "input1"})
        self.assertEqual(label.content, "Username")

    def test_select_initialization(self):
        option1 = Option(value="1")
        option2 = Option(value="2")
        select = Select(name="select1", options=[option1, option2])
        self.assertEqual(select.tag, "select")
        self.assertEqual(select.attributes, {"for": "select1", "label": ""})
        self.assertIn(option1, select.children)
        self.assertIn(option2, select.children)

    def test_image_initialization(self):
        image = Image(src="static/image.png", alt="An image")
        self.assertEqual(image.tag, "img")
        self.assertEqual(
            image.attributes, {"src": "static/image.png", "alt": "An image"}
        )

    def test_form_initialization(self):
        form = Form(action="/submit", method="post")
        self.assertEqual(form.tag, "form")
        self.assertEqual(form.attributes, {"action": "/submit", "method": "post"})
