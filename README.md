# MTGDeckbuilding

Python tool to handle the import and export of MTG decks from a series of tools alongside providing output features that enable enhancement of decklists

<h2>Usage</h2>

* via python module call

```python
import mtgDelver
config = {
    'output':'output.html',
    'outputType':'VariantsHTML',
    'input':'decks/Ardenn.txt',
    'inputType':'archideckt'
}
response = mtgDelver.execute(config)
```

* via command line
```bash
python3 mtgDelver.py --output output.html --outputType VariantsHTML --input decks/Ardenn.txt --inputType archideckt
```

<h2>Import Features</h2>

* Archideckt (default 1x CardName)
** archideckt
* MTG Delver (default csv export)
** delver

<h2>Export Features</h2>

* CardMarket Import
** MKM


<h2>Output Features</h2>

* Variants visualisation viewable in web browser

