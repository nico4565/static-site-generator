class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        for prop in self.props:
            result += f" {prop}=\"{self.props[prop]}\""
        
        return result
    
    def __repr__(self): 

        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"