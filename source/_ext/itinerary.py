from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective

ITINERARY_ALL = 'itinerary_all_itineraries'

class itinerary(nodes.Admonition, nodes.Element):
    pass


class itinerarylist(nodes.General, nodes.Element):
    pass


def visit_itinerary_node(self, node):
    self.visit_admonition(node)


def depart_itinerary_node(self, node):
    self.depart_admonition(node)


class ItineraryListDirective(Directive):
    def run(self):
        return [itinerarylist('')]

class ItineraryDirective(SphinxDirective):
    has_content = True

    def run(self):
        targetid = f'itinerary-{self.env.new_serialno("itinerary")}'
        target_node = nodes.target('', '', ids=[targetid])

        itinerary_node = itinerary('\n'.join(self.content))
        itinerary_node += nodes.title(_('Itinerary'), _('Itinerary'))
        self.state.nested_parse(self.content, self.content_offset, itinerary_node)

        if not hasattr(self.env, 'itinerary_all_itineraries'):
            self.env.itinerary_all_itineraries = []
        
        self.env.itinerary_all_itineraries.append({
            'docname': self.env.docname,
            'lineno': self.lineno,
            'itinerary': itinerary_node.deepcopy(),
            'target': target_node,
        })

        return [target_node, itinerary_node]

def purge_itineraries(app, env, docname):
    if not hasattr(env, ITINERARY_ALL):
        return
    env.itinerary_all_itineraries = [itinerary for itinerary in env.itinerary_all_itineraries
    if itinerary['docname'] != docname]


def merge_itineraries(app, env, docname, other):
    if not hasattr(env, ITINERARY_ALL):
        return []
    if hasattr(other, ITINERARY_ALL):
        env.itinerary_all_itineraries.extend(other.itinerary_all_itineraries)


def process_itinerary_nodes(app, doctree, fromdocname):
    env = app.builder.env

    if not hasattr(env, ITINERARY_ALL):
        env.itinerary_all_itineraries = []

    for node in doctree.traverse(itinerarylist):
        content = []
        for itinerary_info in env.itinerary_all_itineraries:
            paragraph = nodes.paragraph()
            filename = env.doc2path(itinerary_info['docname'], base=None)
            description = _(f'(The original entry is located in {filename}, '
                            f'line {itinerary_info["lineno"]}')
            paragraph += nodes.Text(description, description)

            new_node = nodes.reference('', '')
            inner_node = nodes.emphasis(_('here'), _('here'))
            new_node['refdocname'] = itinerary_info['docname']
            new_node['refuri'] = app.builder.get_relative_uri(
                fromdocname, itinerary_info['docname']
            )
            new_node['refuri'] += f'#{itinerary_info["target"]["refid"]}'
            new_node.append(inner_node)
            paragraph += new_node
            paragraph += nodes.Text('.)', '.)')

            content.append(itinerary_info['itinerary'])
            content.append(paragraph)
        
        node.replace_self(content)


def setup(app):
    app.add_node(itinerarylist)
    app.add_node(itinerary,
            html=(visit_itinerary_node, depart_itinerary_node),
            latex=(visit_itinerary_node, depart_itinerary_node),
            text=(visit_itinerary_node, depart_itinerary_node)
    )
    app.add_directive('itinerary', ItineraryDirective)
    app.add_directive('itinerarylist', ItineraryListDirective)
    app.connect('doctree-resolved', process_itinerary_nodes)
    app.connect('env-purge-doc', purge_itineraries)
    app.connect('env-merge-info', merge_itineraries)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
