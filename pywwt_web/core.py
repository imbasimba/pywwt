from traitlets import Bool, HasTraits


class BaseWWTWidget(HasTraits):

    def __init__(self):
        super(BaseWWTWidget, self).__init__()
        self.observe(self._on_trait_change, type='change')

    def _on_trait_change(self, changed):
        # This method gets called anytime a trait gets changed. Since this class
        # gets inherited by the Jupyter widgets class which adds some traits of
        # its own, we only want to react to changes in traits that have the wwt
        # metadata attribute (which indicates the name of the corresponding WWT
        # setting).
        wwt_name = self.trait_metadata(changed['name'], 'wwt')
        if wwt_name is not None:
            self._send_msg(event='setting_set',
                           setting=wwt_name,
                           value=changed['new'])

    def _send_msg(self, **kwargs):
        # This method should be overridden and should send the message to WWT
        raise NotImplementedError()

    # TODO: need to add all settings as traits

    constellation_figures = Bool(False, help='Whether to show the constellations').tag(wwt='showConstellationFigures', sync=True)

    # TODO: need to add more methods here.

    def center_on_coordinates(self, ra, dec, fov, instant=True):
        # TODO: make this method take SkyCoord objects
        self._send_msg(event='center_on_coordinates',
                       ra=ra, dec=dec, fov=fov, instant=instant)