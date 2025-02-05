class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        res = []
        for i in self.props.items():
            res.append(f' {i[0]}="{i[1]}"')
        return "".join(res)
    
    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        props_str = self.props_to_html() if self.props else ""
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("Parent node must have a tag")
        if not children:
            raise ValueError("Parent node must have children")
        if props is None:
            props = {}

        super().__init__(tag, None, children, props)  # Explicitly set value to None

    def to_html(self):
        props_str = self.props_to_html() if self.props else ""

        # Use list comprehension + join for efficiency
        children_html = "".join(child.to_html() for child in self.children)

        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"



        