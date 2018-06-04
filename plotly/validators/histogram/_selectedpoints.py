import _plotly_utils.basevalidators


class SelectedpointsValidator(_plotly_utils.basevalidators.AnyValidator):

    def __init__(
        self, plotly_name='selectedpoints', parent_name='histogram', **kwargs
    ):
        super(SelectedpointsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            **kwargs
        )