# AMR-Vis
Visualization for AMR graph.

## Install

[Graphviz](http://www.graphviz.org/) should be manually installed.

Then use ```pip install -e .``` to install python dependencies.

## Usage

Graphvis will automatically add suffix.

```python
import amrvis

amr_text = """(a / amr-unknown)"""
amrvis.draw(amr_text, 
            output_path="out/show",
            reverse=True,
            view=False)
```
