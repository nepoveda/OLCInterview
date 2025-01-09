from __future__ import annotations


class HTMLElement:
    """
    Represents an HTML element.

    Attributes:
        tag (str): The tag name of the HTML element.
        id (str, optional): The id attribute of the HTML element.
        attributes (dict[str, str]): A dictionary of other attributes for the HTML element.
        content (str): The inner content of the HTML element.
        children (list[HTMLElement]): A list of child HTML elements.
    """

    def __init__(
        self,
        tag: str,
        id: str = None,
        attributes: dict[str, str] = None,
        content: str = "",
    ):
        """
        Initializes an HTMLElement instance.

        Args:
            tag (str): The tag name of the HTML element.
            id (str, optional): The id attribute of the HTML element. Defaults to None.
            attributes (dict[str, str], optional): A dictionary of other attributes for the HTML element. Defaults to None.
            content (str, optional): The inner content of the HTML element. Defaults to "".
        """
        self.tag: str = tag
        self.attributes: dict[str, str] = attributes or {}
        self.content: str = content
        self.children: list[HTMLElement] = []
        self.id: str = id

    def __str__(self):
        """
        Returns the string representation of the HTML element.

        Returns:
            str: The string representation of the HTML element.
        """
        if self.id:
            self.attributes = {"id": self.id, **self.attributes}
        attrs = " ".join(f'{key}="{value}"' for key, value in self.attributes.items())
        children_str = " ".join(str(child) for child in self.children)
        return (
            f"<{self.tag} {attrs}>\r\n{self.content}\r\n{children_str}\r\n</{self.tag}>"
        )

    def add_children(self, child: HTMLElement):
        """
        Adds a child element to the HTML element if it is not already present.

        Args:
            child (HTMLElement): The child element to add.

        Returns:
            HTMLElement: The current instance of HTMLElement.
        """
        return self.children.append(child) if child not in self.children else self


class Div(HTMLElement):
    """
    Represents a <div> HTML element.
    """

    def __init__(self, attributes: dict[str, str] = None, content: str = ""):
        """
        Initializes a Div instance.

        Args:
            attributes (dict[str, str], optional): A dictionary of attributes for the div element. Defaults to None.
            content (str, optional): The inner content of the div element. Defaults to "".
        """
        super().__init__("div", attributes=attributes, content=content)


class Anchor(HTMLElement):
    """
    Represents an <a> HTML element.
    """

    def __init__(self, href: str, content: str = "", attributes: dict[str, str] = None):
        """
        Initializes an Anchor instance.

        Args:
            href (str): The href attribute of the anchor element.
            content (str, optional): The inner content of the anchor element. Defaults to "".
            attributes (dict[str, str], optional): A dictionary of other attributes for the anchor element. Defaults to None.
        """
        attributes = {"href": href, **(attributes or {})}
        super().__init__("a", attributes=attributes, content=content)


class Input(HTMLElement):
    """
    Represents an <input> HTML element.
    """

    def __init__(
        self,
        type: str,
        name: str,
        value: str = "",
        attributes: dict[str, str] = None,
    ):
        """
        Initializes an Input instance.

        Args:
            type (str): The type attribute of the input element.
            name (str): The name attribute of the input element.
            value (str, optional): The value attribute of the input element. Defaults to "".
            attributes (dict[str, str], optional): A dictionary of other attributes for the input element. Defaults to None.
        """
        attributes = {"type": type, "name": name, "value": value, **(attributes or {})}
        self.children = []
        super().__init__("input", attributes=attributes)


class Option(HTMLElement):
    """
    Represents an <option> HTML element.
    """

    def __init__(self, value: str, attributes: dict[str, str] = None):
        """
        Initializes an Option instance.

        Args:
            value (str): The value attribute of the option element.
            attributes (dict[str, str], optional): A dictionary of other attributes for the option element. Defaults to None.
        """
        attributes = {"value": value, **(attributes or {})}
        super().__init__("option", attributes=attributes)


class OptGroup(HTMLElement):
    """
    Represents an <optgroup> HTML element.
    """

    def __init__(
        self,
        label: str,
        options: list[Option] = None,
        attributes: dict[str, str] = None,
    ):
        """
        Initializes an OptGroup instance.

        Args:
            label (str): The label attribute of the optgroup element.
            options (list[Option], optional): A list of Option elements. Defaults to None.
            attributes (dict[str, str], optional): A dictionary of other attributes for the optgroup element. Defaults to None.
        """
        attributes = {"label": label, **(attributes or {})}
        super().__init__("optgroup", attributes=attributes)
        self.children = options or []


class Label(HTMLElement):
    """
    Represents a <label> HTML element.
    """

    def __init__(self, for_: str, content: str = "", attributes: dict[str, str] = None):
        """
        Initializes a Label instance.

        Args:
            for_ (str): The for attribute of the label element.
            content (str, optional): The inner content of the label element. Defaults to "".
            attributes (dict[str, str], optional): A dictionary of other attributes for the label element. Defaults to None.
        """
        attributes = {"for": for_, **(attributes or {})}
        super().__init__("label", attributes=attributes, content=content)


class Select(HTMLElement):
    """
    Represents a <select> HTML element.
    """

    def __init__(
        self,
        name: str,
        label: str = "",
        options: list[Option | OptGroup] = None,
        attributes: dict[str, str] = None,
    ):
        """
        Initializes a Select instance.

        Args:
            name (str): The name attribute of the select element.
            label (str, optional): The label attribute of the select element. Defaults to "".
            options (list[Option | OptGroup], optional): A list of Option or OptGroup elements. Defaults to None.
            attributes (dict[str, str], optional): A dictionary of other attributes for the select element. Defaults to None.
        """
        attributes = {"for": name, "label": label, **(attributes or {})}
        super().__init__("select", attributes=attributes)
        self.children = options or []


class Image(HTMLElement):
    """
    Represents an <img> HTML element.
    """

    def __init__(self, src: str, alt: str, attributes: dict[str, str] = None):
        """
        Initializes an Image instance.

        Args:
            src (str): The src attribute of the img element.
            alt (str): The alt attribute of the img element.
            attributes (dict[str, str], optional): A dictionary of other attributes for the img element. Defaults to None.
        """
        attributes = {"src": src, "alt": alt, **(attributes or {})}
        super().__init__("img", attributes=attributes)


class Form(HTMLElement):
    """
    Represents a <form> HTML element.
    """

    def __init__(
        self,
        action: str,
        method: str,
        attributes: dict[str, str] = None,
    ):
        """
        Initializes a Form instance.

        Args:
            action (str): The action attribute of the form element.
            method (str): The method attribute of the form element.
            attributes (dict[str, str], optional): A dictionary of other attributes for the form element. Defaults to None.
        """
        attributes = {"action": action, "method": method, **(attributes or {})}
        super().__init__("form", attributes=attributes)
