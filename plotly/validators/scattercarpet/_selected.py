import _plotly_utils.basevalidators


class SelectedValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='selected', parent_name='scattercarpet', **kwargs
    ):
        super(SelectedValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Selected',
            data_docs="""
            marker
                plotly.graph_objs.scattercarpet.selected.Marker
                instance or dict with compatible properties
            textfont
                plotly.graph_objs.scattercarpet.selected.Textfo
                nt instance or dict with compatible properties""",
            **kwargs
        )
