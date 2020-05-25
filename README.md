# cell_def_gui: parse XML cell definitions; create GUI

We focus on *just* parsing the `<cell_definitions>` in the .xml.

Run this to generate the Python module that will become the `Cells` tab in the GUI (see google doc).
```
$ python cells.py config-immune-response.xml
```
Test the created Jupyter GUI with:
```
$ jupyter notebook test_gui.ipynb
```

Here's my earlier google doc of notes:
https://docs.google.com/document/d/1SY0PNsPWNiYilQG4NS4ysp8KbYdtkxP1wIHnpK0vu88/edit
