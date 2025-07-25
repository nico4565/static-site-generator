# static-site-generator

 ----------------------------------

## Usage
As the title implies, this is meant to generate static sites from .md files.
The core of the project consists of methods and logic designed to analyze, parse, and process the .md file. The end product is an .html file.

The .md files are dissected into blocks of text. These blocks are then individually analyzed and transformed into HtmlNodes, forming a tree structure that represents the .html document.

Here is an example of the transformation:

### Block A 

"This is a block of text with some inline features such as **bold text**, _italic text_, and ```code``` text."

The  block of text above would be than transformed into a tree of nodes, which I'll try to graphically represent here:

```
[Main parent NODE: <div>
    [Secondary parent: <p>
        [Leaf Node: "This is a block of text with some inline features such as "]
        [Leaf Node: <b>"bold text"</b>]
        [Leaf Node: ", "]
        [Leaf Node: <i>"italic text"</i>]
        [Leaf Node: " and "]
        [Leaf Node: <code>"code text"</code>]
        [Leaf Node: "."]
    </p>]
</div>]
```
