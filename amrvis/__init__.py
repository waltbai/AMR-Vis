"""Parse and draw AMR graph."""
import os

import penman
from graphviz import Digraph
from penman.models import amr, noop

DEFAULT_DIR = "./out/"


def draw(amr_text, output_path=None, reverse=True, view=False):
    """Draw amr graph.

    :param amr_text: serialized AMR text.
    :param output_path: output path.
    :param reverse: if '-of'-like relations are reversed.
    :param view: whether to automatically open the image.
    """
    # Parse AMR text with penman
    if reverse:
        model = amr.model
    else:
        model = noop.model
    penman_graph = penman.decode(amr_text, model=model)
    # Construct graph
    if output_path is None:
        output_path = os.path.join(DEFAULT_DIR, "default")
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
    graph = Digraph(format="png", filename=output_path)
    # Draw instance nodes
    for id_, _, value in penman_graph.instances():
        graph.node(id_, value, shape="ellipse")
    # Draw edges
    for head, relation, tail in penman_graph.edges():
        graph.edge(head, tail, relation)
    # Draw attribute nodes
    for id_, relation, value in penman_graph.attributes():
        # create unique id for each attribute value
        attr_id = f"{id_}-{value}"
        graph.node(attr_id, value, shape="box")
        graph.edge(id_, attr_id, relation)
    graph.render(filename=output_path, view=view)
