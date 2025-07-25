# static-site-generator

 ----------------------------------

## Usage
As the title implies, this is meant to generate **static sites**.
The core of the project consists of methods and logic designed to analyze, parse, and process these .md files.
The end product is an .html file.

The .md files are dissected into blocks of text. These blocks are then individually analyzed and transformed into HtmlNodes, forming a tree structure that represents the .html document.

The content folder contains all the .md origin files of our chosing, if we want to generate a different static site, that's the folder we have to update.
The static folder contains the .css , plus all the assets required (like images).
We can also find a template.html file, much needed for the final transformation.



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
