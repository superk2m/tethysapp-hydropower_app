from tethys_sdk.base import TethysAppBase, url_map_maker


class HydropowerApp(TethysAppBase):
    """
    Tethys app class for Hydropower App.
    """

    name = 'Hydropower App'
    index = 'hydropower_app:home'
    icon = 'hydropower_app/images/icon.gif'
    package = 'hydropower_app'
    root_url = 'hydropower-app'
    color = '#2ecc71'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='hydropower-app',
                           controller='hydropower_app.controllers.home'),
        )

        return url_maps