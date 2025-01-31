from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        
        if self.tag is None:
            return self.value
        
        props_str = self.props_to_html() if self.props else ""
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"